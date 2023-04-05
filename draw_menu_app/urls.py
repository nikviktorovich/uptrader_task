from django.urls import re_path
from . import views


urlpatterns = [
    re_path(
        r'^(?P<menu_tree>([a-z0-9_-]+/)*)$',
        view=views.draw_menu_view,
        name='draw_menu',
    ),
]

