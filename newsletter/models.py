from django.db import models

# Create your models here.


class Subscription(models.Model):
    """
    Create member to newsletter
    """
    fname = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
