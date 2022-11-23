from django.urls import path

from . import views

app_name = "creatures"

urlpatterns = [
    path("opponents", views.IndexView.as_view(), name="index"),
    path(
        "<int:pk>",
        views.CreatureDetailView.as_view(),
        name="detail",
    ),
]
