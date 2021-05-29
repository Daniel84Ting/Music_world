from .forms import CategoryForm, PostForm, CommentForm
from .models import Post
from music_world.views import Event
from accounts.models import User
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def views_post_index(request):

    posts = Post.objects.all()
    return render(request, 'posts/index.html',{"posts":posts})


@login_required
def views_post(request):
    form = PostForm()

    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                username=user,
                title=request.POST['title'],
                events_date_time=request.POST['events_date_time'],
                location=request.POST['location'],
                description=request.POST['description'],
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
        return redirect('posts:post-index')

    if request.GET.get('action') == 'del':
        post.delete()
        return redirect('posts:post-index')

    if request.method == 'POST' and request.GET['action'] == 'edit':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('posts:posts_show', post.id)
        
    if request.GET.get('action') == 'edit':
        form = PostForm(instance=post)

        context = {"form":form, "post":post, "edit":True}
        return render(request, 'posts/show.html', context)
    
    comment_form = CommentForm()

    context = {"post":post, "edit":False, "comment_form":comment_form}
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

    
@login_required
def views_comment(request, post):
    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid():
            
            
            post = Post.objects.get(pk=post)
            post.comments.create(user=request.user, comment=request.POST['comment'])

            return redirect('posts:posts_show', post.id)
    return HttpResponse({"message": "works"})

    