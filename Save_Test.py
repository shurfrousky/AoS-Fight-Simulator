print("")

import Hit_Wound_Roll_Test
import AoS_Unit_Stats
Test = Hit_Wound_Roll_Test
UnitStats = AoS_Unit_Stats
UnitSaveRate = UnitStats.Stormcast_Vindictors_Stats['SAVE']

#Rolls to save from incoming wounds
def roll_to_save(save_amount, save_rating):
    import random
    failed_saves = []
    succesful_saves = []

    for save in range(save_amount):
        d6 = random.randint(1, 6)
    
        if d6 < save_rating:
            failed_saves.append(d6)
        elif d6 >= save_rating:
            succesful_saves.append(d6)

    print(f"Rolling {save_amount} dice to save...")
    print(f"You rolled {succesful_saves}, {len(succesful_saves)} save! The rest, {failed_saves}, {len(failed_saves)} failed.")
    return failed_saves

# Calculates Damage
def calculate_dmg(failed_save):
    total_damage = 0
    for save in range(failed_save):
        UnitDamage = UnitStats.Tzaangor_Enlightened_Disc['DMG']
        total_damage += UnitDamage
        print("TESTING TESTING", total_damage)
    print(f"Total damage --> {total_damage}")

Test2 = Test.wound_total
dmg_to_take = roll_to_save(Test2, UnitSaveRate)
print("")
calculate_dmg(len(dmg_to_take))


