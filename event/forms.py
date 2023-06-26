from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'poster', 'registration_link', 'time', 'event_summary']
        