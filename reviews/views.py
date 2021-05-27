from music_world.models import Event
from reviews.models import Review
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
@csrf_exempt
@login_required
def views_create(request, event):
    if request.method == 'POST':

        form = ReviewForm(request.POST)
        if form.is_valid():
            
            
            event = Event.objects.get(pk=event)
            event.reviews.create(name=request.POST['name'], review=request.POST['review'])

            return redirect('events:musics_show', event.id)
    return HttpResponse({"message": "works"})
