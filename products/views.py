from django.shortcuts import render, get_object_or_404
from .models import Product, Size, Image, ProductDetail
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
    images_list = Image.objects.filter(product_id=product_id).all()
    product_details= ProductDetail.objects.filter(product_id=product_id).all()
    
    # loop through images_list dict object
    for image in images_list.values():
        images_list = list(image.values())
        images_list = images_list[2:]
    
    # loop through product details dict object
    for detail in product_details.values():
        # product_details = list(detail)
        details_key = list(detail)[2:]
        details_value = list(detail.values())[2:]
        # print(product_details)
    context = {
        'product': product,
        'size_list': size_list,
        'images_list': images_list,
        'details_key': details_key,
        'details_value': details_value
    }
    return render(request, 'products/product_detail.html', context)
