from django import forms
from django.forms import fields
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','event_date','venue','description','image']