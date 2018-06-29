
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
]