from django.shortcuts import render, redirect
from products.models import Product
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the quantity of the specified product to the shopping bag """

    # product = Product.objects.get(pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    size = None
    bag = request.session.get('bag', {})

    if 'size' in request.POST:
        size = request.POST.get('size')
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['size']:
                bag[item_id]['size'][size] += quantity
                print(bag[item_id], 'Item already exists in bag')
        else:
            bag[item_id] = {'size': {size: quantity}}

            print(bag[item_id], 'Item did not exist in bag yet')

    request.session['bag'] = bag
    print(request.session['bag'], 'shopping bag')
    return redirect(redirect_url)
