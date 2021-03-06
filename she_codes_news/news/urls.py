from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/edit', views.EditStoryView.as_view(), name='editStory'),
    path('<int:pk>/delete', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('categories/', views.CategoryListView.as_view(), name='categoryList'),  
    path('categories/<str:slug>', views.CategoryStoriesView.as_view(), name='categoryStories'),
    path('followed-topics', views.FollowedTopicsIndexView.as_view(), name='followedTopics'),
]
