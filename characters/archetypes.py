archetypes = ("Cleric", "Fighter", "Magic User", "Thief", "Dwarf", "Elf", "Halfling")

origin_cleric = {
    "prompt": "Who do you worship?",
    "choices": (
        (
            1,
            "God of Battle • As long as you wear a helmet, heretic creatures can’t refuse to duel with you.",
        ),
        (
            2,
            "God of Death • Anything you touch is weakened, but you may suffer backlash.",
        ),
        (
            3,
            "God of Nature • You can speak with animals, but you’re still limited by their natural intelligence.",
        ),
    ),
}

origin_fighter = {
    "prompt": "Who taught you to fight?",
    "choices": (
        (
            1,
            "Mercenary Veteran • When you inflict Critical Damage, the target loses a limb or is disemboweled.",
        ),
        (
            2,
            "Order of Knights • You always keep any mount you’re riding calm and under control.",
        ),
        (
            3,
            "Tribesmen • You can always find food and water for yourself, if the environment offers such resources.",
        ),
    ),
}

origin_magic_user = {
    "prompt": "What kind of magic do you practice?",
    "choices": (
        (
            1,
            "Elemental • Choose one element, you always have 3 Armor against it.  (Suggested Spell: Fireball)",
        ),
        (
            2,
            "Necromancy • Once per day, you can touch a humanoid skull and ask it one question, it will answer truthfully based on what it knew in life.  After that, the skull turns to dust and you suffer Fatigue. (Suggested Spell: Animate Dead)",
        ),
        (
            3,
            "Enchantment • Mundane creatures are more easily convinced by your words. (Suggested Spell: Command)",
        ),
    ),
}

origin_thief = {
    "prompt": "What is your specialty?",
    "choices": (
        (
            1,
            "Assassin • When you attack a target who’s unaware of you, you deal +d12 Bonus Damage and ignore Armor.",
        ),
        (
            2,
            "Rogue • You can find a helpful contact in any city, but you’ll also be requested to help from time to time.",
        ),
        (
            3,
            "Swindler • Forging documents and crafting convincing disguises is Trivial to you.",
        ),
    ),
}
origin_dwarf = {
    "prompt": "How did you serve your clan?",
    "choices": (
        (
            1,
            "Architect • Detecting construction tricks, traps, possible weak points etc; is Trivial to you.",
        ),
        (
            2,
            "Artisan • Choose one craft (blacksmith, jeweler, leatherworker, etc).  Executing it is Trivial to you, given the necessary time and materials.",
        ),
        (3, "Commander • Your Hirelings always succeed on Morale"),
    ),
}

origin_elf = {
    "prompt": "Which skill have you mastered over the years?",
    "choices": (
        (
            1,
            "Loremaster • If you don’t know a certain piece of knowledge, you know where to start searching.",
        ),
        (
            2,
            "Seer • Once per session, burn 1 LUCK and ask the GM a Yes/No question, they will answer truthfully.",
        ),
        (3, "Wanderer • You know how to orient yourself by looking at the stars."),
    ),
}

origin_halfling = {
    "prompt": "Why did you leave the comfort of your home?",
    "choices": (
        (
            1,
            "Inexperienced Explorer • When lost and alone, you can burn 1 LUCK to follow the right path.",
        ),
        (2, "Traveling Merchant • You're immune to fear effects."),
        (
            3,
            "Unusual Adventurer • You pass unnoticed in crowds and Opponents always attack you last.",
        ),
    ),
}


origins = dict(
    zip(
        archetypes,
        (
            origin_cleric,
            origin_fighter,
            origin_magic_user,
            origin_thief,
            origin_dwarf,
            origin_elf,
            origin_halfling,
        ),
    )
)

if __name__ == "__main__":
    print(origins)
