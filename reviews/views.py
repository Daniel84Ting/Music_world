import json
from music_world.models import Event
from accounts.models import User
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
    if request.method == "POST":
        user = User.objects.get(pk= request.user.id)
        form = ReviewForm(request.POST, instance=User)
        if form.is_valid():
            
            event = Event.objects.get(pk=event)
            event.reviews.create(username=request.POST,review=request.POST['review'])
            
            return redirect('events:musics_show', event.id)
        
        def clean(self):
            if self.username == user is not None:
                raise ValidationError()

    return HttpResponse({"message":"it works"}) 

@csrf_exempt
@login_required
def view_reviews(request, event_id):

    if request.method == 'POST':
        
        json_data = json.loads(request.body.decode(encoding='UTF-8'))
        event = Event.objects.get(pk=event_id)
        event.reviews.create(username=request.user.username,review=json_data['review'], event=event_id)
        
        return JsonResponse({"message": "success"}, status=200, safe=True)

    reviews = Review.objects.filter(username=request.user)
    serialize = [r.serialize() for r in reviews]
    return JsonResponse(serialize, safe=False)