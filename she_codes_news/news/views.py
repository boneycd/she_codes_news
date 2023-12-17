from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.shortcuts import get_object_or_404




class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm 
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# modification 
# class EditStoryView(generic.CreateView):
#     form_class = StoryForm 
#     model = NewsStory
#     context_object_name = 'storyform'
#     template_name = 'news/editStory.html'
#     success_url = reverse_lazy('news:index')

   

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')


class AuthorStoriesView(generic.ListView):
    model = NewsStory
    template_name = 'news/authorStories.html'
    context_object_name = "author_stories"

    def get_queryset(self):
        return NewsStory.objects.filter(author = self.kwargs['pk'])
        
        
    

# # Add story
# class AddStoryView(generic.CreateView):
#     form_class = StoryForm
#     context_object_name = 'storyForm'
#     template_name = 'news/createStory.html'
#     success_url = reverse_lazy('news:index')
    
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         # this is the user that is currently logged in
#         return super().form_valid(form)





