import awakened as aw
import delve_Class as dc
import item as item
import accolade as acc
import skill as sk
from timeline import *


grace = aw.Awakened(name='Grace McGwaed', level_cap=12)
grace.add_equipment(item.Equipment("Hoodie and Jeans","Regular clothing",None,"Underwear",0,1,0,0,0,None))

def printTrees ():
    for tree in sk.AllTreeList:
        desc = ":"
        for t in range(1,5):
            if not grace.trees[tree].tiers[t].lock: desc += " T"+str(t)
        if not desc == ":": print(tree + desc)

def printPotTrees (t):
    for tree in sk.AllTreeList:
        if grace.trees[tree].tiers[t].lock and not grace.trees[tree].tiers[t-1].lock: print(f'grace.unlock_tier("{tree}",{t})')

#Day 1
print("Day 1")
grace.regen(10.4)
grace.add_experience(195)
grace.reduce_vital("HP",110)
grace.reduce_vital("SP",50)
grace.add_skill(sk.healing_word())
grace.cast_skill("Healing Word",20) #all the healing on Day 1

# Day 2
print("Day 2")
grace.regen(9.6)
grace.essence_exhange()
grace.raise_attribute(4,30) #raise Focus by 30
grace.unlock_tier("Restoration",1)
grace.cast_skill("Healing Word",4) #Healing Micah

grace.add_skill(sk.natural_intuition)
grace.add_skill(sk.chemical_intuition)

grace.regen(16)

# Day 3
print("Day 3")
grace.regen(3.6)
grace.essence_exhange()
grace.cast_skill("Healing Word",7) #Post Work-out Healing
grace.reduce_vital("SP",100)
grace.regen(20.4)

#Day 4, training
print("Day 4")
grace.regen(4)
grace.essence_exhange()
grace.cast_skill("Healing Word",7) #Post Work-out Healing
grace.reduce_vital("SP",100)
grace.regen(20)

# Day 5, training
print("Day 5")
grace.regen(6)
grace.essence_exhange()
grace.raise_attribute(5,10) #Raise Clarity
grace.add_skill(sk.cleave_fibers())
grace.cast_skill("Healing Word",7) #Post Work-out Healing
grace.reduce_vital("SP",100)
grace.regen(18)

print("Day 6")
# Day 6; KIN
grace.regen(1)
grace.essence_exhange()
grace.cast_skill("Cleave Fibers",1)
grace.add_experience(2050)
grace.add_skill(sk.congeal())
grace.raise_attribute(5,10)
grace.raise_attribute(4,5)
grace.raise_attribute(3,5)
grace.cast_skill("Cleave Fibers",30)
grace.regen(2)
grace.cast_skill("Cleave Fibers",19)
grace.regen(4)
grace.cast_skill("Cleave Fibers",10)
grace.regen(0.5)
grace.cast_skill("Congeal",3)
#Level 8 Dire-Kin
grace.reduce_vital("HP",20)
grace.reduce_vital("HP",27)
grace.cast_skill("Cleave Fibers",1)
grace.reduce_vital("HP",46)
grace.reduce_vital("HP",3)
grace.reduce_vital("HP",40)
grace.reduce_vital("HP",20)

grace.regen(16.5)

#Day 7
print("Day 7")
grace.regen(8)
grace.essence_exhange()
grace.cast_skill("Healing Word",15)
grace.regen(3)
grace.cast_skill("Cleave Fibers",5)

grace.unlock_tier("Natureworking",1)
grace.unlock_tier("Chemistry",1)

grace.add_skill(sk.purge_poison())
grace.cast_skill("Purge Poison",1)
grace.regen(13)

#Day 8; Leaving once again.
print("Day 8")
grace.regen(9)
grace.essence_exhange()
#...or back, I suppose
grace.regen(15)

#Day 9; All the way to day 14!
print("Day 9")
grace.regen(24)
grace.essence_exhange()
#print(grace.get_skill_power("Healing Word") * 15)
grace.cast_skill("Cleave Fibers",5)
grace.cast_skill("Healing Word",15)
grace.cast_skill("Congeal",9)
#10
print("Day 10")
grace.regen(24)
grace.essence_exhange()
grace.unlock_tier("Restoration",2)
grace.cast_skill("Cleave Fibers",5)
grace.cast_skill("Healing Word",15)
grace.cast_skill("Congeal",4)
#11
print("Day 11")
grace.regen(24)
grace.essence_exhange()
grace.cast_skill("Cleave Fibers",5)
grace.cast_skill("Healing Word",15)
grace.cast_skill("Congeal",3)
#12
print("Day 12")
grace.regen(24)
grace.essence_exhange()
grace.cast_skill("Cleave Fibers",5)
grace.cast_skill("Healing Word",15)
grace.cast_skill("Congeal",3)
#13
print("Day 13")
grace.regen(24)
grace.essence_exhange()
grace.cast_skill("Cleave Fibers",5)
grace.cast_skill("Healing Word",15)
grace.cast_skill("Congeal",3)

