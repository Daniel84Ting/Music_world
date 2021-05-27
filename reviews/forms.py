from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
        
    class Meta:
        model = Review
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'review' : forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Review'
            }),
            'date_posted' : forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1',
            }),
            'event': forms.Select(attrs={
                'class': 'form-control'
            })
            
        }