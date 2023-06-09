from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):

    """ A view to show individual product details """

    designproducts = Product.objects.all()

    context = {
        'designproducts': designproducts,
    }

    return render(request, 'designproducts/designproducts.html', context)

def product_detail(request, designproduct_id):

    """ A view to show all products, including sort and search queries """

    designproduct = get_object_or_404(Product, pk=designproduct_id)

    context = {
        'designproduct': designproduct,
    }

    return render(request, 'designproducts/product_detail.html', context)
