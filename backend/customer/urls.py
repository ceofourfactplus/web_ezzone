from django.urls import path
from . import views

urlpatterns = [
    path('customer', views.CustomerList.as_view()),
    path('customer/<int:pk>', views.CustomerDetail.as_view()),
    path('save-address/<int:pk>', views.SaveAddress.as_view())
]
