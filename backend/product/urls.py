from django.urls import path
from product import views

urlpatterns = [
    path('category/', views.ProductCategoryList.as_view()),
    path('category/<int:pk>/', views.ProductCategoryDetail.as_view()),
    path('sale-channel/', views.SalechannelList.as_view()),
    path('sale-channel/<int:pk>/', views.SaleChannelDetail.as_view()),
    path('sale-channel/status/<int:pk>/', views.SaleChannelStatus.as_view()),
    path('topping/', views.ToppingList.as_view()),
    path('topping/<int:pk>/', views.ToppingDetail.as_view()),
    path('topping/status/<int:pk>/', views.ToppingStatus.as_view()),
    path('topping-pos/', views.ToppingPos.as_view()),
    path('type-topping/', views.TypeToppingList.as_view()),
    path('type-topping/<int:pk>/', views.TypeToppingDetail.as_view()),
    path('price-product/', views.PriceProductList.as_view()),
    path('price-product/<int:pk>/', views.PriceProductDetail.as_view()),
    path('table-topping/', views.TableToppingList.as_view()),
    path('table-topping/<int:pk>/', views.TableToppingDetail.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product-pos/<int:pk>/', views.ProductPos.as_view()),
    # path('select-product-by-catgory/<int:id>/',views.SelectProductByCategory.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('product/status/<int:pk>/', views.ProductStatus.as_view()),
    path('price-topping/', views.PriceToppingList.as_view()),
    path('many-price-topping/', views.PriceToppingMany.as_view()),
    path('many-price-product/', views.PriceProductMany.as_view()),
]