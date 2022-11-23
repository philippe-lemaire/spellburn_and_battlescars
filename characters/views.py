from random import randint, choice

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .models import Character
from .forms import CharacterCreationForm


from .roll import roll_stats

from .backgrounds import backgrounds
from .equipment import equipment

from .random_names import random_names
from .archetypes import archetypes

from .equipment import equipment


@login_required
def create_character(request):
    if request.method == "POST":
        form = CharacterCreationForm(request.POST)
        if form.is_valid():
            # création du personnage proprement dit
            character = Character()
            character.archetype = CharacterCreationForm.archetype_choices[
                int(form.cleaned_data["archetype"]) - 1
            ][1]

            if character.archetype == "Random":
                character.archetype = choice(archetypes)

            character.name = form.cleaned_data["name"] or "Anonyme"
            character.user = request.user

            character.hp = randint(1, 6)
            background, bg_gear = choice(backgrounds.get(character.hp))
            character.background = background
            character.gear = bg_gear
            prioritize_body = form.cleaned_data["prioritize_body"]
            body, mind, luck = roll_stats(prioritize_body=prioritize_body)
            character.body = body
            character.mind = mind
            character.luck = luck

            # save the char
            character.save()

            # redirect to my characters or character detail
            # add a success message before
            messages.success(request, "Personnage créé.")
            return HttpResponseRedirect(reverse("characters:my_characters"))
    else:
        # build context with empty form
        context = {"form": CharacterCreationForm()}

    return render(request, "characters/create_character.html", context)


class my_characters(LoginRequiredMixin, ListView):
    model = Character
    # paginate_by = 10  # if pagination is desired
    template_name = "characters/my_characters.html"
    context_object_name = "characters"

    # redirect_field_name = "personnages/mes_personnages"

    def get_queryset(self):
        return Character.objects.filter(user=self.request.user)


class character_detail(LoginRequiredMixin, DetailView):
    model = Character
    template_name = "characters/character_detail.html"


@login_required
def delete_character(request, pk):
    character = Character.objects.get(pk=pk)
    # check if character.user and request.user match
    if character.user == request.user:
        name = character.name
        character.delete()
        messages.success(request, f"Rest in peace, {name}.")
    else:
        messages.warning(request, "This characters is not yours.")

    return HttpResponseRedirect(reverse("characters:my_characters"))
