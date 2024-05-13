from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from wewindecoration import views

urlpatterns = [
   path("", views.index, name="home"),
   path("home", views.index, name="home"),
   path("gallery", views.gallery, name="gallery"),
   path("decoration", views.decoration, name="decoration"),
   path("decoration_detail/<int:decoration_id>/", views.decoration_detail, name="decoration_detail"),

   path("cart", views.cart, name="cart"),
   path('add_to_cart/<int:decoration_id>/', views.add_to_cart, name='add_to_cart'),
   path('remove_from_cart/<int:decoration_id>/', views.remove_from_cart, name='remove_from_cart'),

   path('checkout/', views.checkout, name='checkout'),

    path('order_history', views.order_history, name='order_history'),
    path("order_history_details/<int:order_id>/",views.order_history_details,name="order_history_details"),



]