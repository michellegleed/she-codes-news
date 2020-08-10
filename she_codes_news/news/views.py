from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import NewsStory
from .forms import StoryForm

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = ''
    
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        # form.instance.last_modified = None
        return super().form_valid(form)
        
class EditStoryView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = ''
    
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'story'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.modified = True
        return super().form_valid(form)

    def test_func(self):
        story = self.get_object()
        if self.request.user == story.author:
            return True
        return False

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

# class DeleteStoryView(generic.DeleteView):
#     model = NewsStory
 

