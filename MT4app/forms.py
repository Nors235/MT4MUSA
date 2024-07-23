from django import forms
from .models import Service, Review


class ServiceForm(forms.ModelForm):
    """ Service Form"""
    class Meta:
        """ fields for comment form"""
        model = Service
        fields = ('name', 'description', 'price')

