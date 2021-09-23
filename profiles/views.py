from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, WishList
from .forms import UserProfileForm

from checkout.models import Order


def wish_list(request):
    """ Display the users wish list """
    username = request.user.username
    profile = UserProfile.objects.get(user__username=username)
    wish_list = WishList.objects.all().filter(user=profile)
    template = 'profiles/wish_list.html'
    context = {
        'wish_list': wish_list,
    }

    return render(request, template, context)


@login_required
def remove_wish_list(request, product_id):
    """ Delete a book from the users wish list """

    username = request.user.username
    profile = UserProfile.objects.get(user__username=username)
    wish_list = WishList.objects.all().filter(user=profile)
    for books in wish_list:
        if books.product.id == int(product_id):
            print('true')
            books.delete()

    wish_list = WishList.objects.all().filter(user=profile)
    template = 'profiles/wish_list.html'
    context = {
        'wish_list': wish_list,
    }

    return render(request, template, context)


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)