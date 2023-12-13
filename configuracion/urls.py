"""
URL configuration for configuracion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import handler400, handler403, handler404, handler500
from django.views.generic import TemplateView
from modulos.acceso.views import acceder, recovery_password_vista
urlpatterns = [
    path('admin/', admin.site.urls),

    # INDEX
    path('', acceder, name='index'),

    # RECOVERY PASSWORD
    path('recovery_password_vista/', recovery_password_vista, name='recovery_password'),

    # MODULO DE ANALISIS
    path('', include('modulos.restaurante.urls')),
    # MODULOS
    path('acceso/', include('modulos.acceso.urls')),
    path('usuarios/', include('modulos.usuarios.urls')),
    path('productos/', include('modulos.productos.urls')),
    path('menu/', include('modulos.menu.urls')),
    path('proveedores/', include('modulos.proveedores.urls')),
]
