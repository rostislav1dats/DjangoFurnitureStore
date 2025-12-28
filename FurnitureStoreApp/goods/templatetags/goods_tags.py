from django import template
from goods.models import Categories

register = template.Library()

@register.simple_tag()
def get_tag_categories():
    return Categories.objects.order_by('name')
