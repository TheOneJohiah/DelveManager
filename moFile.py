import awakened as aw;
import delve_Class as dc;
import skill as sk;

mo = aw.Awakened(name='Mo',attributes = [10, 10, 10, 10, 10, 10, 10, 10], level = 0, level_cap=0)
mo.add_experience(70)
mo.update_level_cap(4)
mo.add_skill(sk.firebolt)
mo.raise_attribute(4, 10)
mo.cast_skill("Firebolt",2) #shooting goblin thing
mo.add_experience(120)
mo.update_level_cap(12)
mo.reduce_vital("SP", 50) #Whacking things with clubs and generally running around
mo.cast_skill("Firebolt",1) #shooting stonesinger
mo.add_experience(2300)
mo.update_level_cap(21)

mo.regen(9.6) #sleeping after all the chaos
mo.essence_exhange()
mo.cast_skill("Firebolt",17) #Getting firebolt to rank 2
mo.reduce_vital("SP", 100) #Exercise time
mo.regen(10) #Time spent during the day

mo.regen(14) #Morning of the third day
mo.essence_exhange()
mo.reduce_vital("SP",30) #morning workout

mo.regen(24) #Morning of the fourth day
mo.essence_exhange() #First morning after kin warning
mo.reduce_vital("SP",10) #morning workout

mo.regen(24) #Morning of the fifth day
mo.essence_exhange() #Second morning after kin warning
mo.raise_attribute(4, 20) #Focus before fighting
mo.raise_attribute(5, 6) # Clarity maxed out for level 5
mo.reduce_vital("SP",90) #Kinfight
mo.cast_skill("Firebolt",20) #Kinfight
mo.add_experience(1200)
mo.cast_skill("Firebolt",10) #Killing off some injured kin for killreq
#Get back, get given houses

mo.regen(24) #Morning of the sixth day
mo.essence_exhange() #Morning after killing kin and getting houses

mo.reduce_vital("SP",90) #Training this day
mo.cast_skill("Firebolt",10)

mo.regen(24) #Morning of the seventh day
mo.essence_exhange() #Morning of training day, got backpacks that evening

mo.add_skill(sk.smoke_burst) #Flame burst time
mo.reduce_vital("SP",100) #Training this day, mostly just hoarding mana
mo.add_vital("MP",mo.vitals[5]*0.10) #regen assuming most of this day was spent within 2 meters of Daniel's 14% winter.

mo.regen(24) #Morning of the eighth day
mo.essence_exhange() #Morning of cave investigation day, day 1 of training timelapse
print("Cave and training day")

mo.reduce_vital("SP",100) #Workout
mo.add_vital("MP",mo.vitals[5]*0.10) #regen assuming most of this day was spent within 2 meters of Daniel's 14% winter.
mo.cast_skill("Firebolt",10)
print(mo.currVitals[2])

mo.regen(24) #Morning of the ninth day
mo.essence_exhange() #2 of 7 training timelapse
print("2 of 7")

mo.reduce_vital("SP",100) #Workout
mo.add_vital("MP",mo.vitals[5]*0.20) #regen assuming most of this day was spent within range of Daniel's 30% winter.
mo.cast_skill("Firebolt",10)
print(mo.currVitals[2])

mo.regen(24) #Morning of the tenth day
mo.essence_exhange() #3 of 7 training timelapse
print("3 of 7")

mo.reduce_vital("SP",100) #Workout
mo.add_vital("MP",mo.vitals[5]*0.40) #regen assuming most of this day was spent within range of Daniel's 67% winter.
mo.cast_skill("Firebolt",10)

mo.regen(24) #Morning of the eleventh day
mo.essence_exhange() #4 of 7 training timelapse
print("4 of 7")

mo.reduce_vital("SP",100) #Workout
mo.add_vital("MP",mo.vitals[5]*0.45) #regen assuming most of this day was spent within range of Daniel's 76% winter.
mo.cast_skill("Firebolt",16)
print(mo.currVitals[2])

mo.regen(24) #Morning of the twelfth day
mo.essence_exhange() #5 of 7 training timelapse
print("5 of 7")

mo.reduce_vital("SP",100) #Workout
mo.add_vital("MP",mo.vitals[5]*0.80) #regen assuming most of this day was spent within 2 meters of Daniel's 115% winter.
mo.add_vital("MP",1000) # Mana bank, edging soulstrain
mo.cast_skill("Firebolt",129)
print(mo.currVitals[2])

mo.regen(24) #Morning of the thirteenth day
mo.essence_exhange() #6 of 7 training timelapse
print("6 of 7")

mo.reduce_vital("SP",100) #Workout
mo.add_vital("MP",mo.vitals[5]*0.85) #regen assuming most of this day was spent within range of Daniel's 120% winter.
mo.add_vital("MP",1000) # Mana bank, edging soulstrain
mo.cast_skill("Firebolt",130)
print(mo.currVitals[2])

mo.regen(24) #Morning of the fourteenth day
mo.essence_exhange() #7 of 7 training timelapse
print("7 of 7, skar evening")

mo.add_skill(sk.fire_affinity) #Unlocked with five ranks in fire evocation
mo.add_skill(sk.heat_mastery) #Unlocked with firebolt level 5
skillFiAff = mo.skills["Fire Affinity"]
skillHeMas = mo.skills["Heat Mastery"]

mo.reduce_vital("SP",100) #Workout
mo.add_vital("MP",mo.vitals[5]*0.40) #regen assuming most of this day was spent within range of Daniel's 68% winter.
mo.cast_skill("Firebolt",10)
skillFiAff.bank_exp(0.1*10*10)
skillHeMas.bank_exp(0.1*10*10)

mo.raise_attribute(4, 24) #Focus before fighting Skar
mo.regen(14) #regen before fight?
mo.add_vital("MP",333) # Mana bank, filling up for the fight
mo.reduce_vital("SP",100) #Fighting Skar
mo.cast_skill("Firebolt",30) #Fighting Skar
skillFiAff.bank_exp(0.1*30*10)
skillHeMas.bank_exp(0.1*30*10)

mo.regen(10) #Morning of the fifteenth day
mo.essence_exhange() #Morning after fighting Skar
print("Eviction day")

mo.add_vital("MP",mo.vitals[5]*1.2) #regen assuming most of this day was spent within range of Daniel's 170% winter.
mo.add_vital("MP",1000) # Mana bank, edging soulstrain

mo.reduce_vital("SP",60) #Walking
mo.cast_skill("Firebolt",160) #Training
skillFiAff.bank_exp(0.1*160*10)
skillHeMas.bank_exp(0.1*160*10)

mo.regen(24) #Morning of the sixteenth day
mo.essence_exhange() #Morning after getting kicked out

mo.update_vitals()
mo.update_free_attributes()
mo.printCharSheet(altCol= False)
print(mo.general_statistics)