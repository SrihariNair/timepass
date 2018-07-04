from django.db import models
from django.utils import timezone


class Userpost(models.Model):
    title = models.CharField(blank=True, max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approval = models.CharField(blank=True, max_length=100)

    def _str_(self):
        return str(self.title)