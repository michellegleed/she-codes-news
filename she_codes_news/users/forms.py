from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'bio']
        widgets = {
            'username': forms.TextInput(
                # attrs={
                #     'class': 'new-story-form-input',
                # }
            ),
            'image_url': forms.URLInput(
                attrs={
                    # 'class': 'new-story-form-input',
                    'placeholder': 'Enter a url for your profile image.',
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'class': 'profile-form-input',
                    'id': 'content-ta',
                    'placeholder': 'Tell us a bit about yourself.',
                }
            )
        }