from django import forms
from django.forms import ModelForm

from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ["title", "image_url", "content"]
        widgets = {
            # 'pub_date': forms.DateInput(
            #     format=('%B/%d/%Y %H:%M'),
            #     attrs={
            #         'class': 'new-story-form-input',
            #         'placeholder': 'Select a date',
            #         # 'type': 'date',
            #     }
            # ),
            'title': forms.TextInput(
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

