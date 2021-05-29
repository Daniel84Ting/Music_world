from django import forms 
from .models import *
from .views import *
from django.forms import widgets
from bootstrap_datepicker_plus import DatePickerInput

class PostForm(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    
    class Meta:
        model = Post
        fields = ("title","events_date_time","location","description","cover",)

        widgets = {
            'title' : forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Events Title'
            }),
            'events_date_time' : forms.DateTimeInput(attrs={
                'class': 'form-control',
                'data-target': 'datetimepicker',
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

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ('user','post',)

        widgets = {
            'comment' : forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Review'
            }),
            
        }

