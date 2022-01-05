from django.urls import path
from product import views

urlpatterns = [
    path('category/', views.ChangeList.as_view()),
    path('category/<int:pk>', views.ProductCategoryDetail.as_view()),
    path('topping/', views.ToppingList.as_view()),
    path('topping-by-type/<int:type>', views.ToppingByType.as_view()),
    path('product-by-type/<int:type>', views.ProductByType.as_view()),
    path('category-by-type/<int:type>', views.CategoryByType.as_view()),
    path('topping/category/', views.ToppingCategoryList.as_view()),
    path('topping/category/<int:pk>', views.ToppingCategoryDetail.as_view()),
    path('category/status/<int:pk>/', views.ProductCategoryStatus.as_view()),
    path('category/get-amount-product/<int:category_id>', views.AmountPorduct.as_view()),
    path('category/get-amount-topping/<int:category_id>', views.AmountTopping.as_view()),
    path('sale-channel/', views.SalechannelList.as_view()),
    path('sale-channel/create/', views.CreateSaleChannel.as_view()),
    path('sale-channel/ezzone', views.SaleChannelEzzone.as_view()),
    path('sale-channel/<int:pk>/', views.SaleChannelDetail.as_view()),
    path('sale-channel/status/<int:pk>/', views.SaleChannelStatus.as_view()),
    path('price-product/', views.PriceProductList.as_view()),
    path('price-product/<int:pk>/', views.PriceProductDetail.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product-by-type-and-search/<int:type>/<str:search>/', views.ProductByTypeAndSearch.as_view()),
    path('topping-by-search/<str:search>/', views.ToppingBySearch.as_view()),
    path('product/category/<int:category_id>', views.ProductByCategory.as_view()),
    path('product-pos/<int:pk>/', views.ProductPos.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('product/status/<int:pk>/', views.ProductStatus.as_view()),
    path('many-price-product/', views.PriceProductMany.as_view()),
    path('check-category-topping/<str:category_name>', views.CheckCategoryTopping.as_view()),
    path('sale-channel-update-img/<int:pk>/',views.UpdateImageSaleChannel.as_view()),
    path('delete-sale-channel-by-list/',views.DeleteSaleChannel.as_view())
]
