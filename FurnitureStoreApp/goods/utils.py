from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import Products

def search_q(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector('name', 'description', config='english')
    query = SearchQuery(query, config='english')

    return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0.00001).order_by("-rank")
