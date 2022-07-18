from django.shortcuts import render, get_object_or_404
from .models import Product, Size
# Create your views here.


def all_products(request):
    """ A view to return all products
    including sorting and searching queries """

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to individual product details """

    product = get_object_or_404(Product, pk=product_id)
    size_list = Size.objects.filter(product_id=product_id).all()
    context = {
        'product': product,
        'size_list': size_list
    }
    return render(request, 'products/product_detail.html', context)
