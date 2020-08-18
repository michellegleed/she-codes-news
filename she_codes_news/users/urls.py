from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import CreateAccountView, UserProfileView, EditProfileView, DeleteAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name="createAccount"),
    path('profile/<int:pk>', UserProfileView.as_view(), name="profile"),
    path('edit-profile/', EditProfileView.as_view(), name="editProfile"),
    path('delete-account/', DeleteAccountView.as_view(), name="deleteAccount"),

]

# serving static images uploaded by user in DEVELOPMENT only!! This is not suitable for production.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
