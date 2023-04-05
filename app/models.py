from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=200, blank=False, default='')
    description = models.TextField(max_length=1500, blank=False, default='')
    isDone = models.BooleanField(default=False)

    def __str__(self):
        return self.name