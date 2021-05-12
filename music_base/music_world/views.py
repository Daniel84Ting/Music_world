from django.shortcuts import render

# Create your views here.

def views_index(request):
    return render(request, 'musics/index.html')