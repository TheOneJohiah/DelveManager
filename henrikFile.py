import awakened as aw;
import delve_Class as dc;
import skill as sk;

henrik = aw.Awakened(name='Henrik',attributes = [10, 10, 10, 10, 10, 10, 10, 10], level = 0, level_cap=12)
henrik.add_experience(70)
henrik.update_level_cap(4)
henrik.add_experience(120)
henrik.update_level_cap(12)
henrik.reduce_vital("SP", 110) #Whacking things with clubs and generally running around
henrik.add_experience(700)
henrik.update_level_cap(21)

henrik.regen(9.6) #sleeping after all the chaos
henrik.essence_exhange()
henrik.raise_attribute(4, 50)
henrik.add_skill(sk.fire_arrow)
henrik.add_skill(sk.intrinsic_clarity)
henrik.add_skill(sk.intrinsic_focus)
henrik.add_skill(sk.drilling_shot)
henrik.add_skill(sk.concussive_blows)

henrik.cast_skill("Fire Arrow",10) #training time
henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(10) #Time spent during the day

henrik.cast_skill("Fire Arrow",10) #training time
henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(14) #Morning of the third day
henrik.essence_exhange()

henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(24) #Morning of the fourth day
henrik.essence_exhange() #First morning after kin warning

henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(24) #Morning of the fifth day
henrik.essence_exhange() #Second morning after kin warning

henrik.reduce_vital("SP",20) #walking and such
henrik.cast_skill("Fire Arrow",20) #kinfight
henrik.cast_skill("Drilling Shot",8) #kinfight
henrik.add_experience(1200)
#Get back, get given houses

henrik.regen(24) #Morning of the sixth day
henrik.essence_exhange() #Morning after killing kin and getting houses

henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(24) #Morning of the seventh day
henrik.essence_exhange() #Morning of training day, got backpacks that evening
henrik.add_vital("MP",henrik.vitals[5]*0.10) #regen assuming most of this day was spent within 2 meters of Daniel's 14% winter.

henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(24) #Morning of the eighth day
henrik.essence_exhange() #Morning of cave investigation day, day 1 of training timelapse
henrik.add_vital("MP",henrik.vitals[5]*0.10) #regen assuming most of this day was spent within 2 meters of Daniel's 14% winter.
print("Cave and training day")

henrik.reduce_vital("SP",20) #walking and such
henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(24) #Morning of the ninth day
henrik.essence_exhange() #2 of 7 training timelapse
henrik.add_vital("MP",henrik.vitals[5]*0.20) #regen assuming most of this day was spent within range of Daniel's 30% winter.
print("2 of 7")

henrik.cast_skill("Fire Arrow",20) #training time
henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(24) #Morning of the tenth day
henrik.essence_exhange() #3 of 7 training timelapse
henrik.add_vital("MP",henrik.vitals[5]*0.40) #regen assuming most of this day was spent within range of Daniel's 67% winter.
print("3 of 7")

henrik.cast_skill("Fire Arrow",20) #training time
henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(24) #Morning of the eleventh day
henrik.essence_exhange() #4 of 7 training timelapse
henrik.add_vital("MP",henrik.vitals[5]*0.45) #regen assuming most of this day was spent within range of Daniel's 76% winter.
print("4 of 7")

henrik.cast_skill("Fire Arrow",20) #training time
henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(24) #Morning of the twelfth day
henrik.essence_exhange() #5 of 7 training timelapse
henrik.add_vital("MP",henrik.vitals[5]*0.80) #regen assuming most of this day was spent within 2 meters of Daniel's 115% winter.
henrik.add_vital("MP",1000) # Mana bank, edging soulstrain
print("5 of 7")

henrik.cast_skill("Fire Arrow",180) #training time
henrik.reduce_vital("SP",20) #Just firing fire arrows and such
henrik.cast_skill("Drilling Shot",7) #training time

henrik.regen(24) #Morning of the thirteenth day
henrik.essence_exhange() #6 of 7 training timelapse
henrik.add_vital("MP",henrik.vitals[5]*0.85) #regen assuming most of this day was spent within range of Daniel's 120% winter.
henrik.add_vital("MP",1000) # Mana bank, edging soulstrain
print("6 of 7")

henrik.set_class(dc.animus)

henrik.cast_skill("Fire Arrow",40) #training time
henrik.reduce_vital("SP",10) #Just firing fire arrows and such
henrik.cast_skill("Drilling Shot",2) #training time

henrik.regen(24) #Morning of the fourteenth day
henrik.essence_exhange() #7 of 7 training timelapse
henrik.add_vital("MP",henrik.vitals[5]*0.40) #regen assuming most of this day was spent within range of Daniel's 68% winter.
print("7 of 7, skar evening")

henrik.cast_skill("Drilling Shot",2) #training time
henrik.regen(14) #regen before fight?
henrik.add_vital("MP",333) # Mana bank, filling up for the fight
henrik.raise_attribute(4,10)
henrik.cast_skill("Concussive Blows",8)
henrik.cast_skill("Fire Arrow",30) #Fighting Skar
henrik.cast_skill("Drilling Shot",16) #Fighting Skar
henrik.reduce_vital("SP",20) #Fighting Skar

