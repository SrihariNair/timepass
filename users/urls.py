from django.urls import path
from . import views
app_name='users'
urlpatterns = [
    # todo Adding ading view address
    path('forgot_password/',views.ForgetFormView, name ='ForgetPassword'),
    path('security_question/<int:pk>',views.SecurityQuestion,name='SecurityQuestion'),
    path('signup/', views.SignUp.as_view(), name='signup'),
  ]