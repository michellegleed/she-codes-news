from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, DeleteView
from django.views import generic
from django.shortcuts import get_object_or_404
# from django.contrib.auth import get_user_model

from news.models import NewsStory
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'users/createAccount.html'

class EditProfileView(generic.DetailView):
    template_name = 'users/edit-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_stories'] = NewsStory.objects.filter(author=self.request.user.id).order_by('-pub_date')
        return context

    def get_object(self):
        return get_object_or_404(CustomUser, pk=self.request.user.id)
        # return get_user_model()

class UserProfileView(generic.DetailView):
    template_name = 'users/profile.html'
    model = CustomUser
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_stories'] = NewsStory.objects.filter(author=self.object).order_by('-pub_date')
        return context
        # While this detail view is executing, self.object will contain the object that the view is operating upon.

class DeleteAccountView(DeleteView):
    template_name = 'users/deleteAccount.html'
    model = CustomUser
    success_url = reverse_lazy('news:index')

    def get_object(self):
        return get_object_or_404(CustomUser, pk=self.request.user.id)