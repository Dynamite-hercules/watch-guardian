# store/views.py
from django.shortcuts import render, get_object_or_404
from .models import Watch, Brand

def product_catalog(request):
    # Fetch all watches and brands from the database
    watches = Watch.objects.all()
    brands = Brand.objects.all()
    
    context = {
        'watches': watches,
        'brands': brands,
    }
    return render(request, 'store/catalog.html', context)

def product_detail(request, slug):
    # Fetch the specific watch by its slug, or return a 404 page if not found
    watch = get_object_or_404(Watch, slug=slug)
    
    context = {
        'watch': watch,
    }
    return render(request, 'store/detail.html', context)