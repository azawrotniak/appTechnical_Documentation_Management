from django.views.generic import CreateView

from .forms import ElementForm, MachineForm, MaterialForm, ServiceForm, ToolForm, VendorForm
from .models import Element, Machine, Material, Service, Tool, Vendor


class AddVendorView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'machining/add_vendor.html'


class AddServiceView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'machining/add_service.html'


class AddToolView(CreateView):
    model = Tool
    form_class = ToolForm
    template_name = 'machining/add_tool.html'


class AddMaterialView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'machining/add_material.html'


class AddMachineView(CreateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machining/add_machine.html'


class AddElementView(CreateView):
    model = Element
    form_class = ElementForm
    template_name = 'machining/add_element.html'


