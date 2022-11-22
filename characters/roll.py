from random import randint
from .mishaps import mishaps


def roll_stats(prioritize_body=True):
    """function to roll stats"""
    results = []

    for _ in range(3):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        result = d1 + d2 + 3
        results.append(result)

    results.sort()

    luck = results[0]
    if prioritize_body:
        body = results[2]
        mind = results[1]
    else:
        mind = results[2]
        body = results[1]

    return body, mind, luck


def roll_save(stat, advantage=False, disadvantage=False):
    stat = int(stat)
    roll = randint(1, 20)

    if advantage ^ disadvantage:
        roll2 = randint(1, 20)

    if advantage and not disadvantage:
        roll = min(roll, roll2)
    if disadvantage and not advantage:
        roll = max(roll, roll2)

    if roll == 20:
        return "Natural 20! Failure"
    if roll == stat:
        return "Critical Success! Mark +1 LUCK!"
    if roll < stat:
        return "Success"
    return "Failure…"


def roll_spell(power):

    # roll the power * d6
    dice = [randint(1, 6) for d in range(power)]
    print(dice)
    # each die above 3 gives fatigue
    fatigue = len([d for d in dice if d > 3])

    # check if mishap with length of the set of dice
    if len(set(dice)) < len(dice):
        sum_ = sum(dice)
        if sum_ > 21:
            sum_ = 21
        return mishaps.get(sum_)

    return sum(dice), fatigue
