from django.contrib import admin

# Register your models here.

from .models import Character

# Register your models here.


class CharacterAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "archetype", "user"]


admin.site.register(Character, CharacterAdmin)
