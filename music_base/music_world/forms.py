from django import forms 
from django.forms import widgets
from music_world.models import Event


class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = '__all__'

        widgets = {
            'title' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Events Title'
            }),
            'events_date_time' : forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            }),
            'location' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Events Location'
            }),
            'description' : forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Events Description'
            }),
            'cover': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
