from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import ElementForm, MachineForm, MaterialForm, ServiceForm, ToolForm, VendorForm
from .models import Element, Machine, Material, Service, Tool, Vendor


class HomeView(View):
    def get(self, request):
        return render(request, "base.html")


class AddVendorView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'machining/add_vendor.html'
    success_url = reverse_lazy('vendor-list')


class AddServiceView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'machining/add_service.html'
    success_url = reverse_lazy('service-list')


class AddToolView(CreateView):
    model = Tool
    form_class = ToolForm
    template_name = 'machining/add_tool.html'
    success_url = reverse_lazy('tool-list')


class AddMaterialView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'machining/add_material.html'
    success_url = reverse_lazy('material-list')


class AddMachineView(CreateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machining/add_machine.html'
    success_url = reverse_lazy('machine-list')


class AddElementView(CreateView):
    model = Element
    form_class = ElementForm
    template_name = 'machining/add_element.html'
    success_url = reverse_lazy('element-list')


class VendorList(ListView):
    model = Vendor


class ServiceList(ListView):
    model = Service


class ToolList(ListView):
    model = Tool


class MaterialList(ListView):
    model = Material


class MachineList(ListView):
    model = Machine


class ElementList(ListView):
    model = Element


class VendorUpdate(UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'machining/add_vendor.html'
    success_url = reverse_lazy('vendor-list')


class ServiceUpdate(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'machining/add_service.html'
    success_url = reverse_lazy('service-list')


class ToolUpdate(UpdateView):
    model = Tool
    form_class = ToolForm
    template_name = 'machining/add_tool.html'
    success_url = reverse_lazy('tool-list')


class MaterialUpdate(UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'machining/add_material.html'
    success_url = reverse_lazy('material-list')


class MachineUpdate(UpdateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machining/add_machine.html'
    success_url = reverse_lazy('machine-list')


class ElementUpdate(UpdateView):
    model = Element
    form_class = ElementForm
    template_name = 'machining/add_element.html'
    success_url = reverse_lazy('element-list')


class VendorDelete(DeleteView):
    model = Vendor
    success_url = reverse_lazy('vendor-list')


class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('service-list')


class ToolDelete(DeleteView):
    model = Tool
    success_url = reverse_lazy('tool-list')


class MaterialDelete(DeleteView):
    model = Material
    success_url = reverse_lazy('material-list')


class MachineDelete(DeleteView):
    model = Machine
    success_url = reverse_lazy('machine-list')


class ElementDelete(DeleteView):
    model = Element
    success_url = reverse_lazy('element-list')
