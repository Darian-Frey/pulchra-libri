from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

# Renders shopping bag #

def view_bag(request):
    return render(request, 'bag/bag.html')

#Add specified quantity of product to bag #


def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, "Successfully added to your bag")

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
