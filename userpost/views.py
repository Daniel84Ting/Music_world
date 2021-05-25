from .forms import CategoryForm, PostForm
from .models import Post
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from django.views.generic import *
import uuid

# Create your views here.

@login_required
def views_index(request):

    events = Post.objects.all()
    return render(request, 'musics/index.html',{"events":events})

@login_required
def views_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            post = Post(
                title=request.POST['title'],
                events_date_time=request.POST['events_date_time'],
                location=request.POST['location'],
                description=request.POST['description'],
                date_posted=request.POST['date_posted'],
                cover=request.FILES['cover']
                )
            
            post.save()
            categories = form.cleaned_data['categories']
            for cat in categories:
                post.categories.add(cat)
            return redirect('events:musics_index')
    
    posts = Post.objects.all()

    context = {"form":form, "posts":posts}
    return render(request, 'posts/post.html', context)

@login_required
def views_postShow(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return redirect('events:musics_index')

    if request.GET.get('action') == 'del':
        post.delete()
        return redirect('events:musics_index')

    if request.method == 'POST' and request.GET['action'] == 'edit':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('posts:posts_show', post.id)
        
    if request.GET.get('action') == 'edit':
        form = PostForm(instance=post)

        context = {"form":form, "post":post, "edit":True}
        return render(request, 'posts/show.html', context)

    

    review_form = ReviewForm()

    context = {"post":post, "edit":False, "review_form":review_form}
    return render(request, 'posts/show.html', context)

@login_required
def views_create_category(request):

    category_form = CategoryForm()
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('posts:category_create')

    context = {"category_form":category_form}
    return render(request, 'posts/create_category.html', context)