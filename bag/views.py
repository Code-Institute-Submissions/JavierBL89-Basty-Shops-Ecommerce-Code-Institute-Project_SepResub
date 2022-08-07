from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product, Size
from .handle_stock import handle_stock, decrement_stock, increment_stock, update_stock
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the quantity of the specified product to the shopping bag """
    
    product = Product.objects.get(pk=item_id)            
    quantity = 1
    size = None
    redirect_url = request.POST.get('redirect_url')

    if 'size_id' in request.POST:
        item_size_id = request.POST.get('size_id')

    if 'product_size' in request.POST:
        size = request.POST.get('product_size')

    bag = request.session.get('bag', {})

    print(f"bag is {bag}")
    print(item_id, 'item id')

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['item_size'].keys():
                bag[item_id]['item_size'][size] += quantity
                handle_stock(item_size_id)
            else:
                bag[item_id]['item_size'][size] = quantity
                handle_stock(item_size_id)
        else:
            bag[item_id] = {'item_size': {size: quantity}}
    else:
        # send error 500 message
        pass

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_item(request, item_id):

    try:
        product_sizes_list = Size.objects.filter(product_id=item_id).all()
        size = None

        if 'product_size' in request.POST:
            size = request.POST['product_size']

        if 'quantity' in request.POST:
            quantity = request.POST.get('quantity')
            print('yyyyyyyy')
        
        for item_size in product_sizes_list.values():
            if size in item_size['size']:
                item_size_id = item_size['id']
                print('yyyeess', item_size['id'])
                update_stock(item_size_id, quantity)

        bag = request.session.get('bag', {})
        bag.pop(item_id)
        
        request.session['bag'] = bag
        print(request.session['bag'], 'bag session')
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


def increment_quantity(request, item_id):

    product_sizes_list = Size.objects.filter(product_id=item_id).all()
    quantity = 1
    size = None

    if 'product_size' in request.POST:
        size = request.POST.get('product_size')

    for item_size in product_sizes_list.values():
        if size in item_size['size']:
            item_size_id = item_size['id']
            print('yyyeess', item_size['id'])
            decrement_stock(item_size_id)

    bag = request.session.get('bag', {})
    print(bag)
    if size:
        if quantity > 0:
            bag[item_id]['item_size'][size] += quantity
        else:
            del bag[item_id]['item_size']['quantity']
            if not bag[item_id]['item_size']['quantity']:
                bag.pop(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def decrement_quantity(request, item_id):

    product_sizes_list = Size.objects.filter(product_id=item_id).all()
    quantity = 1
    size = None

    if 'product_size' in request.POST:
        size = request.POST.get('product_size')

    for item_size in product_sizes_list.values():
        if size in item_size['size']:
            item_size_id = item_size['id']
            print('yyyeess', item_size['id'])
            increment_stock(item_size_id)

    bag = request.session.get('bag', {})
    print(bag)
    if size:
        if quantity > 0:
            bag[item_id]['item_size'][size] -= quantity
        else:
            del bag[item_id]['item_size']['quantity']
            if not bag[item_id]['item_size']['quantity']:
                bag.pop(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


