from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.views.generic.detail import SingleObjectMixin

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect

from .forms import AttachmentForm, ElementForm, MachineForm, MaterialForm, ServiceForm, ToolForm, VendorForm
from .models import Attachment, Element, Machine, Material, Service, Tool, Vendor
from .filters import ElementFilter, MachineFilter, MaterialFilter, ServiceFilter, ToolFilter, VendorFilter

User = get_user_model()


class HomeView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        return render(request, "base.html")


class AddVendorView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.add_vendor'
    model = Vendor
    form_class = VendorForm
    template_name = 'machining/add_vendor.html'
    success_url = reverse_lazy('vendor-list')


class AddServiceView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.add_service'
    model = Service
    form_class = ServiceForm
    template_name = 'machining/add_service.html'
    success_url = reverse_lazy('service-list')


class AddToolView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.add_tool'
    model = Tool
    form_class = ToolForm
    template_name = 'machining/add_tool.html'
    success_url = reverse_lazy('tool-list')


class AddMaterialView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.add_material'
    model = Material
    form_class = MaterialForm
    template_name = 'machining/add_material.html'
    success_url = reverse_lazy('material-list')


class AddMachineView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.add_machine'
    model = Machine
    form_class = MachineForm
    template_name = 'machining/add_machine.html'
    success_url = reverse_lazy('machine-list')


class AddElementView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = reverse_lazy('login')
    permission_required = 'machining.add_element'
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


class VendorList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_vendor'
    paginate_by = 15
    model = Vendor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = VendorFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ServiceList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_service'
    paginate_by = 15
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ServiceFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ToolList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_tool'
    paginate_by = 15
    model = Tool

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ToolFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MaterialList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_material'
    paginate_by = 15
    model = Material

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MaterialFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MachineList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_machine'
    paginate_by = 15
    model = Machine

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MachineFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ElementList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_element'
    paginate_by = 15
    model = Element

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ElementFilter(self.request.GET, queryset=self.get_queryset())
        return context


class VendorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.change_vendor'
    model = Vendor
    form_class = VendorForm
    template_name = 'machining/add_vendor.html'
    success_url = reverse_lazy('vendor-list')


class ServiceUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.change_service'
    model = Service
    form_class = ServiceForm
    template_name = 'machining/add_service.html'
    success_url = reverse_lazy('service-list')


class ToolUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.change_tool'
    model = Tool
    form_class = ToolForm
    template_name = 'machining/add_tool.html'
    success_url = reverse_lazy('tool-list')


class MaterialUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.change_material'
    model = Material
    form_class = MaterialForm
    template_name = 'machining/add_material.html'
    success_url = reverse_lazy('material-list')


class MachineUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.change_machine'
    model = Machine
    form_class = MachineForm
    template_name = 'machining/add_machine.html'
    success_url = reverse_lazy('machine-list')


class ElementUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.change_element'
    model = Element
    form_class = ElementForm
    template_name = 'machining/add_element.html'
    success_url = reverse_lazy('element-list')


class VendorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.delete_vendor'
    model = Vendor
    success_url = reverse_lazy('vendor-list')


class ServiceDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.delete_service'
    model = Service
    success_url = reverse_lazy('service-list')


class ToolDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.delete_tool'
    model = Tool
    success_url = reverse_lazy('tool-list')


class MaterialDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.delete_material'
    model = Material
    success_url = reverse_lazy('material-list')


class MachineDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.delete_machine'
    model = Machine
    success_url = reverse_lazy('machine-list')


class ElementDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.delete_element'
    model = Element
    success_url = reverse_lazy('element-list')


class AddAttachmentView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = reverse_lazy('login')
    permission_required = 'machining.add_attachment'
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


class ElementDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_element'
    model = Element

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AttachmentDelete(LoginRequiredMixin, DeleteView, PermissionRequiredMixin, SingleObjectMixin):
    login_url = reverse_lazy('login')
    permission_required = 'machining.delete_attachment'
    model = Attachment
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        success_url = reverse_lazy('element-detail',
                                   kwargs={'pk': self.kwargs['e_pk']})
        return success_url


class MachineDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_machine'
    model = Machine


class MaterialDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_material'
    model = Material


class ServiceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_service'
    model = Service


class ToolDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_tool'
    model = Tool


class VendorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    permission_required = 'machining.view_vendor'
    model = Vendor
