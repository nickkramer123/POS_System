"""
URL configuration for django_start project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"), # connects template function in views to template.html
    path("admin/", admin.site.urls), # not sure what this does yet
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"), # connects add_to_cart function in views to add_to_cart
    path("clear_cart/", views.clear_cart, name="clear_cart"), # connects clear_cart function in views to clear_cart
]
