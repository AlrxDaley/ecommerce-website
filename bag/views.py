from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """A view to retun the bags content page"""
    return render(request, 'bag/bag.html')