from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Todo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_completed = models.CharField(max_length=255, default='Not_completed')
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse('todo_list')




