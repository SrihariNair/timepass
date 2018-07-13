from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

from users.models import CustomUser



class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return str(self.title)+"-"+str(self.author)



class LeaveApplication(models.Model):
    subject = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    APPROVE_CHOICE = (
        ('APPROVED', 'APPROVED'),
        ('NOT APPROVED', 'NOT APPROVED'),
    )
    approval = models.CharField(blank=True, max_length=100, choices=APPROVE_CHOICE)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def _str_(self):
        return self.subject



class Announcement(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title
