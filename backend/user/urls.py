from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.RegisterUserAPIView.as_view()),
  path('user-info/', views.UserInfo.as_view()),
  path('verify/', views.activate.as_view()),
  path('conf-pas/', views.ConfirmPass.as_view()),
  path('is-active/', views.IsActive.as_view()),
]