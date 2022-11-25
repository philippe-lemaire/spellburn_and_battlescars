from django import forms
from .archetypes import origins, triggers_dict, abilities_dict
from .spells import spell_choices


class CharacterCreationForm(forms.Form):
    name = forms.CharField(
        label="Name of the character. Leave empty for a random name.",
        max_length=100,
        required=False,
    )
    archetype_choices = (
        ("1", "Cleric"),
        ("2", "Fighter"),
        ("3", "Magic-User"),
        ("4", "Thief"),
        ("5", "Dwarf"),
        ("6", "Elf"),
        ("7", "Halfling"),
        ("8", "Random"),
    )

    archetype = forms.ChoiceField(
        label="What archetype do you want to be?",
        choices=archetype_choices,
        required=True,
    )

    prioritize_body = forms.BooleanField(
        label="Do you want to prioritize BODY over MIND?",
        required=False,
    )


class ChooseOriginForm(forms.Form):
    origin = forms.ChoiceField(
        label="<b>Origins</b><br>",
        choices=[],
        required=True,
    )
    ability = forms.ChoiceField(
        label="<b>Abilities</b><br>",
        choices=[],
        required=True,
    )

    def __init__(self, archetype=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if archetype:
            self.fields["origin"].choices = origins.get(archetype).get("choices")
            self.fields["origin"].label += origins.get(archetype).get("prompt")
            self.fields["ability"].label += triggers_dict.get(archetype)
            self.fields["ability"].choices = abilities_dict.get(archetype)


class RollSpellForm(forms.Form):
    spell = forms.ChoiceField(choices=spell_choices)
    power = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="How many dice do you want to invest?",
        required=True,
    )
