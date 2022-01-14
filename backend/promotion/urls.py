from django.urls import path
from . import views

urlpatterns = [
    path('point/', views.PointPromotionAPI().as_view()),
    path('point/<int:pk>', views.Point().as_view()),
    path('voucher/', views.VoucherAPI().as_view()),
    path('voucher/<int:pk>', views.VoucherGET().as_view()),
    path('package/', views.PackageAPI().as_view()),
    path('package/<int:pk>', views.PackageGET().as_view()),
    path('package-item/', views.PackageItemAPI().as_view()),
    path('package-item/<int:pk>', views.PackageItemGET().as_view()),
    path('package-item-topping/', views.ItemToppingToppingAPI().as_view()),
    path('package-item-topping/<int:pk>', views.ItemToppingGET().as_view()),
    path('reward/', views.RewardAPI().as_view()),
    path('reward/<int:pk>', views.RewardGET().as_view()),
    path('condition-reward/', views.ConditionRewardAPI().as_view()),
    path('condition-reward/<int:pk>', views.ConditionRewardGET().as_view()),
]