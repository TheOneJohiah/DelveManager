# Witness my jank!
import awakened as aw;
import delve_Class as dc;
import skill as sk;
import item as eq;
import accolade as ac;

# Example usage
t = aw.Awakened(name='Teston Lautts',attributes = [10, 10, 200, 80, 10, 10, 10, 10], level = 25, character_class = dc.shieldwielding_defender)
t.add_experience(2000)  # Set the character's current experience
t.add_skill(sk.intrinsic_strength(), starting_level=10)
t.add_skill(sk.intrinsic_recovery(), starting_level=10)
t.add_skill(sk.intrinsic_endurance(), starting_level=10)
t.add_skill(sk.intrinsic_vigor(), starting_level=10)
t.add_skill(sk.intrinsic_focus(), starting_level=10)
t.add_skill(sk.intrinsic_clarity(), starting_level=10)
t.unlock_tier("Physicality",1)
t.unlock_tier("Physicality",2)
t.add_skill(sk.intrinsic_resistance,starting_level=10)
t.add_skill(sk.resistance_synergy,starting_level=10)
t.add_equipment(eq.Equipment("Greater Force-sheild","A powerful shield",eq.force_steel,"Offhand",20000,500,1000,99,1,[eq.Rune("Grand Force Resistance",[eq.ResistanceEnchantment("Resistance","",[100,100,0,0,1000,100,100,0],1)])]))
t.add_equipment(eq.grand_allstat_ring)
t.inventory['Ring'].runes[1].enchantments[0].attribute_buff = [0,0,920,80,0,0,0,0]
t.add_accolade(ac.skars_glorious_return,8)
t.add_accolade(ac.sphinx_riddle,200)
t.remove_accolade(ac.sphinx_riddle,195)
t.update_buffs()

t.add_skill(sk.winter,10)
t.add_skill(sk.amplify_aura(),10)
t.add_skill(sk.extend_aura(),10)

t.regen(1512)

t.cast_skill("Winter",16,["Amplify Aura","Extend Aura"])

t.printCharSheet(altCol=True)