from django.urls import path

from . import views

app_name = "characters"

urlpatterns = [
    path("create_character", views.create_character, name="create_character"),
    path("my_characters", views.my_characters.as_view(), name="my_characters"),
    path(
        "my_characters/detail/<int:pk>",
        views.character_detail.as_view(),
        name="character_detail",
    ),
    path(
        "my_characters/delete/<int:pk>", views.delete_character, name="delete_character"
    ),
    path("scars", views.Scars.as_view(), name="scars"),
    path("magic/spells", views.Spells.as_view(), name="spells"),
    path("magic/mishaps", views.Mishaps.as_view(), name="mishaps"),
    path("magic/roll_spell", views.roll_spell_view, name="roll_spell"),
    path("equipment", views.Equipment.as_view(), name="equipment"),
]
