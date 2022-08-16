from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Size, Image, ProductDetail, Category
from .forms import ProductForm, SizeForm, ImageForm, ProductDetailForm
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


def add_product(request):
    
    # product_detail_form = None
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        product_detail_form = ProductDetailForm(request.POST)
        size_form = SizeForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if product_form.is_valid():
            if product_detail_form.is_valid():
                if size_form.is_valid():
                    if image_form.is_valid():
                        product_form.save()
                        product_detail_form.save()
                        size_form.save()
                        image_form.save()

                        product = Product.objects.all().last()
                        product_details = ProductDetail.objects.filter(product_id=None).all()
                        product_sizes = Size.objects.filter(product_id=None).all()
                        product_images = Image.objects.filter(product_id=None).all()

                        # Attach the product id to all the product colections sizes
                        product_sizes.update(product_id=product)
                        product_details.update(product_id=product)
                        product_images.update(product_id=product)
                        messages.info(request, 'Product successfuly added!')
                        return redirect((reverse('add_product')))
        else:
            messages.error(request, 'Could not add product. Please check the form is valid.')

    else:
        # this empty forms won't wipe out the form errors
        product_form = ProductForm()
        size_form = SizeForm()
        image_form = ImageForm()
        product_detail_form = ProductDetailForm()

    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
        'size_form': size_form,
        'image_form': image_form,
        'product_detail_form': product_detail_form
    }
    return render(request, template, context)
