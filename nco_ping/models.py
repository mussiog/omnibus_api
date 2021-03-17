from django.db import models
from django.contrib.auth.models import User

class NcoPing(models.Model):
    host = models.CharField(max_lenth=100)
    delay = models.IntegerField()
    description = models.CharField(max_lenth=100)
    lastedit = models.DateTimeField(auto_now_add=True)

    Class Meta:
        ordering = ['-lastedit']
