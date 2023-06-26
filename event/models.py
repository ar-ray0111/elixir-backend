from django.db import models

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=20)
    poster = models.ImageField()
    registration_link = models.URLField(max_length=100)
    time = models.DateField()
    event_summary = models.TextField()
