from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.RegisterUserAPIView.as_view()),
  path('user-info/', views.UserInfo.as_view()),
  path('verify/', views.activate.as_view()),
  path('conf-pas/', views.ConfirmPass.as_view()),
  path('login/', views.IsActive.as_view()),
  path('read-all/', views.UserList.as_view())
]