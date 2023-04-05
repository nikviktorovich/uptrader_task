from django.contrib import admin
from . import models


# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Menu, MenuAdmin)
