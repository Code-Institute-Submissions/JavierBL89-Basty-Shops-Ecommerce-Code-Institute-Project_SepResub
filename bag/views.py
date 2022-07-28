from django.shortcuts import render, redirect
from products.models import Product
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the quantity of the specified product to the shopping bag """
    
    product = Product.objects.get(pk=item_id)
    print(product)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    print(f"bag is {bag}")
    print(item_id, 'item id')

    size = request.POST.get('size')
    print('this is the size', request.POST.get('size'), )

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        print('Item already exists in bag')
    else:
        bag[item_id] = quantity
        print('Item did not exist in bag yet')

    request.session['bag'] = bag
    print(request.session['bag'], 'shopping bag')
    return redirect(redirect_url)
