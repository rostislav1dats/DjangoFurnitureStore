from django.shortcuts import render

def view_index(request):
    context = {
        'title': 'Home - головна',
        'content': 'Магазин мебелів HOME',
    }
    return render(request, 'main/index.html', context)

def view_about(request): 
    context = {
        'title': 'Home - Інфо',
        'content': 'Про нас',
        'text_on_page': 'Текст про те чому це такий класний магазин і чудовий товар.'
    }
    return render(request, 'main/about.html', context)
