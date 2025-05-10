from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Task(models.Model):

    class StateChoises(models.TextChoices):
        UNDONE = 'Undone',
        DONE = 'Done',
        IN_PROGRESS = 'In progress',

    title = models.CharField(max_length=150)
    text = models.TextField()
    state = models.CharField(choices=StateChoises.choices, max_length=20, default=StateChoises.UNDONE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def get_absolute_url(self):
        return reverse('todoapp:detail_task', args=(self.id,))
    
    def __str__(self):
        return f'{self.title} of {self.user.username}'