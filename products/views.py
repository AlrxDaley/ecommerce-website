from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from .models import product, category

# Create your views here.

def all_products(request):
    """A view to show all products, including sorting and search queries"""
    
    Products = product.objects.all()
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
                Products = Products.annotate(lower_name=Lower('name'))
                
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            
            Products = Products.order_by(sortkey)
            

              
                
        
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            Products = Products.filter(category__name__in=categories)
            categories = category.objects.filter(name__in=categories)
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You didnt enter any search criteria!')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            Products = Products.filter(queries)
    
    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': Products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    
    Product = get_object_or_404(product, pk=product_id)
    
    context = {
        'products': Product,
    }

    return render(request, 'products/products_detail.html', context)

