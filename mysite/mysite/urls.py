"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from prueba.views import inicio_ver, descuento
from prueba.views import home_ver
from prueba.views import actividades_ver


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_ver,name='home'),
    path('inicio/', home_ver,name='inicio'),
    path('descuento/', descuento,),
    path('tarea/', actividades_ver,name='tarea'),
]
#vistas globales