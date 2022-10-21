from django import forms
from django.forms import ModelForm
from .models import Venue, Event


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # fields = '__all__'
        # Fields will appear in this order:
        fields = ('name', 'address', 'city', 'venue_image', 'website', 'description', 'how_to_get_there')
        # Set Bootstrap classes for inputs:
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'how_to_get_there': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2
            })
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        # fields = '__all__'
        # Fields will appear in this order:
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
        # Alter labels for inputs:
        labels = {
            'event_date': 'Event date (YYYY-MM-DD HH:MM):',
        }
        # Set Bootstrap classes for inputs:
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'event_date': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'venue': forms.Select(attrs={
                'class': 'form-control'
            }),
            'manager': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'attendees': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
        }
