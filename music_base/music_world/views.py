from music_world.forms import EventForm
from music_world.models import Event
from django.shortcuts import redirect, render

# Create your views here.

def views_index(request):

    events = Event.objects.all()
    return render(request, 'musics/index.html',{"events":events})

def views_profile(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('musics_index')
    
    events = Event.objects.all()

    return render(request, 'musics/profile.html', {"form":form, "events":events})