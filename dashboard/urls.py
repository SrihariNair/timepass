from django.urls import path
from . import views
app_name='dashboard'


urlpatterns = [
    path('birthday_list/',views.birthdaylist,name='birthday_list'),
    path('detailview/', views.detailview, name='detailview'),
    path('home/',views.home,name='home'),
    path('new_post/',views.new_posts,name='new_posts'),
    path('posts/',views.PostList.as_view(),name='posts'),
    path('posts_details/<int:pk>',views.postdetail,name='post_detail'),
    path('approval/', views.approval, name='approval'),
    path('applyleave/', views.applyleave, name='applyleave'),
]
