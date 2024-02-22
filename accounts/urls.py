from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name = 'logout'),
   ## path('login-api/',views.UserAPI.as_view()),
  ##  path('register-api/',views.RegisterUserAPIView.as_view()),
]
