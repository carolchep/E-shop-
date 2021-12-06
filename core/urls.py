from django.urls import path
from .views import (products,checkout,HomeView,ItemDetailView,add_to_cart)

app_name='core'
urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('checkout/', checkout,name='checkout'),
    path('products/<slug>/', ItemDetailView.as_view(),name='products'),
    path('add-to-cart/<slug>/', add_to_cart,name='add-to-cart')
  
]