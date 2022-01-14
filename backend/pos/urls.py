from django.urls import path
from pos import views

urlpatterns = [
    path('payment/', views.PaymentList.as_view()),
    path('order/', views.OrderList.as_view()),
    path('order/payment-channel/<int:order_id>/<int:payment_id>', views.SelectPaymentOrder.as_view()),
    path('order/accept/food/<int:pk>', views.AcceptFoodOrder.as_view()),
    path('order/finish/food-item/<int:pk>', views.FinishFoodOrderItem.as_view()),
    path('order/finish/food-order/<int:pk>', views.FinishFoodOrder.as_view()),
    path('order/today/on-going/food', views.FoodOrderOnGoing.as_view()),
    path('order/accept/drink/<int:pk>', views.AcceptDrinkOrder.as_view()),
    path('order/finish/drink-item/<int:pk>', views.FinishDrinkOrderItem.as_view()),
    path('order/finish/drink-order/<int:pk>', views.FinishDrinkOrder.as_view()),
    path('order/today/on-going/drink', views.DrinkOrderOnGoing.as_view()),
    path('order/today/', views.TodayOrderList.as_view()),
    path('order/today/completed', views.TodayOrderCompleted.as_view()),
    path('order/today/unpaid', views.TodayOrderUnpaid.as_view()),
    path('order/today/void', views.TodayOrderVoid.as_view()),
    path('order/today/on-going', views.TodayOrderOnGoing.as_view()),
    path('all-order/', views.AllOrder.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
    path('order-item/', views.OrderItemList.as_view()),
    path('order-item/<int:id>/', views.OrderItemDetail.as_view()),
    path('order-item-topping/', views.OrderItemToppingList.as_view()),
    path('order-item-topping/<int:id>/', views.OrderItemToppingDetail.as_view()),
]
 