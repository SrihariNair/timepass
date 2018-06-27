from django.urls import path
from . import views
app_name='dashboard'


urlpatterns = [
    path('birthday_list/',views.birthdaylist,name='birthday_list'),
    path('detailview/<int:customuser_id>/', views.detailview, name='detailview'),
    path('home/',views.home,name='home'),
]