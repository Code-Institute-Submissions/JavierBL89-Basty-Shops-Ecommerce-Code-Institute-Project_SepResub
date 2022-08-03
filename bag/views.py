from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product
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

    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
        print('this is the size', size)

    bag = request.session.get('bag', {})

    print(f"bag is {bag}")
    print(item_id, 'item id')

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['item_size'].keys():
                bag[item_id]['item_size'][size] += quantity
            else:
                bag[item_id]['item_size'][size] = quantity
        else:
            bag[item_id] = {'item_size': {size: quantity}}
    else:
        # send error 500 message
        pass

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    # size = None
    # if 'size' in request.POST:
    #     size = request.POST['size']
    bag = request.session.get('bad', {})
    # if size:
    if quantity > 0:
        bag[item_id]['quantity'] += quantity
    else:
        del bag[item_id]['quantity']
        if not bag[item_id]['quantity']:
            bag.pop(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_item(request, item_id):
    try:
        # size = None 
        # if 'size' in request.POST:
        #     size =  request.POST.get['size']
        bag = request.session.get('bag', {})
        # if size:
            # del bag[item_id]['item_size']['size']
            # if not bag[item_id]['item_size']['size']
            #     bag.pop(item_id)
        # else:
        bag.pop(item_id)
        request.session['bag'] = bag
        print(request.session['bag'], 'bag session')
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)