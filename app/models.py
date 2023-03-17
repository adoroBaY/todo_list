from django.db import models


class ToDo(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    isDone = models.BooleanField(default=False)
def __str__(self):
        return self.Title