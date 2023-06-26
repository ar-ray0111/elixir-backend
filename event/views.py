from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from .models import Event
from .forms import EventForm
import json
# Create your views here.

def event_form(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('api_call')
        
    else:
        form = EventForm()
        
    return render(request, 'FormTemplate.html', {'form': form})


def api_call(request):
    events = Event.objects.all()
    event_list = {
        "events": [
            {
                "event_name": event.event_name,
                "poster": event.poster.url if event.poster else None,
                "registration_link": event.registration_link,
                "time": event.time.strftime("%Y-%m-%d") if event.time else None,
                "event_summary": event.event_summary,
            }for event in events
        ] 
    }

    json_data = json.dumps(event_list, indent=4)
    return HttpResponse(json_data, content_type="application/json")
