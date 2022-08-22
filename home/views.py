from django.shortcuts import render
from products.models import Product
from newsletter.forms import SubscriptionForm
from newsletter.models import Subscription

from newsletter.subscription_confirmation import send_subs_confirm_email

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
        return render(request, 'home/index.html', context)
    else:
        if new_member.is_valid():
            new_member.save()
            new_member = Subscription.objects.get(fname=fname, email=email)
            messages.info(request, 'Subscription complete, check your \
                                inbox and enjoy the 10% off')
            send_subs_confirm_email(new_member)
            form = SubscriptionForm()
            context = {
                'subscription_form': form,
            }
            return render(request, 'home/index.html', context)
        else:
            messages.info(request, 'Something went wrong, \
                                try again later')
            return render(request, 'home/index.html', context)
