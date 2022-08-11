from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm
# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.info(request, 'There is nothing in the bag')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LBOvCLzFhEXkarg7N0Q42yNteeE2b883G6fG7P5sJpRWPztcqxrogMts2NEZnQCPqCSG39dhvvF8LVQ5rbRS1x900jV78wniI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
