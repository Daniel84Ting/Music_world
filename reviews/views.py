import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from music_world.models import Event
from reviews.models import Review
from reviews.forms import ReviewForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
# import uuid

# Create your views here.
@login_required
def views_create(request, event):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            
            event = Event.objects.get(pk=event)
            event.reviews.create(name=request.POST['name'],review=request.POST['review'])

            return redirect('events:musics_show', event.id)
    
    # if request.GET.get('action') == 'del':
    #     event.delete()
    #     return redirect('events:musics_show')

    return HttpResponse({"message":"it works"}) 

@csrf_exempt
@login_required
def view_reviews(request, event_id):

    if request.method == 'POST':
        
        json_data = json.loads(request.body.decode(encoding='UTF-8'))
        event = Event.objects.get(pk=event_id)
        event.reviews.create(name=request.user.username,review=json_data['review'], event=event_id)
        
        return JsonResponse({"message": "success"}, status=200, safe=True)

    reviews = Review.objects.filter(name=request.user)
    serialize = [r.serialize() for r in reviews]
    return JsonResponse(serialize, safe=False)