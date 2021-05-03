"""appTechnical_Documentation_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from machining import views as ex_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ex_view.HomeView.as_view(), name="home"),
    path('machining/add_vendor/', ex_view.AddVendorView.as_view(), name="add-vendor"),
    path('machining/add_service/', ex_view.AddServiceView.as_view(), name="add-service"),
    path('machining/add_tool/', ex_view.AddToolView.as_view(), name="add-tool"),
    path('machining/add_material/', ex_view.AddMaterialView.as_view(), name="add-material"),
    path('machining/add_machine/', ex_view.AddMachineView.as_view(), name="add-machine"),
    path('machining/add_element/', ex_view.AddElementView.as_view(), name="add-element"),
    path('machining/vendor_list/', ex_view.VendorList.as_view(), name="vendor-list"),
    path('machining/service_list/', ex_view.ServiceList.as_view(), name="service-list"),
    path('machining/tool_list/', ex_view.ToolList.as_view(), name="tool-list"),
    path('machining/material_list/', ex_view.MaterialList.as_view(), name="material-list"),
    path('machining/machine_list/', ex_view.MachineList.as_view(), name="machine-list"),
    path('machining/element_list/', ex_view.ElementList.as_view(), name="element-list"),
    path('machining/vendor/<int:pk>/update/', ex_view.VendorUpdate.as_view(), name="update-vendor"),
    path('machining/service/<int:pk>/update/', ex_view.ServiceUpdate.as_view(), name="update-service"),
    path('machining/tool/<int:pk>/update/', ex_view.ToolUpdate.as_view(), name="update-tool"),
    path('machining/material/<int:pk>/update/', ex_view.MaterialUpdate.as_view(), name="update-material"),
    path('machining/machine/<int:pk>/update/', ex_view.MachineUpdate.as_view(), name="update-machine"),
    path('machining/element/<int:pk>/update/', ex_view.ElementUpdate.as_view(), name="update-element"),
    path('machining/vendor/<int:pk>/delete/', ex_view.VendorDelete.as_view(), name="delete-vendor"),
    path('machining/service/<int:pk>/delete/', ex_view.ServiceDelete.as_view(), name="delete-service"),
    path('machining/tool/<int:pk>/delete/', ex_view.ToolDelete.as_view(), name="delete-tool"),
    path('machining/material/<int:pk>/delete/', ex_view.MaterialUpdate.as_view(), name="delete-material"),
    path('machining/machine/<int:pk>/delete/', ex_view.MachineUpdate.as_view(), name="delete-machine"),
    path('machining/element/<int:pk>/delete/', ex_view.ElementUpdate.as_view(), name="delete-element"),
]

