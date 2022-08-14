from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

# Create your views here.


def profile(request):
    """Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile info successfully updated')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    for order in orders:
        print(order,'puttttt')

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)
