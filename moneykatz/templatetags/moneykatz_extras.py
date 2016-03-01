from django import template
from moneykatz.models import Category

register = template.Library()


@register.inclusion_tag('moneykatz/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(), 'act_cat': cat}
