from django.urls import path
from . import views
app_name='users'
urlpatterns = [

    path('forgot_password/',views.ForgetFormView, name ='ForgetPassword'),
    path('security_question/<int:pk>',views.SecurityQuestion,name='SecurityQuestion'),
    path('new_password/<int:pk>',views.NewPass,name='NewPass'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('detailupdate/<int:pk>/', views.DetailUpdateForm.as_view(), name='update'),
    path('detailsview/<int:pk>/', views.DetailViewForm.as_view(), name='detailview'),
    path('documents/<int:pk>/', views.DocumentView.as_view(), name='documents'),
    path('documentsupload/<int:pk>/', views.DocumentUpload.as_view(), name='documentsupload'),

  ]


