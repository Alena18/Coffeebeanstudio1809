from django.shortcuts import render
from .models import Product

def all_products(request):

    """ A view to show all products, including sort and search queries """

    designproducts = Product.objects.all()

    context = {
        'designproducts': designproducts,
    }

    return render(request, 'designproducts/designproducts.html', context)

