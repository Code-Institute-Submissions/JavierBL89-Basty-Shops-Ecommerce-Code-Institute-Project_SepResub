from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
    path('update_details/',
         views.update_details,
         name='update_details'),
#     path('delete_account/<int:user_id>',
#          views.delete_account,
#          name='delete_account'),
]
