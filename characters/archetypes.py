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

abilities_cleric = (
    (
        0,
        "Healer • Burn 1 LUCK and make an appropriate Save to remove a disease, poison or curse from a Close target.",
    ),
    (
        1,
        "Miracle • You can beg your deity for aid in a desperate manner.\nWhen you do so, Save LUCK, on a success your plea is heard precisely, on a failure it doesn’t happen exactly as you expected. Regardless of the result, your LUCK becomes 0 after the roll.",
    ),
    (
        2,
        "Sacrifice • You can regain LUCK by making offerings to appease your deity, being that wealth or specific items related to your faith. How much LUCK is received depends on the magnitude of the sacrifice, at the GM's discretion.",
    ),
    (
        3,
        "Turn Unholy • You may suffer Fatigue to make all Nearby creatures considered heretical to your deity test Morale (pg 32).",
    ),
)

abilities_fighter = (
    (
        0,
        "Combat Maneuvers • In combat, you can attack and make a maneuver (disarm, blind, etc) in the same action.",
    ),
    (
        1,
        "Critical Hits • When you inflict BODY Damage but the target succeeds in the Critical Damage Save, their attacks are Impaired on the next Round.",
    ),
    (
        2,
        "Scrap Fighter • You can destroy one item you're carrying to ignore Damage you're about to suffer, as long as you can explain how the item protects you.",
    ),
    (
        3,
        "Slayer • When fighting with weapons, you re-roll any Damage rolls of 1.  You must use the new result.",
    ),
)

abilities_magic_user = (
    (
        0,
        "Arcanist • Reading magical runes, interpreting scrolls, and dealing with other magical items is Trivial to you.",
    ),
    (
        1,
        "Blood Sacrifice • Once per Casting Spell, you may take d4 Damage to add +1 Power to your roll. Reduce any Fatigue created by this spell by 1.",
    ),
    (
        2,
        "Dangerous Magic • When you Cast Spell, you may burn 1 LUCK to re-roll all dice used. You must use the new roll.",
    ),
    (
        3,
        "Familiar • Gain a mystical companion with 3 HP and an interesting ability (determined by the GM). You can communicate with it telepathically as long as you can see it. If it dies, it can be re-summoned one week later by spending a night's work.",
    ),
)

abilities_thief = (
    (0, "Expertise • You do thief stuff with Advantage (hide, climb, etc).  "),
    (
        1,
        "Lucky • At the start of each session Roll d20, if the result is higher than your current LUCK, increase it by 1.",
    ),
    (
        2,
        "Practiced in Shadows • Attempting to hide or move with stealth against non-magical creatures of similar sensory ability to humans is Trivial to you.",
    ),
    (
        3,
        "Thieves’ Cant • You speak a secret dialect know only by other thieves, allowing you to hide messages inside seemingly normal conversations.",
    ),
)

abilities_dwarf = (
    (
        0,
        "Combat Maneuvers • In combat, you can attack and make a maneuver (disarm, blind, etc) in the same action.",
    ),
    (1, "Dwarven Senses • You can sniff out gold items and precious gems Nearby."),
    (2, "Resilience • You have Advantage on Saves against poison and disease."),
    (
        3,
        "Shield Master • While wearing a shield, you can suffer Fatigue to ignore the physical Damage received from an attack.",
    ),
)

abilities_elf = (
    (0, "Ancient Mind • You’re immune to magical sleep and paralysis.  "),
    (
        1,
        "Arcane by Nature • Once per day, you can make a LUCK Save to ignore a spell Mishap.",
    ),
    (
        2,
        'Heightened Senses • You get a "weird feeling" when there’s a secret passage Close to you.',
    ),
    (
        3,
        "Precise Grace • So long as you are aware of the threat, you can never be disarmed.",
    ),
)

abilities_halfling = (
    (
        0,
        "Good Luck Charm • Once per session, you can have an ally in eyesight to remake any roll. They choose which result to keep.",
    ),
    (
        1,
        "Lucky • At the start of each session Roll d20, if the result is higher than your current LUCK, increase it by 1.",
    ),
    (
        2,
        "Slippery • You have Advantage on Saves made to sneak and hide, and can do so even against creatures with supernatural senses.",
    ),
    (
        3,
        "Two-weapon Fighter • When you're dual wielding, you have a +d8 Bonus Damage to your attacks.",
    ),
)

triggers_cleric = "Begin with one. Gain another when you Recover a Treasure or Consecrate a Place of Power."
triggers_fighter = (
    "Begin with one. Gain another when you Recover a Treasure or Defeat a Notable Foe."
)
triggers_magic_user = "Begin with one. Gain another when you Recover a Treasure or Uncover Ancient Knowledge."
triggers_thief = (
    "Begin with one. Gain another when you Recover a Treasure or Succeed in a Heist."
)
triggers_dwarf = "Begin with one. Gain another when you Recover a Treasure or Strengthen your People."
triggers_elf = (
    "Begin with one. Gain another when you Recover a Treasure or Amend with Nature."
)
triggers_halfling = (
    "Begin with one. Gain another when you Recover a Treasure or Achieve Greatness."
)

triggers = (
    triggers_cleric,
    triggers_fighter,
    triggers_magic_user,
    triggers_thief,
    triggers_thief,
    triggers_dwarf,
    triggers_elf,
    triggers_halfling,
)
abilities_choices = (
    abilities_cleric,
    abilities_fighter,
    abilities_magic_user,
    abilities_thief,
    abilities_dwarf,
    abilities_elf,
    abilities_halfling,
)

triggers_dict = dict(zip(archetypes, triggers))

abilities_dict = dict(zip(archetypes, abilities_choices))


# starting gear

gear_cleric = [
    "Heavy Maul (d10, bulky)",
    "Chainmail (2 Armor, bulky)",
    "",
    "Helmet (+1 Armor)",
    "Holy Symbol",
    " Cloak of the Order",
]

gear_fighter = [
    "Glaive (d10, bulky)",
    "",
    "Arming Sword (d8)",
    "Shortbow (d6)",
    "Splintmail (1 Armor)",
    "Tobacco & Pipe",
    "Dice Set",
]

gear_magic_user = [
    "Fizzled Staff (d6)",
    "Grimoire (pick one spell, bulky)",
    "",
    "Scroll (random spell)",
    "Ragged Clothing (hidden pockets)",
    "Two Leycaps (pg 47)",
]

gear_thief = [
    "Dagger (d6)",
    "Dagger (d6)",
    "Hooded Jerkin (1 Armor)",
    "Lockpicks",
    "Grappling Hook",
    "Metal File",
]

gear_dwarf = [
    "Mace (d8)",
    "Chainmail (2 Armor, bulky)",
    "",
    "Shield (+1 Armor)",
    "Pick",
    "Large Sack",
]


gear_elf = [
    "Elegant Sword (d8)",
    "Recurve Bow (d8)",
    "Gilt Clothing (1 Armor)",
    "Grimoire (Charm or Detect Magic, bulky)",
    "",
    "Silken Rope",
]

gear_halfling = [
    "Sling (d4)",
    "Fancy Leathers (1 Armor)",
    "Shortsword (d6)",
    "Shortsword (d6)",
    "Bag of Marbles",
    "Tobacco Pouch & Pipe",
]


gear = [
    gear_cleric,
    gear_fighter,
    gear_magic_user,
    gear_thief,
    gear_dwarf,
    gear_elf,
    gear_halfling,
]

starting_gear_dict = dict(zip(archetypes, gear))
