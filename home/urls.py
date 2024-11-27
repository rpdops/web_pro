from django.contrib import admin
from django.urls import path, include
from home import views
from .views import authView, home
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",home ,name='home'),
    path("", views.index, name='home'),
    path("about", views.cart, name='cart'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="authView"),
    #path("logout/", LogoutView.as_view(), name='logout'),
    path("logout/", views.logout, name='logout'),

    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),
    path("remove_from_cart/<int:item_id>/", views.remove_from_cart, name="remove_from_cart")
]
admin.site.site_header = "Saurabh Admin"
admin.site.site_title = "Saurabh Admin Portal"
admin.site.index_title = "Welcome to Saurabh E-commerce"