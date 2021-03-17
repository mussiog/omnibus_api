from django.db import models
from django.contrib.auth.models import User

class NcoPing(models.Model):
    host = models.CharField(max_length=100)
    delay = models.IntegerField()
    description = models.CharField(max_length=100)
    lastedit = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-lastedit']
