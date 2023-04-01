from django import template
from django.urls import reverse, NoReverseMatch
from django.db.models import Prefetch

from menu.models import MenuItem

register = template.Library()


def get_menu_items(menu_items, current_url):
    for item in menu_items:
        try:
            item.url = reverse(item.url)
        except NoReverseMatch:
            item.url = item.url

        if current_url.startswith(item.url):
            item.is_active = True

            for child in item.children.all():
                child.is_expanded = True
        else:
            item.is_active = False

        if item.parent is not None:
            item.is_child = True

    return menu_items


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_title):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu_name=menu_title).select_related('parent').prefetch_related('children')
    current_url = request.path

    menu_items = [item for item in menu_items if item.menu_name == menu_title]

    menu_items = get_menu_items(menu_items, current_url)

    return {'menu_items': menu_items}
