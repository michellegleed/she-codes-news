from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic

from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'users/createAccount.html'

class UserProfileView(generic.DetailView):
    # model = CustomUser
    template_name = 'users/profile.html'
    
    def get_queryset(self):
        '''Return all news stories.'''
        return CustomUser.get_username(self)


