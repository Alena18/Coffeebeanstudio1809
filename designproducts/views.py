from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

def all_products(request):

    """ A view to show individual product details """

    designproducts = Product.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('designproducts'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            designproducts = designproducts.filter(queries)

    context = {
        'designproducts': designproducts,
        'search_term': query,
    }

    return render(request, 'designproducts/designproducts.html', context)

def product_detail(request, designproduct_id):

    """ A view to show all products, including sort and search queries """

    designproduct = get_object_or_404(Product, pk=designproduct_id)

    context = {
        'designproduct': designproduct,
    }

    return render(request, 'designproducts/product_detail.html', context)
