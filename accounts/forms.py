from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city','country','image',)

        widgets = {
            
            'city' : forms.TextInput(attrs={
                'class': 'form-control', 
            }),
            'country' : forms.TextInput(attrs={
                'class': 'form-control', 
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

        


