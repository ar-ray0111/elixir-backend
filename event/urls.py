from django.urls import path
from . import views


urlpatterns = [
    path('', views.event_form, name='event_form'),
    path('events_api/', views.api_call, name='events')
]
