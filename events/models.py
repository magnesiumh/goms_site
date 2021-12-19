# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    Event_Name = models.CharField(max_length=60)
    Venue = models.CharField(max_length=200,
                             blank=True)

    Date_of_event = models.DateTimeField()

    Event_details = models.TextField()

    update_date = models.DateField(blank=True, null=True)

    username = models.ForeignKey(User, blank=True,
                                 null=True, on_delete=models.CASCADE)


def __str__(self):
    return str(self.id)
