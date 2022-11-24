from django import forms


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


class RollSpellForm(forms.Form):
    power = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="What's the power level you are casting with ? Up to your free inventory slots (max 5). High power levels are dangerous.",
        required=True,
    )
