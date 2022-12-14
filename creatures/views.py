from django.views import generic
from .models import Creature


class IndexView(generic.ListView):
    model = Creature
    ordering = ["name"]


class CreatureDetailView(generic.DetailView):
    model = Creature


class HirelingsView(generic.TemplateView):
    template_name = "creatures/hirelings.html"


class NPCView(generic.TemplateView):
    template_name = "creatures/NPCs.html"
