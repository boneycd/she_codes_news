from django.urls import path
from .views import CreateAccountView , ProfilePageView

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/<int:pk>', ProfilePageView.as_view(), name='profilePage'),
]