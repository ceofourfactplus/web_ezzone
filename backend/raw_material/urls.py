from django.urls import path
from . import views

urlpatterns = [
    path('raw-material/', views.RawMaterialListAPIView().as_view()),
    path('category/', views.CategoryAPIView.as_view()),
    path('category/<int:pk>', views.RMCategoryDetailAPIView.as_view()),
#     path('supplier/', views.SupplierListAPIView.as_view()),
    path('unit', views.UnitListAPIView.as_view()),
#     path('stock/', views.StockListAPIView.as_view()),
#     path('stock-trance/', views.StockTranceListAPIView.as_view()),
#     path('payer/', views.PayerListAPIView.as_view()),
#     path('invoice/', views.InvoiceListAPIView.as_view()),
#     path('invoice-detail/', views.InvoiceDetailListAPIView.as_view()),

#     path('supplier/<int:pk>/', views.SupplierDetailAPIView.as_view()),
#     path('unit/<int:pk>/', views.UnitDetailAPIView.as_view()),
#     path('stock/<int:pk>/', views.StockDetailAPIView.as_view()),
#     path('stock-trance/<int:pk>/', views.StockTranceDetailAPIView.as_view()),
#     path('payer/<int:pk>/', views.PayerDetailAPIView.as_view()),
#     path('invoice/<int:pk>/', views.InvoiceDetailAPIView.as_view()),
#     path('invoice-detail/<int:pk>/', views.InvoiceDetailDetailAPIView.as_view()),
#     path('delete-all', views.DeleteAllDataAPIView.as_view()),
#     path('category-fil/<str:q>', views.CategoryFilter.as_view()),
#     path('unit-fil/<str:q>', views.UnitFil.as_view()),
#     path('frequency/stock/<int:stock_id>', views.StockFrequency.as_view()),
#     path('to-buy/',views.ToBuyStock.as_view()),
]
