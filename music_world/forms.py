from django import forms 
from .models import *
# from django.forms import widgets



class EventForm(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    
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
                'data-target': '#datetimepicker1',
                'placeholder': 'yyyy-mm-dd  00:00'
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

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'

