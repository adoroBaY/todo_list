from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, default='')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title