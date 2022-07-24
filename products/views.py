from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Size, Image, ProductDetail, Category
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def all_products(request):
    """ A view to return all products
    including sorting and searching queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = Product.annotate(lower_title=Lower('title'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category']
            if not categories:
                messages.error(request, "No category found")
                return redirect(reverse, ('products'))
            category = Q(title__icontains=categories) 
            products = products.filter(category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse, ('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(title__icontains=query)
            products = products.filter(queries)
           
        current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting
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
