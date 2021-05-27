from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
        
    class Meta:
        model = Review
        fields = ("review","date_posted",)

        widgets = {
            
            'review' : forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Events Review'
            }),
            'date_posted' : forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1',
            }),
            
        }