import django_filters
from .models import Element, Machine, Material, Service, Tool, Vendor


class VendorFilter(django_filters.FilterSet):
    class Meta:
        model = Vendor
        fields = {
            'name': ['icontains'],
            'address': ['icontains'],
            'phone': ['icontains'],
            'tax_number': ['icontains'],
        }


class ServiceFilter(django_filters.FilterSet):
    class Meta:
        model = Service
        fields = {
            'name': ['icontains'],
            'address': ['icontains'],
            'phone': ['icontains'],
            'tax_number': ['icontains'],
        }


class MachineFilter(django_filters.FilterSet):
    service = django_filters.ModelChoiceFilter(queryset=Service.objects.all())

    class Meta:
        model = Machine
        fields = {
            'name': ['icontains'],
            'manufacturer': ['icontains'],
            'type': ['icontains'],
            'service': [],
        }


class ToolFilter(django_filters.FilterSet):
    vendor = django_filters.ModelChoiceFilter(queryset=Vendor.objects.all())

    class Meta:
        model = Tool
        fields = {
            'name': ['icontains'],
            'kind': ['icontains'],
            'size': ['icontains'],
            'number_tiles': ['icontains'],
            'height': ['icontains'],
            'vendor': [],
        }


class MaterialFilter(django_filters.FilterSet):
    class Meta:
        model = Material
        fields = {
            'name': ['icontains'],
            'symbol': ['icontains'],
        }


class ElementFilter(django_filters.FilterSet):
    material = django_filters.ModelChoiceFilter(queryset=Material.objects.all())
    machine = django_filters.ModelChoiceFilter(queryset=Machine.objects.all())

    class Meta:
        model = Element
        fields = {
            'name': ['icontains'],
            'version': ['icontains'],
            'material': [],
            'machine': [],
        }
