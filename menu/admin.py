from django.contrib import admin
from .models import MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0
    exclude = ('is_active',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_name', 'url', 'parent')
    inlines = [MenuItemInline]
    exclude = ('is_active',)
