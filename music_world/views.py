from reviews.forms import ReviewForm
from music_world.forms import EventForm, CategoryForm
from music_world.models import Event
from django.shortcuts import redirect, render
import uuid

# Create your views here.

def views_index(request):

    events = Event.objects.all()
    return render(request, 'musics/index.html',{"events":events})

def views_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events:musics_index')
    
    events = Event.objects.all()

    context = {"form":form, "events":events}
    return render(request, 'musics/events.html', context)

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

def views_create_category(request):

    category_form = CategoryForm()
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('events:musics_index')

    context = {"category_form":category_form}
    return render(request, 'musics/create_category.html', context)