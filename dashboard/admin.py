from django.contrib import admin
from .models import Post, LeaveApplication, Announcement, Document

# Register your models here.

admin.site.register(Post)

admin.site.register(LeaveApplication)

admin.site.register(Announcement)

admin.site.register(Document)