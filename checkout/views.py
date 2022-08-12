from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from bag.contexts import bag_contents

from django.conf import settings

from .forms import OrderForm

from .models import Order, OrderLineItem
from products.models import Product

# stripe
import stripe


# Create your views here.

def checkout(request):
    """
    View that renders the checkout page 
    and handles checkout  payment proccess
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'post_code': request.POST['post_code'],
            'town_or_city': request.POST['town_or_city'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(pk=item_id)
                    for size, quantity in item_data['item_size'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=size
                        )
                        order_line_item.save()
                except product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't"
                        "found in our database."
                        "Call us for assistance!"
                    ))
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Doble check the information in the form.'))
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.info(request, 'There is nothing in the bag')
            return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(amount=stripe_total,
                                         currency=settings.STRIPE_CURRENCY)

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public ley is missing. \
            Did you forget to set it in your enviroment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkout
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)