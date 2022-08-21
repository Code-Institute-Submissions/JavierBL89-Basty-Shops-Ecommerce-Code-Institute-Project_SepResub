from django.shortcuts import render
from products.models import Product
# Create your views here.


def index(request):
    """ View to return index page"""

    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)