#14
print("Day 14")
grace.regen(24)
grace.essence_exhange()
grace.cast_skill("Cleave Fibers",5)
grace.cast_skill("Healing Word",15)
grace.cast_skill("Healing Word",10) #Healing Fiig

#15 Leaving Hillrod
print("Day 15")
grace.regen(8)
grace.essence_exhange()
grace.regen(2)
grace.cast_skill("Healing Word",2) #Healing Micah
grace.cast_skill("Cleave Fibers",32) #Cutting down trees
grace.regen(14)
grace.cast_skill("Cleave Fibers",8)

#16 Training week 3
print("Day 16")
grace.regen(8)
grace.essence_exhange()
grace.unlock_tier("Natureworking",2)
grace.cast_skill("Cleave Fibers",1)
grace.cast_skill("Congeal",3)
grace.cast_skill("Purge Poison",7)
grace.regen(16)

#17 Training 3.2
print("Day 17")
grace.regen(24)
grace.essence_exhange()
grace.cast_skill("Cleave Fibers",1)
grace.cast_skill("Congeal",2)
grace.cast_skill("Purge Poison",15)

#18 Training 3.3
print("Day 18")
grace.regen(24)
grace.essence_exhange()
grace.cast_skill("Cleave Fibers",1)
grace.cast_skill("Congeal",3)
grace.cast_skill("Purge Poison",15)
grace.cast_skill("Healing Word",3)

#19 Training 3.4
print("Day 19")
grace.regen(24)
grace.essence_exhange()
grace.cast_skill("Cleave Fibers",1)
grace.cast_skill("Congeal",2)
grace.cast_skill("Purge Poison",15)

#20 Training 3.5
print("Day 20")
grace.regen(24)
grace.essence_exhange()
grace.unlock_tier("Alchemy",1)
grace.cast_skill("Cleave Fibers",1)
grace.cast_skill("Congeal",1)
grace.cast_skill("Purge Poison",15)

#21 Training 3.6
print("Day 21")
grace.regen(24)
grace.essence_exhange()
grace.unlock_tier("Chemistry",2)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",1)
grace.cast_skill("Purge Poison",15)

#22 Training 3.7
print("Day 22")
grace.regen(24)
grace.essence_exhange()
grace.unlock_tier("Runecrafting",1)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",1)
grace.cast_skill("Purge Poison",14)
grace.bank_skill_exp("Natural Intuition",400)
grace.bank_skill_exp("Chemical Intuition",4000)

#23 Diggy Diggy Hole
print("Day 23")
grace.regen(8)
grace.essence_exhange()
grace.character_class.attribute_effect[5] = 510 #Winter
grace.update_vitals()
grace.regen(14)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",59)
grace.regen(2)
grace.cast_skill("Cleave Fibers",9)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()

#24 Depths; Quillbears!
print("Day 24")
grace.regen(8)
grace.essence_exhange()
grace.unlock_tier("Alchemy",2)
grace.add_experience(42)
grace.character_class.attribute_effect[5] = 520 #Winter
grace.update_vitals()
grace.cast_skill("Cleave Fibers",5)
grace.regen(14)
grace.cast_skill("Cleave Fibers",45)
grace.regen(2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",6)
grace.bank_skill_exp("Natural Intuition",2500)
grace.bank_skill_exp("Chemical Intuition",4500)

#25 Day after! Quillbears two.
print("Day 25")
grace.regen(8)
grace.essence_exhange()
grace.unlock_tier("Magical Utility",1)
grace.unlock_tier("Armor Crafting",1)
grace.unlock_tier("Weapon Crafting",1)
grace.unlock_tier("Artificing",1)
grace.unlock_tier("Arcane Shifter",1)
grace.add_accolade(acc.flamewillow_grove,5)
grace.update_attributes()
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",20)
grace.regen(14)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",36)
grace.regen(2)
grace.cast_skill("Cleave Fibers",5)
grace.cast_skill("Congeal",1)

#26 Day after! to Day 50 :O
print("Day 26 - 1/25")
grace.regen(8)
grace.character_class.attribute_effect[3] = 52
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Runecrafting",2)
grace.bank_skill_exp("Chemical Intuition",6000)
grace.bank_skill_exp("Natural Intuition",20000)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",17)
grace.regen(7.4)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",3)
grace.regen(7.4)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",3)
grace.regen(1.2)

#27
print("Day 27 - 2/25")
grace.character_class.attribute_effect[3] = 0
grace.character_class.attribute_effect[5] = 520
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[3] = 104
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Equipment Use",1)
grace.unlock_tier("Heavy Armor",1)
grace.unlock_tier("Light Armor",1)
grace.unlock_tier("Melee Weapons",1)
grace.unlock_tier("Hurling",1)
grace.unlock_tier("Survivalist Utility",1)

grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",26)
grace.regen(3.7)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",1)
grace.regen(3.7)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",2)
grace.regen(3.7)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",1)
grace.regen(3.7)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",2)
grace.regen(1.2)

#28
print("Day 28 - 3/25")
grace.character_class.attribute_effect[5] = 520
grace.character_class.attribute_effect[3] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[3] = 156
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Artificing",2)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",21)
grace.regen(2.9)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",1)
grace.regen(2.9)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",1)
grace.regen(2.9)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",1)
grace.regen(2.9)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",1)
grace.regen(2.9)
grace.cast_skill("Congeal",2)
grace.cast_skill("Cleave Fibers",2)
grace.regen(1.5)

