import pickle

# Witness my jank!
import awakened as aw;
import delve_Class as dc;
import skill as sk;
import item as eq;
import accolade as ac;

# Example usage
t = aw.Awakened(name='Teston Lautts',attributes = [10, 10, 200, 80, 10, 10, 10, 10], level = 25, character_class = dc.shieldwielding_defender)
v = aw.Awakened(name="Invess T'gatin",level=20,character_class=dc.dynamo)
h = aw.Awakened(name="Eg'zpe Rym-Ant",level=12,character_class=dc.geomancer)

t.add_experience(4400)  # Set the character's current experience

t.add_skill(sk.intrinsic_strength(), starting_level=10)
t.add_skill(sk.intrinsic_recovery(), starting_level=10)
t.add_skill(sk.intrinsic_endurance(), starting_level=10)
t.add_skill(sk.intrinsic_vigor(), starting_level=10)
t.add_skill(sk.intrinsic_focus(), starting_level=10)
t.add_skill(sk.intrinsic_clarity(), starting_level=10)
t.unlock_tier("Physicality",1)
t.unlock_tier("Physicality",2)
t.unlock_tier("Physical Passives",1)
t.unlock_tier("Physical Passives",2)
t.add_skill(sk.intrinsic_resistance,starting_level=10)
t.add_skill(sk.resistance_synergy,starting_level=10)
t.add_equipment(eq.Equipment("Greater Force-sheild","A powerful shield",eq.force_steel,"Offhand",20000,500,1000,99,1,[eq.Rune("Grand Force Resistance",[eq.ResistanceEnchantment("Resistance","",[100,100,0,0,1000,100,100,0],1)])]))
t.add_equipment(eq.grand_allstat_ring)
t.inventory['Ring'].runes[1].enchantments[0].attribute_buff = [0,0,920,80,0,0,0,0]
t.add_accolade(ac.skars_glorious_return,8)
t.add_accolade(ac.sphinx_riddle,200)
t.remove_accolade(ac.sphinx_riddle,195)
t.update_buffs()

v.add_skill(sk.winter,1)
v.add_skill(sk.amplify_aura(),1)
v.add_skill(sk.extend_aura(),1)

t.regen(1512)

v.raise_attribute(5,200)
v.cast_skill("Winter",16,["Amplify Aura","Extend Aura"])
v.essence_exhange()

'''
print("T:",t.attributes[1],t.attributes[2],t.vitals)
print("V:",v.attributes[1],v.attributes[2],v.vitals)
print("H:",h.attributes[1],h.attributes[2],h.vitals)
t.printCharSheet(altCol=True)
v.printCharSheet(altCol=True)
h.printCharSheet(altCol=True)

## Pickling test
db = {}
db['teston'] = t
db['invess'] = v

dbfile = open('./saves/campaign1.pk1','ab')
pickle.dump(db, dbfile)                    
dbfile.close()

## For loading
dbfile = open('./saves/campaign1.pk1','rb')
db = pickle.load(dbfile)
for keys in db:
    print(keys, '=>', db[keys])
dbfile.close()'''

t.jsonCharSheet()