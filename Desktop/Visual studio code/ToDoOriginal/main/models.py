from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    persone = models.TextField(max_length=50)
    phone_number = models.TextField()
    date_of_meeting = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToHabits(models.Model):
    name = models.TextField(max_length=25)
    done_for_today = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    comment = models.TextField(max_length=999)