#29
print("Day 29 - 4/25")
grace.character_class.attribute_effect[5] = 520
grace.character_class.attribute_effect[3] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[3] = 208
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Armor Crafting",2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",21)
grace.regen(.5)
grace.cast_skill("Congeal",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(.5)

#30
print("Day 30 - 5/25")
grace.character_class.attribute_effect[5] = 520
grace.character_class.attribute_effect[3] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[3] = 208
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Magical Utility",2)

grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",18)
grace.regen(.5)
grace.cast_skill("Congeal",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",1)
grace.regen(.5)

#31
print("Day 31 - 6/25")
grace.character_class.attribute_effect[5] = 560
grace.character_class.attribute_effect[3] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[1] = 56
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Equipment Use",2)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",68)
grace.regen(1.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",2)
grace.regen(4.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(4.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",5)
grace.regen(4.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(1)
grace.cast_skill("Healing Word",1)

#32
print("Day 32 - 7/25")
grace.character_class.attribute_effect[5] = 560
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[1] = 112
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Arcane Mysteries",1)
grace.unlock_tier("Arcane Metamagic",1)
grace.unlock_tier("Arcane Utility",1)
grace.unlock_tier("Elemental Enhancement",1)
grace.unlock_tier("Elemental Inhibition",1)
grace.unlock_tier("Geoevocation",1)
grace.unlock_tier("Earth Manipulation",1)
grace.unlock_tier("Hydroevocation",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",66)
grace.regen(3)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",4)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",7)
grace.regen(2.6)
grace.cast_skill("Healing Word",3)

#33
print("Day 33 - 8/25")
grace.character_class.attribute_effect[5] = 560
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[1] = 168
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Water Manipulation",1)
grace.unlock_tier("Aeroevocation",1)
grace.unlock_tier("Air Manipulation",1)
grace.unlock_tier("Psionics",1)
grace.unlock_tier("Beams",1)
grace.unlock_tier("Threat Attraction",1)
grace.unlock_tier("Shieldwielding",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",66)
grace.regen(3)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",4)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",7)
grace.regen(2.6)
grace.cast_skill("Healing Word",3)

#34
print("Day 34 - 9/25")
grace.character_class.attribute_effect[5] = 600
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[1] = 240
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Physical Passive",1)
grace.unlock_tier("Physical Utility",1)
grace.unlock_tier("Physicality",1)
grace.unlock_tier("Staff Combat",1)
grace.unlock_tier("Swordplay",1)
grace.unlock_tier("Fencing",1)
grace.unlock_tier("Dagger Combat",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",70)
grace.regen(3)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",4)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",7)
grace.regen(2.6)
grace.cast_skill("Healing Word",3)

#35
print("Day 35 - 10/25")
grace.character_class.attribute_effect[5] = 600
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[1] = 240
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Sharpshooting",1)
grace.unlock_tier("Tracking",1)
grace.unlock_tier("Aura Metamagic",1)
grace.unlock_tier("Offensive Auras",1)
grace.unlock_tier("Defensive Auras",1)
grace.unlock_tier("Utility Auras",1)
grace.unlock_tier("Elemental Archer",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",70)
grace.regen(3)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",4)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",7)
grace.regen(2.6)
grace.cast_skill("Healing Word",3)

#35
print("Day 35 - 10/25")
grace.character_class.attribute_effect[5] = 600
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[1] = 240
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Evocation Metamagic",1)
grace.unlock_tier("Fire Evocation",1)
grace.unlock_tier("Ice Evocation",1)
grace.unlock_tier("Monster Taming",1)
grace.unlock_tier("Divination",1)
grace.unlock_tier("Defensive Constructs",1)
grace.unlock_tier("Force Metamagic",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",70)
grace.regen(3)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",4)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",7)
grace.regen(2.6)
grace.cast_skill("Healing Word",3)

#36
print("Day 36 - 11/25")
grace.character_class.attribute_effect[5] = 618
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Blood Magic",1)
grace.unlock_tier("Stoneworking",1)
grace.unlock_tier("Metalworking",1)
grace.unlock_tier("Tree 56",1)
grace.unlock_tier("Tree 57",1)
grace.unlock_tier("Tree 58",1)
grace.unlock_tier("Tree 59",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",72)
grace.regen(3)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",4)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",7)
grace.regen(2.6)
grace.cast_skill("Healing Word",3)

#37
print("Day 37 - 12/25")
grace.character_class.attribute_effect[5] = 715
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Tree 60",1)
grace.unlock_tier("Tree 61",1)
grace.unlock_tier("Tree 62",1)
grace.unlock_tier("Tree 63",1)
grace.unlock_tier("Tree 64",1)
grace.unlock_tier("Tree 65",1)
grace.unlock_tier("Tree 66",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",81)
grace.regen(3)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",4)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",7)
grace.regen(2.6)
grace.cast_skill("Healing Word",3)

#38
print("Day 38 - 13/25")
grace.character_class.attribute_effect[5] = 758
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Tree 67",1)
grace.unlock_tier("Tree 68",1)
grace.unlock_tier("Tree 69",1)
grace.unlock_tier("Tree 70",1)
grace.unlock_tier("Tree 71",1)
grace.unlock_tier("Tree 72",1)
grace.unlock_tier("Tree 73",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",86)
grace.regen(3)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",4)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(5.2)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",7)
grace.regen(2.6)
grace.cast_skill("Healing Word",3)

#39
print("Day 39 - 14/25")
grace.character_class.attribute_effect[5] = 783
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Tree 74",1)
grace.unlock_tier("Tree 75",1)
grace.unlock_tier("Tree 76",1)
grace.unlock_tier("Tree 77",1)
grace.unlock_tier("Tree 78",1)
grace.unlock_tier("Tree 79",1)
grace.unlock_tier("Tree 80",1)
grace.unlock_tier("Tree 81",1)
grace.unlock_tier("Tree 82",1)
grace.unlock_tier("Tree 83",1)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",88)
grace.regen(4.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",6)
grace.regen(6)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",8)
grace.regen(5.5)
grace.cast_skill("Healing Word",6)

#40
print("Day 40 - 15/25")
grace.character_class.attribute_effect[5] = 804
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Tree 84",1)
grace.unlock_tier("Tree 85",1)
grace.unlock_tier("Tree 86",1)
grace.unlock_tier("Tree 87",1)
grace.unlock_tier("Tree 88",1)
grace.unlock_tier("Tree 89",1)
grace.unlock_tier("Tree 90",1)
grace.unlock_tier("Tree 91",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",90)
grace.regen(4.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",5)
grace.regen(6)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",8)
grace.regen(5.5)
grace.cast_skill("Healing Word",7)

#41; Back to winter!!!
print("Day 41 - 16/25")
grace.character_class.attribute_effect[5] = 810
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 810
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Tree 92",1)
grace.unlock_tier("Tree 93",1)
grace.unlock_tier("Tree 94",1)
grace.unlock_tier("Tree 95",1)
grace.unlock_tier("Tree 96",1)
grace.unlock_tier("Tree 97",1)
grace.unlock_tier("Tree 98",1)
grace.unlock_tier("Tree 99",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",90)
grace.regen(4.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",51)
grace.regen(6)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",68)
grace.regen(5.5)
grace.cast_skill("Healing Word",63)

#42
print("Day 42 - 17/25")
grace.character_class.attribute_effect[5] = 810
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 810
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Tree 100",1)
grace.unlock_tier("Tree 101",1)
grace.unlock_tier("Tree 102",1)
grace.unlock_tier("Tree 103",1)
grace.unlock_tier("Tree 104",1)
grace.unlock_tier("Tree 105",1)
grace.unlock_tier("Tree 106",1)
grace.unlock_tier("Tree 107",1)
grace.unlock_tier("Tree 108",1)
grace.unlock_tier("Tree 109",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",90)
grace.regen(4.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",51)
grace.regen(6)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",68)
grace.regen(5.5)
grace.cast_skill("Healing Word",63)

#43 WHAT THE FUCK DANIEL
print("Day 43 - 18/25")
grace.character_class.attribute_effect[5] = 810
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 1984
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Tree 110",1)
grace.unlock_tier("Tree 111",1)
grace.unlock_tier("Tree 112",1)
grace.unlock_tier("Tree 113",1)
grace.unlock_tier("Tree 114",1)
grace.unlock_tier("Tree 115",1)
grace.unlock_tier("Tree 116",1)
grace.unlock_tier("Tree 117",1)
grace.unlock_tier("Tree 118",1)
grace.unlock_tier("Tree 119",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",90)
grace.regen(3.5)
grace.cast_skill("Healing Word",90)
grace.regen(1)
grace.cast_skill("Congeal",1)
grace.regen(2.5)
grace.cast_skill("Healing Word",90)
grace.regen(3.5)
grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",90)
grace.regen(3.5)
grace.cast_skill("Healing Word",90)
grace.regen(2)
grace.cast_skill("Healing Word",52)

#44
print("Day 44 - 19/25")
grace.character_class.attribute_effect[5] = 810
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 5490
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Tree 120",1)
grace.unlock_tier("Tree 121",1)
grace.unlock_tier("Tree 122",1)
grace.unlock_tier("Tree 123",1)
grace.unlock_tier("Tree 124",1)
grace.unlock_tier("Tree 125",1)
grace.unlock_tier("Tree 126",1)
grace.unlock_tier("Tree 127",1)
grace.unlock_tier("Tree 128",1)
grace.unlock_tier("Tree 129",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Healing Word",90)
grace.regen(1.3)
grace.cast_skill("Healing Word",90)
grace.regen(1.3)
grace.cast_skill("Healing Word",90)
grace.regen(1.3)
grace.cast_skill("Healing Word",52) #Max Healing Word at this point
grace.cast_skill("Cleave Fibers",10)
grace.regen(0.6) #4.5
grace.cast_skill("Congeal",1)
grace.regen(0.7)
grace.cast_skill("Cleave Fibers",25)
grace.regen(1.3)
grace.cast_skill("Cleave Fibers",25)
grace.regen(1.3)
grace.cast_skill("Cleave Fibers",25)
grace.regen(1.3)
grace.cast_skill("Cleave Fibers",25)
grace.regen(1.3)
grace.cast_skill("Cleave Fibers",25)
grace.regen(0.1) #10.5
grace.cast_skill("Congeal",1)
grace.regen(1.2)
grace.cast_skill("Cleave Fibers",25)
grace.regen(1.3)
grace.cast_skill("Cleave Fibers",25)
grace.regen(1.3)
grace.cast_skill("Cleave Fibers",25)
grace.regen(1.3)
grace.cast_skill("Cleave Fibers",25)
grace.regen(0.4)
grace.cast_skill("Cleave Fibers",8)

#45
print("Day 45 - 20/25")
grace.character_class.attribute_effect[5] = 810
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 6756
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Tree 130",1)
grace.unlock_tier("Tree 131",1)
grace.unlock_tier("Tree 132",1)
grace.unlock_tier("Tree 133",1)
grace.unlock_tier("Tree 134",1)
grace.unlock_tier("Tree 135",1)
grace.unlock_tier("Tree 136",1)
grace.unlock_tier("Tree 137",1)
grace.unlock_tier("Tree 138",1)
grace.unlock_tier("Tree 139",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(0.1) #4.5
grace.cast_skill("Congeal",1)
grace.regen(1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(0.6) #10.5
grace.cast_skill("Congeal",1)
grace.regen(0.5)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(1.1)
grace.cast_skill("Cleave Fibers",22)
grace.regen(0.6)
grace.cast_skill("Cleave Fibers",13)

#46
print("Day 46 - 21/25")
grace.character_class.attribute_effect[5] = 810
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 7943
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Tree 140",1)
grace.unlock_tier("Tree 141",1)
grace.unlock_tier("Tree 142",1)
grace.unlock_tier("Tree 143",1)
grace.unlock_tier("Tree 144",1)

grace.cast_skill("Congeal",1)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9) #4.5
grace.cast_skill("Purge Poison",45)
grace.cast_skill("Congeal",1)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.6) #10.5
grace.cast_skill("Congeal",1)
grace.regen(0.3)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.9)
grace.cast_skill("Purge Poison",45)
grace.regen(0.7)
grace.cast_skill("Purge Poison",35)

#47
print("Day 47 - 22/25")
grace.character_class.attribute_effect[5] = 810
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 9266
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Divination",2)

grace.cast_skill("Congeal",1)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.5) #4.5
grace.cast_skill("Congeal",1)
grace.regen(0.3)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.1) #10.5
grace.cast_skill("Congeal",1)
grace.regen(0.7)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)

#48
print("Day 48 - 23/25")
grace.character_class.attribute_effect[5] = 810
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 9266
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Weapon Crafting",2)

grace.cast_skill("Congeal",1)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.5) #4.5
grace.cast_skill("Congeal",1)
grace.regen(0.3)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.1) #10.5
grace.cast_skill("Congeal",1)
grace.regen(0.7)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)
grace.regen(0.8)
grace.cast_skill("Purge Poison",45)

#49 ask to swap to Spring again
print("Day 49 - 24/25")
grace.character_class.attribute_effect[5] = 810
grace.character_class.attribute_effect[1] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[3] = 3433
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.unlock_tier("Stoneworking",2)

grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)
grace.regen(0.2)
grace.cast_skill("Congeal",1)

#50
print("Day 50 - 25/25")
grace.character_class.attribute_effect[5] = 810
grace.character_class.attribute_effect[3] = 0
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.set_class(dc.life_worker)
grace.bank_skill_exp("Natural Intuition",1)
grace.skills["Natural Intuition"].xp -= 1
grace.essence_exhange()
#Just resting for the day
grace.regen(16)

#51; Amor, then Depths
print("Day 51")
grace.character_class.attribute_effect[5] = 828
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.regen(2)
grace.cast_skill("Healing Word",1) #Heal Fiig
grace.cast_skill("Cleave Fibers",1) #Fixing the Shield
#Harvesting
grace.regen(4)
grace.cast_skill("Cleave Fibers",17)
grace.currVitals[2] += 890
grace.cast_skill("Cleave Fibers",18)
grace.currVitals[2] += 900
grace.cast_skill("Cleave Fibers",18)
grace.currVitals[2] += 900
grace.cast_skill("Cleave Fibers",18)
grace.currVitals[2] += 900
grace.cast_skill("Cleave Fibers",18)
grace.currVitals[2] += 900
grace.cast_skill("Cleave Fibers",18)
grace.currVitals[2] += 900
grace.cast_skill("Cleave Fibers",18)
grace.regen(10)

#52 To Dudiro
print("Day 52")
grace.character_class.attribute_effect[5] = 828
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.raise_attribute(4,10)
grace.add_skill(sk.runic_intuition)
grace.cast_skill("Healing Word",90)
grace.regen(16)

#53 To Dudiro 2
print("Day 53")
grace.character_class.attribute_effect[5] = 828
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.raise_attribute(4,10)
grace.add_skill(sk.runes_of_defense())
grace.cast_skill("Healing Word",106)
grace.regen(16)

#54 To Dudiro 3
print("Day 54")
grace.character_class.attribute_effect[5] = 828
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.cast_skill("Healing Word",107)
grace.regen(16)

#55 Dudiro!
print("Day 55")
grace.character_class.attribute_effect[5] = 828
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.regen(4)
tel = 766
tel -= 150
grace.regen(12)
tel -= 22 #Bunk-beds

#56 Dudiro 2; Cadabra, to back to the Skar
print("Day 56")
#grace.character_class.attribute_effect[5] = 828 #Not today
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
tel -= 500 #Highway robbery @ Cadabra
heat_crysts = 15
arcane_crysts = 15
grace.cast_skill("Healing Word",130)
grace.regen(16)
grace.cast_skill("Healing Word",20)

#57 To Skar
print("Day 57")
grace.character_class.attribute_effect[5] = 834
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.cast_skill("Healing Word",93)
grace.regen(16)
grace.cast_skill("Healing Word",20)

#58 To Skar
print("Day 58")
grace.character_class.attribute_effect[5] = 834
grace.update_vitals()
grace.regen(8)
grace.character_class.attribute_effect[5] = 0
grace.update_vitals()
grace.essence_exhange()
grace.cast_skill("Healing Word",93)
grace.regen(16)
grace.cast_skill("Healing Word",20)

#59 Skar!
print("Day 59")
grace.regen(8,[0,0,834])
grace.essence_exhange()
grace.attributes[4][2] += 10 #Manually adding because fuck it
grace.update_attributes()
#grace.add_equipment(item.Item("Endurance "))
grace.regen(6)
grace.cast_skill("Cleave Fibers",6)
tel += 550
heat_crysts += 22
#Creating Heat Resist Leather
grace.cast_skill("Cleave Fibers",12)
tel -= 8 
heat_crysts -= 4
grace.regen(10)

#60 More Crafting!
print("Day 60")
grace.regen(8,[0,0,834])
grace.essence_exhange()
grace.raise_attribute(4,10)
grace.add_skill(sk.steady_scribing())
#grace.bank_skill_exp("Steady Scribing",700)
grace.regen(9)
tel += 79
heat_crysts += 1
#Unwashed Archer - Skar Ogwa
grace.cast_skill("Cleave Fibers",1)
grace.cast_skill("Healing Word",1)
#Lair!
grace.cast_skill("Healing Word",1) #Healing Fiig
grace.update_level_cap(16)
tel += 8
heat_crysts += 3
grace.regen(3)
grace.cast_skill("Cleave Fibers",1)
grace.regen(4)

#61 To Dudiro, once more
print("Day 61")
grace.regen(5)
grace.regen(16,[0,380,0])
grace.essence_exhange()
grace.cast_skill("Healing Word",100)
grace.regen(3,[0,0,834])

#62
print("Day 62")
grace.regen(8,[0,0,834])
grace.essence_exhange()
grace.regen(16,[0,380,0])
grace.cast_skill("Healing Word",150)

#63; At Dudiro
print("Day 63")
grace.regen(8,[0,0,834])
grace.essence_exhange()
tel -= 600
tel += 120
grace.regen(16)

#64
print("Day 64")
grace.regen(8,[0,0,834])
grace.essence_exhange()
grace.regen(16)

#65 - Attack rebuffed, to Quill caves
print("Day 65")
grace.regen(8,[0,0,834])
grace.essence_exhange()
grace.regen(16,[0,380,0])

#66
print("Day 66")
grace.regen(8,[0,0,834])
grace.essence_exhange()
grace.regen(16,[0,380,0])
grace.cast_skill("Healing Word",150)

#67
print("Day 67")
grace.regen(8,[0,0,834])
grace.essence_exhange()
grace.regen(16,[0,380,0])
grace.cast_skill("Healing Word",113)

#68 - Quillcaves
print("Day 68")
grace.regen(8,[0,0,834])
grace.essence_exhange()
grace.regen(16,[0,380,0])

# To day 96!
def test():
    print("XP:",grace.experience)
    for sk in ["Healing Word","Cleave Fibers","Purge Poison","Congeal","Dissolve","Tissue Scan","Alchemic Intuition"]:
        print(sk,": R",grace.get_skill_rank(sk),"XP:",grace.get_skill_xp(sk))
    if grace.level>=15 and grace.free_attributes>0: grace.raise_attribute(0,10)

grace.train_days(28,
                 ["Purge Poison","Congeal"],
                 [0,38,750],
                 sleepmod=[0,0,834],
                 nextskills=[
                     sk.dissolve(),
                     sk.tissue_scan,
                     sk.alchemic_intuition,
                     sk.runes_of_living_enhancement(),
                     sk.runes_of_item_enhancement(),
                     sk.runes_of_complexity(),
                     #sk.stabilize
                 ],
                 stats=[0,0,0,0,50,10],
                 cb=test
                )
tel += 498

#Day 97
print("Day 97")
grace.regen(8,[0,0,834])
grace.essence_exhange()

timeInt = Moment('0936-06-03-12:00:00:000').to(grace.date)
#printPotTrees(3)
print("\nTel:",tel,
      "\nHeat Crysts:",heat_crysts,
      "\nArcane Crysts:",arcane_crysts,
      "\nDay:",grace.date.path(),
      "\nDay:",grace.date.datetime(),
      "\nHours:",timeInt.length.in_hours(),
      "\nDays:",int(timeInt.length.in_days()+.5),
)
grace.printCharSheet(altCol= True)

'''
print(grace.experience)

grace.unlock_tier("Physical Passive",2)
grace.unlock_tier("Physical Utility",2)
grace.unlock_tier("Physicality",2)
grace.unlock_tier("Melee Weapons",2)
grace.unlock_tier("Heavy Armor",2)
grace.unlock_tier("Light Armor",2)
grace.unlock_tier("Shieldwielding",2)
grace.unlock_tier("Staff Combat",2)
grace.unlock_tier("Swordplay",2)
grace.unlock_tier("Fencing",2)
grace.unlock_tier("Dagger Combat",2)
grace.unlock_tier("Hurling",2)
grace.unlock_tier("Sharpshooting",2)
grace.unlock_tier("Tracking",2)
grace.unlock_tier("Threat Attraction",2)
grace.unlock_tier("Aura Metamagic",2)
grace.unlock_tier("Offensive Auras",2)
grace.unlock_tier("Defensive Auras",2)
grace.unlock_tier("Utility Auras",2)
grace.unlock_tier("Elemental Archer",2)
grace.unlock_tier("Evocation Metamagic",2)
grace.unlock_tier("Fire Evocation",2)
grace.unlock_tier("Ice Evocation",2)
grace.unlock_tier("Geoevocation",2)
grace.unlock_tier("Hydroevocation",2)
grace.unlock_tier("Aeroevocation",2)
grace.unlock_tier("Earth Manipulation",2)
grace.unlock_tier("Water Manipulation",2)
grace.unlock_tier("Air Manipulation",2)
grace.unlock_tier("Arcane Metamagic",2)
grace.unlock_tier("Arcane Mysteries",2)
grace.unlock_tier("Arcane Utility",2)
grace.unlock_tier("Arcane Shifter",2)
grace.unlock_tier("Elemental Enhancement",2)
grace.unlock_tier("Elemental Inhibition",2)
grace.unlock_tier("Psionics",2)
grace.unlock_tier("Beams",2)
grace.unlock_tier("Survivalist Utility",2)
grace.unlock_tier("Monster Taming",2)
grace.unlock_tier("Defensive Constructs",2)
grace.unlock_tier("Force Metamagic",2)
grace.unlock_tier("Blood Magic",2)
grace.unlock_tier("Tree 56",2)
grace.unlock_tier("Tree 57",2)
grace.unlock_tier("Tree 58",2)
grace.unlock_tier("Tree 59",2)
grace.unlock_tier("Tree 60",2)
grace.unlock_tier("Tree 61",2)
grace.unlock_tier("Tree 62",2)
grace.unlock_tier("Tree 63",2)
grace.unlock_tier("Tree 64",2)
grace.unlock_tier("Tree 65",2)
grace.unlock_tier("Tree 66",2)
grace.unlock_tier("Tree 67",2)
grace.unlock_tier("Tree 68",2)
grace.unlock_tier("Tree 69",2)
grace.unlock_tier("Tree 70",2)
grace.unlock_tier("Tree 71",2)
grace.unlock_tier("Tree 72",2)
grace.unlock_tier("Tree 73",2)
grace.unlock_tier("Tree 74",2)
grace.unlock_tier("Tree 75",2)
grace.unlock_tier("Tree 76",2)
grace.unlock_tier("Tree 77",2)
grace.unlock_tier("Tree 78",2)
grace.unlock_tier("Tree 79",2)
grace.unlock_tier("Tree 80",2)
grace.unlock_tier("Tree 81",2)
grace.unlock_tier("Tree 82",2)
grace.unlock_tier("Tree 83",2)
grace.unlock_tier("Tree 84",2)
grace.unlock_tier("Tree 85",2)
grace.unlock_tier("Tree 86",2)
grace.unlock_tier("Tree 87",2)
grace.unlock_tier("Tree 88",2)
grace.unlock_tier("Tree 89",2)
grace.unlock_tier("Tree 90",2)
grace.unlock_tier("Tree 91",2)
grace.unlock_tier("Tree 92",2)
grace.unlock_tier("Tree 93",2)
grace.unlock_tier("Tree 94",2)
grace.unlock_tier("Tree 95",2)
grace.unlock_tier("Tree 96",2)
grace.unlock_tier("Tree 97",2)
grace.unlock_tier("Tree 98",2)
grace.unlock_tier("Tree 99",2)
grace.unlock_tier("Tree 100",2)
grace.unlock_tier("Tree 101",2)
grace.unlock_tier("Tree 102",2)
grace.unlock_tier("Tree 103",2)
grace.unlock_tier("Tree 104",2)
grace.unlock_tier("Tree 105",2)
grace.unlock_tier("Tree 106",2)
grace.unlock_tier("Tree 107",2)
grace.unlock_tier("Tree 108",2)
grace.unlock_tier("Tree 109",2)
grace.unlock_tier("Tree 110",2)
grace.unlock_tier("Tree 111",2)
grace.unlock_tier("Tree 112",2)
grace.unlock_tier("Tree 113",2)
grace.unlock_tier("Tree 114",2)
grace.unlock_tier("Tree 115",2)
grace.unlock_tier("Tree 116",2)
grace.unlock_tier("Tree 117",2)
grace.unlock_tier("Tree 118",2)
grace.unlock_tier("Tree 119",2)
grace.unlock_tier("Tree 120",2)
grace.unlock_tier("Tree 121",2)
grace.unlock_tier("Tree 122",2)
grace.unlock_tier("Tree 123",2)
grace.unlock_tier("Tree 124",2)
grace.unlock_tier("Tree 125",2)
grace.unlock_tier("Tree 126",2)
grace.unlock_tier("Tree 127",2)
grace.unlock_tier("Tree 128",2)
grace.unlock_tier("Tree 129",2)
grace.unlock_tier("Tree 130",2)
grace.unlock_tier("Tree 131",2)
grace.unlock_tier("Tree 132",2)
grace.unlock_tier("Tree 133",2)
grace.unlock_tier("Tree 134",2)
grace.unlock_tier("Tree 135",2)
grace.unlock_tier("Tree 136",2)
grace.unlock_tier("Tree 137",2)
grace.unlock_tier("Tree 138",2)
grace.unlock_tier("Tree 139",2)
grace.unlock_tier("Tree 140",2)
grace.unlock_tier("Tree 141",2)
grace.unlock_tier("Tree 142",2)
grace.unlock_tier("Tree 143",2)
grace.unlock_tier("Tree 144",2)
'''