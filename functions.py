import random

# rolling to hit based on selected unit's "hit" value
def roll_to_hit(wpn_type, wpn_attk, hit_rating, attk_total ):
    failed_hits = []
    succesful_hits = []
    attk_total *= wpn_attk

    for attack in range(attk_total):
        d6 = random.randint(1, 6)
        (succesful_hits if d6 >= hit_rating else failed_hits).append(d6)

    print(f"Attacking with '{wpn_type}'.")
    print(f"Rolling {attk_total} dice to hit on a {hit_rating}+...")
    print(f"You rolled {succesful_hits}, {len(succesful_hits)} hit! The rest are {failed_hits}, {len(failed_hits)} failed!")

    return len(succesful_hits) 

# rolling to wound based on selected unit's "wound" value
def roll_to_wound(hit_total, wound_rating):
    failed_wounds = []
    succesful_wounds = []

    for wound in range(hit_total):
        d6 = random.randint(1, 6)
        (succesful_wounds if d6 >= wound_rating else failed_wounds).append(d6)

    print(f"Rolling {hit_total} dice to wound on a {wound_rating}+...")
    print(f"You rolled {succesful_wounds}, {len(succesful_wounds)} wound! The rest are {failed_wounds}, {len(failed_wounds)} failed!")

    return len(succesful_wounds)

# rolling to save based on defending unit's "save" value
def roll_to_save(save_total, save_rating, rend):
    failed_saves = []
    succesful_saves = []

    # check rend, modify save rating, roll saves
    if rend >= 1:
        save_rating += rend
    for save in range(save_total):
        d6 = random.randint(1, 6)
        (succesful_saves if d6 >= save_rating else failed_saves).append(d6)

    if rend >= 1:
        print(f"Rolling {save_total} dice to save on a {save_rating}+ (w/ {rend} rend)...")
        print(f"You rolled {succesful_saves}, {len(succesful_saves)} save! The rest, {failed_saves}, {len(failed_saves)} failed.")
    else:
        print(f"Rolling {save_total} dice to save on a {save_rating}+...")
        print(f"You rolled {succesful_saves}, {len(succesful_saves)} save! The rest, {failed_saves}, {len(failed_saves)} failed.")

    return len(failed_saves)

# calculate damage from failed saves
def calculate_dmg(failed_save_total, wpn_dmg):
    total_dmg = 0
    d3_dmg_rolls = []

    for save in range(failed_save_total):
        d3 = random.randint(1,3)

        if wpn_dmg == "D3":
            unit_dmg = d3
            d3_dmg_rolls.append(d3)
            total_dmg += unit_dmg
        else:
            unit_dmg = wpn_dmg
            total_dmg += unit_dmg
    if wpn_dmg == "D3":
        print(f"D3 damage rolls... {d3_dmg_rolls}")

    print(f"Total damage --> {total_dmg}")
    return total_dmg

def roll_to_ward_save():
    pass