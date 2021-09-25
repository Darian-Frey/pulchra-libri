from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
from profiles.models import WishList, UserProfile

def all_products(request):
    """Renders all products"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(overview__icontains=query) | Q(aurthor__icontains=query) | Q(noteone__icontains=query) | Q(details__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """Shows individual products"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))


@login_required
def wish_list(request, product_id):
    """
    Save book to user wish list
    """
    if request.user.is_authenticated:
        username = request.user.username
        profile = UserProfile.objects.get(user__username=username)
        all_wish_list = WishList.objects.all().filter(user=profile)
        if all_wish_list:
            add_item = True
            for item in all_wish_list:
                if product_id == item.product.id:
                    add_item = False

            if add_item:
                messages.info(request, 'Book added to your wish list')
                saved_item = WishList(user=profile, product_id=product_id, status=True)
                saved_item.save()
                return HttpResponseRedirect(reverse('product_detail', args=(product_id,)))
            else:
                messages.info(request, 'You already have this book saved to your wish list')
                return HttpResponseRedirect(reverse('product_detail', args=(product_id,)))

        else:
            print("No books in wish list, first book added")
            messages.info(request, 'Congratulations, you saved your first book to your wish list')
            saved_item = WishList(user=profile, product_id=product_id, status=True)
            saved_item.save()
            return HttpResponseRedirect(reverse('product_detail', args=(product_id,)))
    else:
        print("User not logged in")
        return HttpResponseRedirect(reverse('product_detail', args=(product_id,)))
