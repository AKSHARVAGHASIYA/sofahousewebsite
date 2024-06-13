from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name="index"),
    path('index/',views.index, name='index'),
    path('register/',views.register, name='register'),
    path('logIn/', views.logIn, name='logIn'),
    path('logOut/', views.logOut, name='logOut'),
    # path('activate/<uidb64>/<token>',views.activate, name='activate'),


    path('shop/', views.product_list, name='product_list'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path("product_list/", views.product_list, name='product_list'),
    path('update/<str:id>', views.update, name='update'),
    path('add_cart/<str:id>', views.add_cart, name="add_cart"),
    path('cart/', views.cart, name="cart"),
    path('change_qty/<str:id>', views.change_qty, name='update'),
    path('deleteproduct/<str:id>', views.deleteproduct, name='deleteproduct'),
    path('read_cat/<str:id>', views.read_cat, name="read_cat"),


    # path('',views.index, name = 'index'),
    path('index/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    # path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    # path('shop/', views.shop, name='shop'),
    path('thankyou/', views.thankyou, name='thankyou'),

]

