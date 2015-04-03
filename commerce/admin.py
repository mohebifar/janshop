from django.contrib import admin
from models import *
from django.utils.translation import ugettext_lazy as _
from forms import ProductForm


admin.site.index_title = _('Site administration')
admin.site.site_title = _('Site administration')
admin.site.app_name = _('Commerce')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)


class StructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'properties_list',)
    search_fields = ('name',)

    def properties_list(self, obj):
        return " - ".join([p.name for p in obj.properties.all()])


class DetailInline(admin.TabularInline):
    model = Detail


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        DetailInline,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Structure, StructureAdmin)
admin.site.register(Property, PropertyAdmin)