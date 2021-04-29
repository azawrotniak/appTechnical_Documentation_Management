from django import forms

from .models import Element, Machine, Material, Service, Tool, Vendor


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'address', 'phone', 'tax_number']


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'address', 'phone', 'tax_number']


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'manufacturer', 'type', 'serial_number', 'service', 'vendor']


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'kind', 'size', 'number_tiles', 'height', 'vendor']


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'symbol']


class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['name', 'version', 'material', 'machine', 'tool']