from music_world.forms import EventForm
from music_world.models import Event
from django.shortcuts import redirect, render

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
            return redirect('musics_index')
    
    events = Event.objects.all()

    return render(request, 'musics/events.html', {"form":form, "events":events})

def views_show(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return redirect('musics_index')

    form = EventForm(instance=event)

    if request.GET.get('action') == 'edit' and request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)


        if form.is_valid():
            form.save()
            return redirect('musics_show', event.id)
        
    if request.GET.get('action') == 'edit':
        return render(request, 'musics/show.html', {"form":form, "event":event, "edit":True})

    if request.GET.get('action') == 'del':
        event.delete()
        return redirect('musics_index')

    return render(request, 'musics/show.html', {"form":form, "event":event, "edit":False})