from django.contrib import admin
from .models import Subscription

# Register your models here.


@admin.register(Subscription)
class SubscriptionAdminInline(admin.ModelAdmin):
    """
    Class to show newsletter's members fields in admin panel
    """
    fields = ('fname', 'email',)
    list_display = ('fname', 'email',)
