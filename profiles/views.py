from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserProfileForm, UpdateUserForm

from checkout.models import Order

# Create your views here.


def profile(request):
    """Display the user's profile. """

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
    
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile info successfully updated')

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'form': form,
        'profile': user_profile,
    }

    return render(request, template, context)


def order_history(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)


def update_details(request):

    if request.method == 'POST':
        update_form = UpdateUserForm(request.POST, instance=request.user)
        user = get_object_or_404(User, pk=request.user.id)
        
        if update_form.is_valid():
            update_form.save()
            # update user object details
            user.first_name = request.POST['name']
            user.last_name = request.POST['surname']
            user.username = request.POST['username']
            user.email = request.POST['email']
            user.save()
            messages.info(request, 'Profile details successfully updated')
            return redirect(reverse('profile'))

    if request.user.is_authenticated:
        try:
            # profile = UserProfile.objects.get(user=request.user)
            details_form = UpdateUserForm(initial={
                    'name': request.user.first_name,
                    'surname': request.user.last_name,
                    'username': request.user.username,
                    'email': request.user.email,
                })
        except UserProfile.DoesNotExist:
            details_form = UpdateUserForm()
    else:
        details_form = UpdateUserForm()

    template = 'profiles/update_details.html'
    context = {
        'update_form': details_form,
    }

    return render(request, template, context)