henrik.regen(10) #Morning of the fifteenth day
henrik.essence_exhange() #Morning after fighting Skar
henrik.add_vital("MP",henrik.vitals[5]*1.2) #regen assuming most of this day was spent within range of Daniel's 170% winter.
print("Eviction day")

henrik.reduce_vital("SP",20) #Walking and hunting

henrik.regen(24) #Morning of the sixteenth day
henrik.essence_exhange() #Morning after getting kicked out
print("Day 1 of 7 - training at cave")
henrik.add_vital("MP",henrik.vitals[5]*1.5) #regen assuming most of this day was spent within range of Daniel's 200% winter.

henrik.cast_skill("Fire Arrow",40) #training time
henrik.reduce_vital("SP",20) #Hunting
henrik.cast_skill("Drilling Shot",3) #training time

henrik.regen(24) #Morning of the seventeeth day
henrik.essence_exhange() #training montage
print("Day 2 of 7 - training at cave")
henrik.add_vital("MP",henrik.vitals[5]*1.5) #regen assuming most of this day was spent within range of Daniel's 200% winter.

henrik.cast_skill("Fire Arrow",40) #training time
henrik.reduce_vital("SP",20) #Hunting
henrik.cast_skill("Drilling Shot",8) #training time

henrik.regen(24) #Morning of the eighteenth day
henrik.essence_exhange() #training montage
print("Day 3 of 7 - training at cave")
henrik.add_vital("MP",henrik.vitals[5]*1.6) #regen assuming most of this day was spent within range of Daniel's 216% winter.

henrik.cast_skill("Fire Arrow",40) #training time
henrik.reduce_vital("SP",20) #Hunting
henrik.cast_skill("Drilling Shot",8) #training time

henrik.regen(24) #Morning of the nineteenth day
henrik.essence_exhange() #training montage
print("Day 4 of 7 - training at cave")
henrik.add_vital("MP",henrik.vitals[5]*1.7) #regen assuming most of this day was spent within range of Daniel's 270% winter.

henrik.cast_skill("Fire Arrow",40) #training time
henrik.reduce_vital("SP",20) #Hunting
henrik.cast_skill("Drilling Shot",8) #training time

henrik.regen(24) #Morning of the twentieth day
henrik.essence_exhange() #training montage
print("Day 5 of 7 - training at cave")
henrik.add_vital("MP",henrik.vitals[5]*1.7) #regen assuming most of this day was spent within range of Daniel's 270% winter.

henrik.cast_skill("Fire Arrow",40) #training time
henrik.reduce_vital("SP",20) #Hunting
henrik.cast_skill("Drilling Shot",8) #training time

henrik.regen(24) #Morning of the 21st day
henrik.essence_exhange() #training montage
print("Day 6 of 7 - training at cave")
henrik.add_vital("MP",henrik.vitals[5]*2) #regen assuming most of this day was spent within range of Daniel's 316% winter.

henrik.cast_skill("Fire Arrow",40) #training time
henrik.reduce_vital("SP",20) #Hunting
henrik.cast_skill("Drilling Shot",8) #training time

henrik.regen(24) #Morning of the 22nd day
henrik.essence_exhange() #training montage
print("Day 7 of 7 - training at cave")
henrik.add_vital("MP",henrik.vitals[5]*2.3) #regen assuming most of this day was spent within range of Daniel's 334% winter.

henrik.cast_skill("Fire Arrow",40) #training time
henrik.reduce_vital("SP",20) #Hunting
henrik.cast_skill("Drilling Shot",8) #training time

henrik.regen(24) #Morning of the 23rd day
henrik.essence_exhange() #Gotta open da rocks
henrik.add_vital("MP",henrik.vitals[5]*3.1) #regen assuming most of this day was spent within range of Daniel's 410% winter.
print("Opening day")

henrik.cast_skill("Fire Arrow",40) #training time
henrik.reduce_vital("SP",60) #Hunting and clearing rocks
henrik.cast_skill("Drilling Shot",4) #training time

henrik.regen(24) #Morning of the 24th day
henrik.essence_exhange() #Gotta open da rocks
henrik.add_vital("MP",henrik.vitals[5]*3.2) #regen assuming most of this day was spent within range of Daniel's 430% winter.
print("Cave Day 2")

henrik.cast_skill("Concussive Blows",8)
henrik.cast_skill("Fire Arrow",120) #certified hyperfixation moment
henrik.reduce_vital("SP",60) #Shooting bears
henrik.cast_skill("Drilling Shot",11) #Bear time
henrik.add_experience(3960)

henrik.regen(24) #Morning of the 25th day
henrik.essence_exhange() #First day of fighting at the cave mouth
henrik.add_vital("MP",henrik.vitals[5]*3.2) #regen assuming most of this day was spent within range of Daniel's 430% winter.
henrik.add_vital("MP",1000) # Mana bank, edging soulstrain
print("Cave Day 3, i.e. bear day 2")

henrik.cast_skill("Drilling Shot",10) #Bear time
henrik.cast_skill("Fire Arrow",40)
henrik.add_experience(5400)

henrik.regen(24) #Morning of the 26th day
henrik.essence_exhange() #Second day of fighting at the cave mouth


henrik.update_vitals()
henrik.update_free_attributes()
henrik.printCharSheet(altCol= False)
print(henrik.vitals)
print(henrik.currVitals)
print(henrik.general_statistics)