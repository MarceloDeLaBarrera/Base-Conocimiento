"""Proyecto_Tesis URL Configuration

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

from posixpath import relpath
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse
from django.shortcuts import redirect
from django.conf import settings
from base_app import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path("register/", views.register_request, name="register"),
    path("", views.admin_view, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Base de Conocimiento"
admin.site.index_title = "Base de Conocimiento"
admin.site.site_url = "/admin"
