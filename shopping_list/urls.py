from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='Home'),
    path('', views.default_page, name='Default' ),
    path('base/', views.base_page,name='Base'),
]