import AoS_Unit_Stats
from functions import roll_to_hit, roll_to_wound, roll_to_save, calculate_dmg

UnitStats = AoS_Unit_Stats 
# Tzaangor attack profile
attacking_unit_WPN = UnitStats.Tzaangor_Enlightened_Disc['WPN']
attacking_unit_ATTK = UnitStats.Tzaangor_Enlightened_Disc['ATTK']
attacking_unit_HIT = UnitStats.Tzaangor_Enlightened_Disc['HIT']
attacking_unit_WND = UnitStats.Tzaangor_Enlightened_Disc['WND']
attacking_unit_RND = UnitStats.Tzaangor_Enlightened_Disc['RND']
attacking_unit_DMG = UnitStats.Tzaangor_Enlightened_Disc['DMG']
# Stormcast stats
defending_unit_SAVE = UnitStats.Stormcast_Vindictors_Stats['SAVE']



attk_amnt = int(input("How many models are attacking?: "))
print("")

hit_total = roll_to_hit(attacking_unit_WPN, attacking_unit_ATTK, attacking_unit_HIT, attk_amnt)
wound_total = roll_to_wound(hit_total, attacking_unit_WND)
print("")

dmg_to_take = roll_to_save(wound_total, defending_unit_SAVE, attacking_unit_RND)
print("")
calculate_dmg(dmg_to_take, attacking_unit_DMG)
