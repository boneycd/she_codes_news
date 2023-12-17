from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views import generic
from news.models import NewsStory

from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
    story = NewsStory

class ProfilePageView(DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'author'