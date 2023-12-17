from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content' ,'image']
        widgets = {
			'pub_date': forms.DateTimeInput(
				format= { '%m/%d/%Y %H:%M' },
				attrs={
					'class': 'form-control',
					'placeholder': 'Select a date',
					'type': 'datetime-local'
				}
			)
		}