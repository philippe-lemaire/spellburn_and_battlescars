"""spellburn_and_battlescars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("characters/", include("characters.urls")),
    path("npcs/", include("creatures.urls")),
    path("authentification/", include("simple_auth.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
]

handler404 = "spellburn_and_battlescars.views.page_not_found_view"
handler500 = "spellburn_and_battlescars.views.error_view"
