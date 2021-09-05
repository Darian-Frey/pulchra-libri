from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


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
        messages.success(request, "Item added to your bag")

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity in range(0, 10):
        bag[item_id] = quantity
        messages.success(request, "Item added to your bag")
    else:
        bag.pop(item_id)
        messages.success(request, "Item removed from you bag")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    bag.pop(item_id)
    messages.success(request, "Item removed from your bag")

    request.session['bag'] = bag
    return HttpResponse(status=200)
