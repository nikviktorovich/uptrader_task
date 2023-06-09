import logging
from typing import Dict
from typing import List
from django import template
from .. import models


logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag('draw_menu_app/draw_menu_item.html', takes_context=True)
def draw_menu_item(context, menu_item: str):
    """Draws a single menu item"""
    menu_tree: List[str] = context['menu_tree']
    menu_path_head: List[str] = context['menu_path_head']
    menu_dict: Dict[str, models.Menu] = context['menu_dict']
    children_dict: Dict[str, List[str]] = context['children_dict']

    assert menu_item in menu_dict

    readable_name = menu_dict[menu_item].readable_name
    
    if menu_tree and menu_tree[0] == menu_item:
        children = children_dict[menu_item]
    else:
        children = []
    
    new_menu_path_head = menu_path_head + [menu_item] # Head of current menu path
    menu_path = '/'.join(new_menu_path_head[1:] + ['']) # '' grants trailing slash

    return {
        'readable_name': readable_name,
        'menu_tree': menu_tree[1:],
        'menu_path_head': new_menu_path_head,
        'menu_path': menu_path,
        'menu_dict': menu_dict,
        'children_dict': children_dict,
        'children': children,
    }