from django.contrib import admin

from .models import Attachment, Element, Machine, Material, Service, Tool, Vendor

admin.site.register(Element)
admin.site.register(Machine)
admin.site.register(Material)
admin.site.register(Tool)


@admin.register(Vendor)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'address', 'phone', 'tax_number'
    ]


@admin.register(Service)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'address', 'phone', 'tax_number'
    ]
