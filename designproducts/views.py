from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User

from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    designproducts = Product.objects.all()
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
                designproducts = designproducts.annotate(lower_name=Lower('name'))  # noqa
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            designproducts = designproducts.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            designproducts = designproducts.filter(category__name__in=categories)  # noqa
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")  # noqa
                return redirect(reverse('designproducts'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
            designproducts = designproducts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'designproducts': designproducts,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'designproducts/designproducts.html', context)


def product_detail(request, designproduct_id):
    """ A view to show individual product details """

    designproduct = get_object_or_404(Product, pk=designproduct_id)
    user = request.user
    liked = user in designproduct.likes.all() if user.is_authenticated else False

    context = {
        'designproduct': designproduct,
        'liked': liked,
    }

    return render(request, 'designproducts/product_detail.html', context)


@login_required
def add_designproduct(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_designproduct'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')  # noqa
    else:
        form = ProductForm()

    template = 'designproducts/add_designproduct.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_designproduct(request, designproduct_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    designproduct = get_object_or_404(Product, pk=designproduct_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=designproduct)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[designproduct.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')  # noqa
    else:
        form = ProductForm(instance=designproduct)
        messages.info(request, f'You are editing {designproduct.name}')

    template = 'designproducts/edit_designproduct.html'
    context = {
        'form': form,
        'designproduct': designproduct,
    }

    return render(request, template, context)


@login_required
def delete_designproduct(request, designproduct_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=designproduct_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('designproducts'))

@login_required
def like_toggle(request, designproduct_id):
    designproduct = get_object_or_404(Product, pk=designproduct_id)
    user = request.user

    if user in designproduct.likes.all():
        designproduct.likes.remove(user)
        liked = False
    else:
        designproduct.likes.add(user)
        liked = True

    return redirect('product_detail', designproduct_id=designproduct_id)
