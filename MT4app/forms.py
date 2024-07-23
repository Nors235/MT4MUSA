from django import forms
from .models import Service, Review


class ServiceForm(forms.ModelForm):
    """ Service Form"""
    class Meta:
        """ fields for comment form"""
        model = Service
        fields = ('name', 'description', 'price')


class ReviewForm(forms.ModelForm):
    """ Review Form"""
    class Meta:
        """ fields for comment form"""
        model = Review
        fields = ('name', 'description', 'price')