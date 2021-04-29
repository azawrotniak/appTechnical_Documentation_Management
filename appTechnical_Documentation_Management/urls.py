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
    path('add_vendor/', ex_view.AddVendorView.as_view(), name="add-vendor"),
    path('add_service/', ex_view.AddServiceView.as_view(), name="add-service"),
    path('add_tool/', ex_view.AddToolView.as_view(), name="add-tool"),
    path('add_material/', ex_view.AddMaterialView.as_view(), name="add-material"),
    path('add_machine/', ex_view.AddMachineView.as_view(), name="add-machine"),
    path('add_element/', ex_view.AddElementView.as_view(), name="add-element"),
]
