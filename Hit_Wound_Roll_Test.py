print(" ")

import AoS_Unit_Stats # All AoS Unit Stats as Dicts
UnitStats = AoS_Unit_Stats # variable to access dicts

# Tzaangor attack profile
attacking_unit_WPN = UnitStats.Tzaangor_Enlightened_Disc['WPN']
attacking_unit_ATTK = UnitStats.Tzaangor_Enlightened_Disc['ATTK']
attacking_unit_HIT = UnitStats.Tzaangor_Enlightened_Disc['HIT']
attacking_unit_WND = UnitStats.Tzaangor_Enlightened_Disc['WND']

#rolling to hit function
def roll_to_hit(attk_amount, hit_rating):
    import random
    total_hits = 0
    failed_hits = []
    succesful_hits = []
    attk_amount *= attacking_unit_ATTK

    for attack in range(attk_amount):
        d6 = random.randint(1, 6)
    
        if d6 < hit_rating:
            failed_hits.append(d6)
        elif d6 >= hit_rating:
            succesful_hits.append(d6)
            total_hits += 1

    print(f"Attacking with '{attacking_unit_WPN}'.")
    print(f"Rolling {attk_amount} dice to hit on a {attacking_unit_HIT}+...")
    print(f"You rolled {succesful_hits}, {len(succesful_hits)} hit! The rest are {failed_hits}, {len(failed_hits)} failed!")
    print("")
    return total_hits #send reults of succesful hit dice

#rolling to wound funciton
def roll_to_wound(hit_amount, wound_rating):
    import random
    failed_wounds = []
    succesful_wounds = []

    for wound in range(hit_amount):
        d6 = random.randint(1, 6)
    
        if d6 < wound_rating:
            failed_wounds.append(d6)
        elif d6 >= wound_rating:
            succesful_wounds.append(d6)

    print(f"Rolling {hit_amount} dice to wound on a {attacking_unit_WND}+...")
    print(f"You rolled {succesful_wounds}, {len(succesful_wounds)} wound! The rest are {failed_wounds}, {len(failed_wounds)} failed!")
    print("")
    return len(succesful_wounds)


user_attk_amnt = int(input("How many models are attacking?: "))
print("")

hit_total = roll_to_hit(user_attk_amnt, attacking_unit_HIT) #put succesful hit dice into variable & do roll to hit function
wound_total = roll_to_wound(hit_total, attacking_unit_WND) #Total of succesful wound roll

