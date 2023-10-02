# Witness my jank!
import awakened as aw;
import delve_Class as dc;
import skill as sk;
import item as eq;

# Example usage
t = aw.Awakened(name='Teston Lautts',attributes = [10, 10, 200, 10, 10, 10, 10, 10], level = 20, character_class = dc.shieldwielding_defender)
t.add_experience(2000)  # Set the character's current experience
t.add_skill(sk.intrinsic_clarity(), starting_level=10)
t.add_skill(sk.intrinsic_focus(), starting_level=10)
t.add_skill(sk.healing_word(), starting_level=10)
t.unlock_tier("Physicality",1)
t.unlock_tier("Physicality",2)
t.add_skill(sk.Passive("Intrinsic Resistance","Multiplies Resistances by 1 + .2*RNK",1,"Physicality",keywords=['Resistance']),starting_level=10)
t.add_skill(sk.Passive("Resistance Synergy","Allow synergistic cross-multiplication of resistances, 2.5%*RNK",2,"Physicality",keywords=['Resistance']),starting_level=10)
#t.add_equipment(eq.Equipment("Greater Force-sheild","A powerful shield",eq.force_steel,"Offhand",20000,500,1000,99,1,[eq.])
t.add_equipment(eq.grand_allstat_ring)
t.raise_attribute(3,20)
t.printCharSheet()

print(t.accolades)
print(t.used_accolade_slots)