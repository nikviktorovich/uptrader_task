import logging
from django import template


logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag('draw_menu_app/draw_menu_item.html', takes_context=True)
def draw_menu_item(context, menu_item: str):
    """Draws a single menu item"""
    menu_tree_head = context['menu_tree_head']
    menu_tree_tail = context['menu_tree_tail']
    menu_path_head = context['menu_path_head']
    menu_dict = context['menu_dict']
    children_dict = context['children_dict']

    assert menu_item in menu_dict

    readable_name = menu_dict[menu_item].readable_name
    
    if menu_tree_head[-1] == menu_item:
        children = children_dict[menu_item]
    else:
        children = []
    
    new_menu_tree_head = menu_tree_head + menu_tree_tail[:1] # Head of request
    menu_path_head = menu_path_head + [menu_item] # Head of current menu path
    menu_path = '/'.join(menu_path_head[1:] + ['']) # '' grants trailing slash

    return {
        'readable_name': readable_name,
        'menu_tree_head': new_menu_tree_head,
        'menu_tree_tail': menu_tree_tail[1:],
        'menu_path_head': menu_path_head,
        'menu_path': menu_path,
        'menu_dict': menu_dict,
        'children_dict': children_dict,
        'children': children,
    }