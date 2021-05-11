from django.views import View
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect

from .forms import AttachmentForm, ElementForm, MachineForm, MaterialForm, ServiceForm, ToolForm, VendorForm
from .models import Attachment, Element, Machine, Material, Service, Tool, Vendor
from .filters import ElementFilter, MachineFilter, MaterialFilter, ServiceFilter, ToolFilter, VendorFilter


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


class AddElementView(View):
    template_name = 'machining/add_element.html'
    form_class = ElementForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('element-list')


class VendorList(ListView):
    paginate_by = 20
    model = Vendor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = VendorFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ServiceList(ListView):
    paginate_by = 20
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ServiceFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ToolList(ListView):
    paginate_by = 20
    model = Tool

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ToolFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MaterialList(ListView):
    paginate_by = 20
    model = Material

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MaterialFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MachineList(ListView):
    paginate_by = 20
    model = Machine

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MachineFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ElementList(ListView):
    paginate_by = 20
    model = Element

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ElementFilter(self.request.GET, queryset=self.get_queryset())
        return context


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


class AddAttachmentView(View):
    template_name = 'machining/add_attachment.html'
    form_class = AttachmentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        element = get_object_or_404(Element, pk=kwargs['pk'])
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            attachment = Attachment()
            attachment.description = form.cleaned_data['description']
            attachment.type = form.cleaned_data['type']
            attachment.file = request.FILES['file']
            attachment.element = element
            attachment.save()

            return redirect('element-detail', pk=kwargs['pk'])


class ElementDetailView(DetailView):
    model = Element

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AttachmentDelete(DeleteView, SingleObjectMixin):
    model = Attachment
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        success_url = reverse_lazy('element-detail',
                                   kwargs={'pk': self.kwargs['e_pk']})
        return success_url


class MachineDetailView(DetailView):
    model = Machine


class MaterialDetailView(DetailView):
    model = Material


class ServiceDetailView(DetailView):
    model = Service


class ToolDetailView(DetailView):
    model = Tool


class VendorDetailView(DetailView):
    model = Vendor