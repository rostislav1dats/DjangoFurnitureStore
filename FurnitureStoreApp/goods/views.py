from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from .models import Products


def view_catalog(request, category_slug):
    page_number = request.GET.get('page', )
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page_number))
    elided_page_range = paginator.get_elided_page_range(current_page.number, on_each_side=2, on_ends=1)

    context = {
        'title': 'Home - Catalog',
        'goods': current_page,
        'page_range': elided_page_range,
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
