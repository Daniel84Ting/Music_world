from reviews.forms import ReviewForm
from music_world.forms import EventForm
from music_world.models import Event
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from userpost.views import Post
import uuid

# Create your views here.
@login_required
def views_index(request):

    events = Event.objects.all()
    posts = Post.objects.all()
    return render(request, 'musics/index.html',{"events":events, "posts":posts})


@login_required
def views_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = Event(
                title=request.POST['title'],
                events_date_time=request.POST['events_date_time'],
                location=request.POST['location'],
                description=request.POST['description'],
                date_posted=request.POST['date_posted'],
                cover=request.FILES['cover']
                )
            
            event.save()
            return redirect('events:musics_index')
    
    events = Event.objects.all()

    context = {"form":form, "events":events}
    return render(request, 'musics/events.html', context)

@login_required
def views_show(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return redirect('events:musics_index')

    if request.GET.get('action') == 'del':
        event.delete()
        return redirect('events:musics_index')

    if request.method == 'POST' and request.GET['action'] == 'edit':
        form = EventForm(request.POST, request.FILES, instance=event)

        if form.is_valid():
            form.save()
            return redirect('events:musics_show', event.id)
        
    if request.GET.get('action') == 'edit':
        form = EventForm(instance=event)

        context = {"form":form, "event":event, "edit":True}
        return render(request, 'musics/show.html', context)


    review_form = ReviewForm()

    context = {"event":event, "edit":False, "review_form":review_form}
    return render(request, 'musics/show.html', context)

