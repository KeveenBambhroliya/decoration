from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from adminpanel import views

urlpatterns = [

    path("admin_home", views.admin_home, name="admin_home"),
    path("admin_login", views.admin_login, name="admin_login"),
    path("admin_logout", views.admin_logout, name="admin_logout"),
    path("admin_logout", views.admin_logout, name="admin_logout"),

    # gallery_management
    path("admin_gallery_management",views.admin_gallery_management,name="admin_gallery_management"),
    path("add_gallery",views.add_gallery,name="add_gallery"),
    path('edit_gallery/<int:item_id>/',views.edit_gallery, name='edit_gallery'),
    path('delete_gallery/<int:item_id>/',views.delete_gallery, name='delete_gallery'),

    # gallery_management
    path("admin_decoration_management",views.admin_decoration_management,name="admin_decoration_management"),
    path("add_decoration",views.add_decoration,name="add_decoration"),
    path('edit_decoration/<int:item_id>/',views.edit_decoration, name='edit_decoration'),
    path('delete_decoration/<int:item_id>/',views.delete_decoration, name='delete_decoration'),

    # category_management
    path("admin_category_management",views.admin_category_management,name="admin_category_management"),
    path('edit_category/<int:category_id>/',views.edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/',views.delete_category, name='delete_category'),

    # order_manage
    path("admin_order_management",views.admin_order_management,name="admin_order_management"),
    path('order_details/<int:order_id>/', views.order_details, name='order_details'),

        # contactus
    path("contactus",views.contactus,name="contactus"),
    path("contactusdetails/<int:contact_id>/",views.contactusdetails,name="contactusdetails"),

# ------------------------------------------------reset database-----------------------------------------
    path("reset_tables",views.reset_tables,name="reset_tables"),
    path('reset_database', views.reset_database, name='reset_database'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)