from django.shortcuts import render
from products.models import Product
from newsletter.forms import SubscriptionForm


def index(request):
    """ View to return index page"""

    subscription_form = SubscriptionForm()
    products = Product.objects.all()

    context = {
        'products': products,
        'subscription_form': subscription_form
    }
    return render(request, 'home/index.html', context)
