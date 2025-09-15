from django.db import models
from datetime import datetime, timedelta

# Create your models here.
#ORM 
class Tasks(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    reminder_time  = models.DateTimeField(default=datetime.now() + timedelta(minutes=5)) 
    image = models.FileField(upload_to="tasks_images/", blank=True)
    priority = models.IntegerField(null=True)
    priorities = [
        ("low", "LOW"),
        ("high", "HIGH"),
        ("medium", "MEDIUM")
    ]
    new_priority = models.CharField(choices=priorities, blank=True)
    status = models.CharField(max_length=20, default="not_done")
    statuss = [
        ("completed", "COMPLETED"),
        ("pending", "PENDING")    
        ]
    
    new_status = models.CharField(choices=statuss, blank=True)
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    username = models.CharField(max_length=23, null=False)