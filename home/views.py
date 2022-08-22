from django.shortcuts import render
from products.models import Product
from newsletter.forms import SubscriptionForm
from newsletter.models import Subscription

from django.contrib import messages
from django.views.decorators.http import require_POST


def index(request):
    """ View to return index page"""

    subscription_form = SubscriptionForm()
    products = Product.objects.all()

    context = {
        'products': products,
        'subscription_form': subscription_form
    }
    return render(request, 'home/index.html', context)


@require_POST
def subscribe(request):

    if 'redirect_url' in request.POST:
        redirect_url = request.POST['redirect_url']
        print(redirect_url)

        if redirect_url == '/':
            redirect_url = 'home/index.html'
        else:
            redirect_url = 'products/product_detail.html'

    if 'fname' in request.POST:
        fname = request.POST['fname']

    if 'email' in request.POST:
        email = request.POST['email']

    check = Subscription.objects.filter(fname=fname,
                                        email=email).all()

    new_member = SubscriptionForm(request.POST)

    if check:
        messages.info(request, 'Member with same data was \
                            found in our newsletter')
        context = {
            'subscription_form': new_member,
        }
        return render(request, f'{redirect_url}', context)
    else:
        form = SubscriptionForm()
        context = {
            'subscription_form': form,
        }

        if new_member.is_valid():
            new_member.save()
            messages.info(request, 'Subscription complete, check your \
                                inbox and enjoy the 10% off')
            return render(request, f'{redirect_url}', context)
        else:
            messages.info(request, 'Something went wrong, \
                                try again later')
            return render(request, f'{redirect_url}', context)
