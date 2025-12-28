from django.shortcuts import render
from .models import Products


def view_catalog(request):
    goods = Products.objects.all()
    context = {
        'title': 'Home - Catalog',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context=context)


def view_product(request, product_slug=False, product_id=False):
    if product_id:
        product = Products.objects.get(id=product_id)
    else:
        product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context)
