from django.db import models

class ToDo(models.Model):
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
