from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('increment/<item_id>/', views.increment_quantity, name='increment_quantity'),
    path('decrement/<item_id>/', views.decrement_quantity, name='decrement_quantity'),
    path('remove/<item_id>/', views.remove_item, name='remove_item'),
]