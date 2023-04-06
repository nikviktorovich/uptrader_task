import collections
from django import template
from django.db.models import Q
from .. import models


register = template.Library()


@register.inclusion_tag('draw_menu_app/draw_menu.html', takes_context=True)
def draw_menu(context, root: str):
    """Draws menu tree"""
    menu_tree = context['menu_tree']
    menu_tree = [root] + menu_tree

    # Getting all needed menus
    menu_list = models.Menu.objects.filter(
        Q(name__in=menu_tree) | Q(parent__name__in=menu_tree)
    ).select_related('parent').all()
    menu_dict = {menu.name: menu for menu in menu_list}

    # Making dictionary of parents and their children menus
    children_dict = collections.defaultdict(list)
    for menu in menu_list:
        if not menu.parent:
            continue

        children_dict[menu.parent.name].append(menu.name)

    return {
        'menu_name': root,
        'menu_tree': menu_tree,
        'menu_path_head': [],
        'menu_dict': menu_dict,
        'children_dict': children_dict,
    }
