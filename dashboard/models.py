from django.db import models
from django.utils import timezone
from users.models import CustomUser



class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title