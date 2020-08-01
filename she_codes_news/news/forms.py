from django import forms
from django.forms import ModelForm

from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ["title", "author", "pub_date", "image_url", "content"]
        widgets = {
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'new-story-form-input',
                    'placeholder': 'Select a date',
                    'type': 'date',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'new-story-form-input',
                }
            ),  
            'author': forms.TextInput(
                attrs={
                    'class': 'new-story-form-input',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'class': 'new-story-form-input',
                    'placeholder': 'Enter a url for your image.',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'new-story-form-input',
                    'id': 'content-ta',
                    'placeholder': 'Type your story here.',
                }
            ),
          
        }

