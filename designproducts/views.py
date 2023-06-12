from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

def all_products(request):

    """ A view to show individual product details """

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
                designproducts = designproducts.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            designproducts = designproducts.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            designproducts = designproducts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('designproducts'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
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

    """ A view to show all products, including sort and search queries """

    designproduct = get_object_or_404(Product, pk=designproduct_id)

    context = {
        'designproduct': designproduct,
    }

    return render(request, 'designproducts/product_detail.html', context)
