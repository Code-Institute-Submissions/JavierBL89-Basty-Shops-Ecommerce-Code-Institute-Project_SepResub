from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('faqs/', views.faqs, name='faqs'),
    path('terms&conditions/', views.terms_conditions, name='terms_conditions'),
    path('refounds&returns/', views.refounds_returns, name='refounds_returns'),
    path('contact/', views.contact, name='contact'),
]
