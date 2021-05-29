from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
        
    class Meta:
        model = Review
        exclude = ('user','name','event',)

        widgets = {
            'review' : forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Review'
            }),
            
        }