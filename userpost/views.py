from .forms import CategoryForm, PostForm
from .models import Post
from music_world.views import Event
from accounts.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


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
            return redirect('posts:post-index')
    
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
    
    # class views_postShow(UserPassesTestMixin, LoginRequiredMixin):
    #     model = Post
    #     success_url = '/'

    #     def test_func(self):
    #         post = self.get_object()
    #         if self.request.user == post.user:
    #             return True
    #         return False

    context = {"post":post, "edit":False}
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

    
# def views_comment(request, self, *args, **kwargs):

#     form = CommentForm
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             views_comment = self.get_object()
#             form.instance.user = request.user
#             form.instance.post = views_comment
#             form.save()
#             return redirect('posts/show.html')

#     def context_data(self, **kwargs):
#         post_comment = Comment.object.all().filter(post=self.object.id)
#         context = super().context_data(**kwargs)
#         context.update({
#             'form': self.form,
#             'post_comment': post_comment,
#         })
#         return context

#     return render(request, 'posts/show.html', context)

    