from django.urls import path
from .views import CreateAccountView, UserProfileView, EditProfileView, DeleteAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name="createAccount"),
    path('profile/<int:pk>', UserProfileView.as_view(), name="profile"),
    path('edit-profile/', EditProfileView.as_view(), name="editProfile"),
    path('delete-account/', DeleteAccountView.as_view(), name="deleteAccount")
]