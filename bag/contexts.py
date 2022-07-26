from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.conf import settings
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    delivery = 0

    bag = request.session.get('bag', {})
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
    
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product
            })
        print(bag_items)
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE/100)
    
    grand_total = delivery + total
    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'delivery': delivery,
        'total': total,
        'grand_total': grand_total,
    }
    return context