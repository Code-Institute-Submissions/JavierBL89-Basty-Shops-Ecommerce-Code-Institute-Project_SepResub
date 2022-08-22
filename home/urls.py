from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('faqs/', views.faqs, name='faqs'),
]
