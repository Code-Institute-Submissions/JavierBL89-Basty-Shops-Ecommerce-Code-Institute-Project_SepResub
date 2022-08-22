from django.shortcuts import render, redirect, reverse

from .forms import SubscriptionForm
from .models import Subscription

from django.contrib import messages
from django.views.decorators.http import require_POST

# Create your views here.


def subscribe(request):

    if 'redirect_url' in request.POST:
        redirect_url = request.POST['redirect_url']
    print(redirect_url)

    if 'fname' in request.POST:
        fname = request.POST['fname']

    if 'email' in request.POST:
        email = request.POST['email']

    check = Subscription.objects.filter(fname=fname, email=email).all()

    if check:
        messages.info(request, 'Member with same data was found in our newsletter')
        return render(request, "home/index.html")

    else:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Subscription complete, check your inbox and enjoy the 10% off')
            return render(request, "home/index.html")
        else:
            form = SubscriptionForm()
        # except Exception as e:
            messages.info(request, 'Something went wrong, try again later')
            # return HttpResponse(content=e, status=500)
