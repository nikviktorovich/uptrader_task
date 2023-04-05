from django.shortcuts import render


# Create your views here.

def draw_menu_view(request, menu_tree: str):
    menu_tree_list = menu_tree.split('/')

    # Removing unnecessary '' path node
    if menu_tree_list and not menu_tree_list[-1]:
        menu_tree_list = menu_tree_list[:-1]

    return render(request, 'draw_menu_app/index.html', context={
        'menu_tree': menu_tree_list,
    })
