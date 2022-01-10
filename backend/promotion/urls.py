from django.urls import path
from . import views

urlpatterns = [
    path('point/', views.PointPromotionAPI().as_view()),
    path('point/<int:pk>', views.Point().as_view()),
    path('voucher/', views.VoucherAPI().as_view()),
    path('voucher/<int:pk>', views.VoucherGET().as_view()),
    path('package/', views.PackageAPI().as_view()),
    # path('package/<int:pk>', views.PackageGET().as_view()),
    path('package-item/', views.PackageItemAPI().as_view()),
]