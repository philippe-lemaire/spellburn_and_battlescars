from django.contrib import admin
from .models import Creature

# Register your models here.


class CreatureAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "hp", "body", "mind", "armor"]


admin.site.register(Creature, CreatureAdmin)
