from accounts.models import User, Profile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from userpost.views import Post

# Create your views here.

def views_register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        city = request.POST['city']
        country = request.POST['country']
        

        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "password in not match")
            return render(request, "accounts/register.html")
        try:
            pass
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            profile = Profile(city=city, country=country, user=user)
            profile.save()
        
        except IntegrityError:
            messages.error(request, "Username is taken already")
            return render(request, 'accounts/register.html')

        login(request, user)
        return redirect("events:musics_index")
    
    else:
        form = UserCreationForm() 
        return render(request, "accounts/register.html", {"form": form})

    return render(request, "accounts/register.html")


def views_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("events:musics_index")

        else:
            messages.error(request, "username or password is incorrect")
            return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")


def views_logout(request):

    logout(request)
    return redirect('accounts:login')

@login_required
def views_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('accounts:profile')

    else:
        profile_form = ProfileForm(instance=request.user.profile)
    
    posts = Post.objects.all()

    context = {'profile_form': profile_form, 'posts':posts}

    return render(request, 'accounts/profile.html', context)