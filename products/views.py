from django.shortcuts import render
from .models import product

# Create your views here.

def all_products(request):
    """A view to show all products, including sorting and search queries"""
    
    Products = product.objects.all()
    
    context = {
        'products': Products,
    }

    return render(request, 'products/products.html', context)