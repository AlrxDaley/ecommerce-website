from django.shortcuts import get_object_or_404, render
from .models import product

# Create your views here.

def all_products(request):
    """A view to show all products, including sorting and search queries"""
    
    Products = product.objects.all()
    
    context = {
        'products': Products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    
    Product = get_object_or_404(product, pk=product_id)
    
    context = {
        'products': Product,
    }

    return render(request, 'products/products_detail.html', context)

