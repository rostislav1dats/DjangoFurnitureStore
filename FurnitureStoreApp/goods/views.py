from django.shortcuts import render


def view_catalog(request):
    context = {
        'title': 'Home - Catalog',
    }
    return render(request, 'goods/catalog.html', context=context)


def view_product(request):
    return render(request, 'goods/product.html')
