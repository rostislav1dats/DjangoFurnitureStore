from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from .models import Products
from .utils import search_q


def view_catalog(request, category_slug=None):
    page_number = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.select_related('category').all()
    elif query:
        goods = search_q(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page_number))
    elided_page_range = paginator.get_elided_page_range(current_page.number, on_each_side=2, on_ends=1)

    context = {
        'title': 'Home - Catalog',
        'goods': current_page,
        'page_range': elided_page_range,
        'slug_url': category_slug,
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
