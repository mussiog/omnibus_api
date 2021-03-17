from django.db import models
from django.contrib.auth.models import User

Class Nco_ping(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    delay = models.IntegerField()
    description = models.CharField(max_lenth=100)
    lastedit = models.DateTimeField(auto_now_add=True)

    Class Meta:
        ordering = ['-lastedit']

