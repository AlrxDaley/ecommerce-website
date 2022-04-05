from email import message
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from .models import product

# Create your views here.

def all_products(request):
    """A view to show all products, including sorting and search queries"""
    
    Products = product.objects.all()
    query = None
    
    
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You didnt enter any search criteria!')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            Products = Products.filter(queries)
    
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

