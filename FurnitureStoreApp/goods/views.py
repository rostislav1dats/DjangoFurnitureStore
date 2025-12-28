from django.shortcuts import render
from .models import Products


def view_catalog(request):
    goods = Products.objects.all()
    context = {
        'title': 'Home - Catalog',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context=context)


def view_product(request):
    return render(request, 'goods/product.html')
