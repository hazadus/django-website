from django import forms
from django.forms import ModelForm
from .models import Venue


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # fields = '__all__'
        # Fields will appear in this order:
        fields = ('name', 'address', 'city', 'website', 'description', 'how_to_get_there')
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
