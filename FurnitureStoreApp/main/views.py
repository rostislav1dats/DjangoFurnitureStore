from django.shortcuts import render
from goods.models import Categories

def view_index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Home - головна',
        'content': 'Магазин мебелів HOME',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)

def view_about(request): 
    context = {
        'title': 'Home - Інфо',
        'content': 'Про нас',
        'text_on_page': 'Текст про те чому це такий класний магазин і чудовий товар.'
    }
    return render(request, 'main/about.html', context)
