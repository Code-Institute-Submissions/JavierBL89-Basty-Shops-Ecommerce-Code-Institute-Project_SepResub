from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Size, Image, ProductDetail
from .forms import ProductForm, SizeForm, ImageForm, ProductDetailForm
from bag.handle_stock import handle_stock_admin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    product_details = ProductDetail.objects.filter(product_id=product_id).all()
    details_key = None
    details_value = None
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


@login_required
def add_product(request):
    """ Add products to store """

    if not request.user.is_authenticated:
        messages.info(request, 'Request not allowed, only stpore admin.')
        return redirect(reverse('home'))

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
                        return redirect((reverse('product_detail', args=[product.id])))
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
        'product_detail_form': product_detail_form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product from store """

    if not request.user.is_authenticated:
        messages.info(request, 'Request not allowed, only stpore admin.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product_sizes = Size.objects.filter(product_id=product).all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        size_form = SizeForm(request.POST)
        product_details_form = ProductDetailForm(request.POST)

        if form.is_valid():
            if product_details_form.is_valid():
                if product_details_form.is_valid():
                    form.save()
                    product_details_form.save()
                    image_form.save()
                    handle_stock_admin(request, product_id, product_sizes)
                    messages.info(request, 'Product successfuly edited!')
                    return redirect((reverse('product_detail', args=[product.id])))
        else:
            messages.info(request, 'Could not add product. Please check the form is valid.')

    sizes = Size.objects.filter(product_id=product_id).all()
    product_details = ProductDetail.objects.filter(product_id=product_id)
    product_images = get_object_or_404(Image, product_id=product)
    form = ProductForm(instance=product)

    for detail in list(product_details.values()):
        product_detail_data = {
            'heels_mesurement': detail['heels_mesurement'],
            'upper_material': detail['upper_material'],
            'sole': detail['sole'],
            'technology': detail['technology'],
            'lining_material': detail['lining_material'],
            'fastening': detail['fastening'],
        }

    product_detail_form = ProductDetailForm(product_detail_data)
    image_form = ImageForm(instance=product_images)

    template = 'products/edit_product.html'
    messages.info(request, f'You are about to edit {product.title}')
    context = {
        'product_form': form,
        'product_sizes': sizes,
        'product_detail_form': product_detail_form,
        'image_form': image_form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete product fro store """

    if not request.user.is_authenticated:
        messages.info(request, 'Request not allowed, only stpore admin.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.info(request, f'Product {product.title}, was deleted')
    return redirect(reverse('products'))