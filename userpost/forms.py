from django import forms 
from .models import *
from django.forms import widgets

class PostForm(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            # 'username' : forms.TextInput(attrs={
            #     'class': 'form-control',
            # }),
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
            'date_posted' : forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1',
            }),
            'cover': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'

# class CommentForm(forms.ModelForm):
#     content = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'md-textarea form-control' ,
#         'placeholder': 'comment here ... ',
#         'rows': '4',
#         }))
    
#     class Meta:
#         model = Comment
#         fields = ("content",)

