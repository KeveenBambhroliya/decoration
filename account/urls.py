from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from account import views

urlpatterns = [

    path("login", views.login, name="login"),
    path("registration", views.registration, name="registration"),
    path("logout", views.logout, name="logout"),
    path("user_profile", views.user_profile, name="user_profile"),
    path("edit_user_profile",views.edit_user_profile,name="edit_user_profile"),
    path("user_contactus", views.user_contactus, name="user_contactus"),
    path("user_aboutus", views.user_aboutus, name="user_aboutus"),

    
    # only for test
    path("test", views.test, name="test"),



]