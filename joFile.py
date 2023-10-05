import awakened as aw;
import delve_Class as dc;
import skill as sk;

micah = aw.Awakened(name='Micah Redacted',attributes = [10, 10, 10, 10, 10, 10, 10, 10], level = 0, level_cap=12)
micah.add_experience(400)
micah.reduce_vital("HP",40)
micah.reduce_vital("SP",90)

micah.regen(9.6) #sleeping after all the chaos
micah.essence_exhange()
micah.reduce_vital("HP",40)
micah.raise_attribute(4, 10)
micah.raise_attribute(5, 10)
micah.add_skill(sk.stonebolt)
micah.add_skill(sk.rock_push)
micah.cast_skill("Rock Push",20) #morning testing
micah.cast_skill("Stonebolt",13) #get mana down to 50
micah.reduce_vital("SP",90) #Helping out the villagers
micah.raise_attribute(4, 15)
micah.raise_attribute(5, 5)
micah.add_skill(sk.intrinsic_focus,1)
micah.add_skill(sk.intrinsic_clarity,1)
micah.regen(10) #Time spent during the day
micah.cast_skill("Stonebolt",7) #headache time, but I want that level

micah.regen(14) #Morning of the third day
micah.essence_exhange()
micah.reduce_vital("SP",100) #morning workout
micah.cast_skill("Stonebolt",13) #intrinsic leveling

micah.regen(24) #Morning of the fourth day
micah.essence_exhange() #First morning after kin warning
micah.reduce_vital("SP",90) #morning workout

micah.regen(24) #Morning of the fifth day
micah.essence_exhange() #Second morning after kin warning
micah.raise_attribute(4, 10)
micah.cast_skill("Stonebolt",40) #kinfight
micah.reduce_vital("SP",90) #kinfight
micah.add_experience(1200)
micah.cast_skill("Stonebolt",10) #finishing off some injured kin; kill requirement for class fulfilled!
micah.add_experience(-400) #Unlocking Geoevocation t1, earth manipulation t1, evocation metamagic t1, and magic utility t1
micah.add_experience(800)
#Get back, get given houses

micah.regen(24) #Morning of the sixth day
micah.essence_exhange() #Morning after killing kin and getting houses

micah.reduce_vital("SP",90) #Training this day
micah.cast_skill("Stonebolt",10)

micah.regen(24) #Morning of the seventh day
micah.essence_exhange() #Morning of training day, got backpacks that evening

micah.reduce_vital("SP",100) #Training this day, mostly just hoarding mana
micah.add_vital("MP",micah.vitals[5]*0.10) #regen assuming most of this day was spent within 2 meters of Daniel's 14% winter.

micah.regen(24) #Morning of the eighth day
micah.essence_exhange() #Morning of cave investigation day, day 1 of training timelapse
print("Cave and training day")

micah.reduce_vital("SP",100) #Workout
micah.add_vital("MP",micah.vitals[5]*0.10) #regen assuming most of this day was spent within 2 meters of Daniel's 14% winter.
micah.cast_skill("Stonebolt",60)
print(micah.currVitals[2])

micah.regen(24) #Morning of the ninth day
micah.essence_exhange() #2 of 7 training timelapse
print("2 of 7")

micah.reduce_vital("SP",100) #Workout
micah.add_vital("MP",micah.vitals[5]*0.20) #regen assuming most of this day was spent within range of Daniel's 30% winter.
micah.cast_skill("Stonebolt",60)
print(micah.currVitals[2])

micah.regen(24) #Morning of the tenth day
micah.essence_exhange() #3 of 7 training timelapse
print("3 of 7")

micah.reduce_vital("SP",100) #Workout
micah.add_vital("MP",micah.vitals[5]*0.40) #regen assuming most of this day was spent within range of Daniel's 67% winter.
micah.cast_skill("Stonebolt",60)

micah.regen(24) #Morning of the eleventh day
micah.essence_exhange() #4 of 7 training timelapse
print("4 of 7")

micah.reduce_vital("SP",100) #Workout
micah.add_vital("MP",micah.vitals[5]*0.45) #regen assuming most of this day was spent within range of Daniel's 76% winter.
micah.cast_skill("Stonebolt",7)
print(micah.currVitals[2])

micah.regen(24) #Morning of the twelfth day
micah.essence_exhange() #5 of 7 training timelapse
print("5 of 7")

micah.add_skill(sk.stone_spray)
micah.reduce_vital("SP",100) #Workout
micah.add_vital("MP",micah.vitals[5]*0.80) #regen assuming most of this day was spent within 2 meters of Daniel's 115% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spray",90)
print(micah.currVitals[2])

micah.regen(24) #Morning of the thirteenth day
micah.essence_exhange() #6 of 7 training timelapse
print("6 of 7")

micah.reduce_vital("SP",100) #Workout
micah.add_vital("MP",micah.vitals[5]*0.85) #regen assuming most of this day was spent within range of Daniel's 120% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spray",90)
print(micah.currVitals[2])

micah.regen(24) #Morning of the fourteenth day
micah.essence_exhange() #7 of 7 training timelapse
print("7 of 7, skar evening")

micah.reduce_vital("SP",100) #Workout
micah.add_vital("MP",micah.vitals[5]*0.40) #regen assuming most of this day was spent within range of Daniel's 68% winter.
micah.cast_skill("Stone Spray",10)
micah.regen(14) #regen before fight?
micah.add_vital("MP",333) # Mana bank, filling up for the fight
micah.raise_attribute(4,10)
print(micah.currVitals[2])
micah.cast_skill("Stonebolt",30) #Fighting Skar
micah.reduce_vital("SP",100) #Fighting Skar

micah.regen(10) #Morning of the fifteenth day
micah.essence_exhange() #Morning after talking to Skar
print("Eviction day")

micah.reduce_vital("SP",50) #Workout
micah.reduce_vital("HP",40) #Falling on rocks lol
micah.add_vital("MP",micah.vitals[5]*1.2) #regen assuming most of this day was spent within range of Daniel's 170% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spray",90)
micah.cast_skill("Rock Push",600)
print(micah.currVitals[2])

micah.regen(24) #Morning of the sixteenth day
micah.essence_exhange() #Morning after getting kicked out
print("Day 1 of 7 - training at cave")
micah.add_vital("MP",micah.vitals[5]*1.5) #regen assuming most of this day was spent within range of Daniel's 200% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain

micah.reduce_vital("SP",100) #Workout
micah.cast_skill("Rock Push",1500)
rock = micah.skills["Rock Push"]

micah.regen(24) #Morning of the seventeeth day
micah.essence_exhange() #training montage
print("Day 2 of 7 - training at cave")
micah.add_vital("MP",micah.vitals[5]*1.5) #regen assuming most of this day was spent within range of Daniel's 200% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain

micah.reduce_vital("SP",100) #Workout
micah.cast_skill("Rock Push",2400)

micah.regen(24) #Morning of the eighteenth day
micah.essence_exhange() #training montage
print("Day 3 of 7 - training at cave")
micah.add_vital("MP",micah.vitals[5]*1.6) #regen assuming most of this day was spent within range of Daniel's 216% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.add_skill(sk.stone_spear)

micah.reduce_vital("SP",100) #Workout
micah.cast_skill("Stone Spear",45)

micah.regen(24) #Morning of the nineteenth day
micah.essence_exhange() #training montage
print("Day 4 of 7 - training at cave")
micah.add_vital("MP",micah.vitals[5]*1.7) #regen assuming most of this day was spent within range of Daniel's 270% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain

micah.reduce_vital("SP",100) #Workout
micah.cast_skill("Stone Spear",55)

micah.regen(24) #Morning of the twentieth day
micah.essence_exhange() #training montage
print("Day 5 of 7 - training at cave")
micah.add_vital("MP",micah.vitals[5]*1.7) #regen assuming most of this day was spent within range of Daniel's 270% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain

micah.reduce_vital("SP",100) #Workout
micah.cast_skill("Stone Spear",65)

micah.regen(24) #Morning of the 21st day
micah.essence_exhange() #training montage
print("Day 6 of 7 - training at cave")
micah.add_vital("MP",micah.vitals[5]*2) #regen assuming most of this day was spent within range of Daniel's 316% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain

micah.reduce_vital("SP",100) #Workout
micah.cast_skill("Stone Spear",70)

micah.regen(24) #Morning of the 22nd day
micah.essence_exhange() #training montage
print("Day 7 of 7 - training at cave")
micah.add_vital("MP",micah.vitals[5]*2.3) #regen assuming most of this day was spent within range of Daniel's 334% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.set_class(dc.geomancer)

micah.reduce_vital("SP",100) #Workout
micah.cast_skill("Stone Spear",70)

micah.regen(24) #Morning of the 23rd day
micah.essence_exhange() #Gotta open da rocks
micah.add_vital("MP",micah.vitals[5]*3.1) #regen assuming most of this day was spent within range of Daniel's 410% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
print("Opening day")

micah.add_skill(sk.magical_synergy)
micah.add_skill(sk.earth_affinity)
skillEtAff = micah.skills["Earth Affinity"]
micah.reduce_vital("SP",80) #Helping to clear the rock pile
micah.cast_skill("Stone Spear",80)
skillEtAff.bank_exp(0.1*80*50)

micah.regen(24) #Morning of the 24th day
micah.essence_exhange() #Gotta open da rocks
micah.add_vital("MP",micah.vitals[5]*3.2) #regen assuming most of this day was spent within range of Daniel's 430% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
print("Cave Day 2")
micah.raise_attribute(4,30)
micah.add_skill(sk.earthmolding)

micah.cast_skill("Stone Spear",40)
skillEtAff.bank_exp(0.1*40*50)
micah.cast_skill("Rock Push",80) #Bears!
skillEtAff.bank_exp(0.1*80)
micah.add_experience(7392)

micah.regen(24) #Morning of the 25th day
micah.essence_exhange() #Second day of fighting at the cave mouth
micah.add_vital("MP",micah.vitals[5]*3.2) #regen assuming most of this day was spent within range of Daniel's 430% winter.
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
print("Cave Day 3, i.e. bear day 2")

micah.cast_skill("Stone Spear",160)
skillEtAff.bank_exp(0.1*160*50)
micah.add_experience(5400)

micah.regen(24) #Morning of the 26th day
micah.essence_exhange() #Begin timelapse
print("1 of 25 big timelapse")

micah.add_skill(sk.rooted)

micah.add_vital("MP",micah.vitals[5]*5.2) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",50)
skillEtAff.bank_exp(0.1*50*50)
micah.cast_skill("Rooted",300)
skillEtAff.bank_exp(0.1*300*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 27
micah.essence_exhange() #Begin timelapse
print("2 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*5.2) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 28
micah.essence_exhange() #Begin timelapse
print("3 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*5.2) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 29
micah.essence_exhange() #Begin timelapse
print("4 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*5.2) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 30
micah.essence_exhange() #Begin timelapse
print("5 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*5.2) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",2000)
skillEtAff.bank_exp(0.1*2000)

micah.regen(24) #Morning of the day 31
micah.essence_exhange() #Begin timelapse
print("6 of 25 big timelapse")

micah.add_skill(sk.liquefaction)
skillLiq = micah.skills["Liquefaction"]

micah.add_vital("MP",micah.vitals[5]*5.6) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",1000)
skillEtAff.bank_exp(0.1*1000*skillLiq.cost['value'])

micah.regen(24) #Morning of the day 32
micah.essence_exhange() #Begin timelapse
print("7 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*5.6) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",500)
skillEtAff.bank_exp(0.1*500*skillLiq.cost['value'])

micah.regen(24) #Morning of the day 33
micah.essence_exhange() #Begin timelapse
print("8 of 25 big timelapse")

micah.add_skill(sk.stoneset)
micah.add_skill(sk.stonemolding)

micah.add_vital("MP",micah.vitals[5]*5.6) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",250)
skillEtAff.bank_exp(0.1*250*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",250)
skillEtAff.bank_exp(0.1*250*5)
micah.cast_skill("Stoneset",250)
skillEtAff.bank_exp(0.1*250)

micah.regen(24) #Morning of the day 34
micah.essence_exhange() #Begin timelapse
print("9 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*6) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",100)
skillEtAff.bank_exp(0.1*100*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",250)
skillEtAff.bank_exp(0.1*250*5)
micah.cast_skill("Stoneset",250)
skillEtAff.bank_exp(0.1*250)

micah.regen(24) #Morning of the day 35
micah.essence_exhange() #Begin timelapse
print("10 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*6) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",100)
skillEtAff.bank_exp(0.1*100*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",250)
skillEtAff.bank_exp(0.1*250*5)
micah.cast_skill("Stoneset",250)
skillEtAff.bank_exp(0.1*250)

micah.regen(24) #Morning of the day 36
micah.essence_exhange() #Begin timelapse
print("11 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*6.18) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",750)
skillEtAff.bank_exp(0.1*750*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 37
micah.essence_exhange() #Begin timelapse
print("12 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*7.1) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 38
micah.essence_exhange() #Begin timelapse
print("13 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*7.5) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 39
micah.essence_exhange() #Begin timelapse
print("14 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*7.8) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 40
micah.essence_exhange() #Begin timelapse
print("15 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.04) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 41
micah.essence_exhange() #Begin timelapse
print("16 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.1) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 42
micah.essence_exhange() #Begin timelapse
print("17 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.1) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 43
micah.essence_exhange() #Begin timelapse
print("18 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.16) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 44
micah.essence_exhange() #Begin timelapse
print("19 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.16) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 45
micah.essence_exhange() #Begin timelapse
print("20 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.2) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 46
micah.essence_exhange() #Begin timelapse
print("21 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.2) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
micah.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
micah.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 47
micah.essence_exhange() #Begin timelapse
print("22 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.28) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",150)
skillEtAff.bank_exp(0.1*150*50)
micah.cast_skill("Rooted",1600)
skillEtAff.bank_exp(0.1*1600*10)
micah.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
micah.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

micah.regen(24) #Morning of the day 48
micah.essence_exhange() #Begin timelapse
print("23 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.28) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
micah.cast_skill("Rooted",1600)
micah.cast_skill("Earthmolding",1000)
micah.cast_skill("Stoneset",1000)
micah.cast_skill("Rock Push",2000)

micah.regen(24) #Morning of the day 49
micah.essence_exhange() #Begin timelapse
print("24 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.28) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",100)
micah.cast_skill("Rooted",1600)
micah.cast_skill("Earthmolding",1000)
micah.cast_skill("Stoneset",1000)
micah.cast_skill("Rock Push",2000)

micah.regen(24) #Morning of the day 50
micah.essence_exhange() #Begin timelapse
print("25 of 25 big timelapse")

micah.add_vital("MP",micah.vitals[5]*8.34) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Rooted",2000)

micah.regen(24) #Morning of day 51
micah.essence_exhange() #The next arc
print("Delveday")

micah.add_vital("MP",micah.vitals[5]*8.34) #regen with night spent neat Daniel
micah.add_vital("MP",1000) # Mana bank, edging soulstrain
micah.cast_skill("Stone Spear",120)
micah.cast_skill("Stonebolt",1100)
micah.cast_skill("Rooted",480)
micah.cast_skill("Stonemolding",500)

micah.regen(24) #Morning of day 52
micah.essence_exhange() #The next arc
print("Back to town")

"""micah.regen(24) #Morning of day 53
micah.essence_exhange() #The next arc
print("On our way to Doduo")

micah.regen(24) #Morning of day 54
micah.essence_exhange() #The next arc
print("Travelling to Diglett")

micah.regen(24) #Morning of day 55
micah.essence_exhange() #The next arc
print("Made it to Duodecillion")

micah.regen(24) #Morning of day 56
micah.essence_exhange() #The next arc
print("Overnight in Daryl")

micah.regen(24) #Morning of day 57
micah.essence_exhange() #The next arc
print("Travel")

micah.regen(24) #Morning of day 58
micah.essence_exhange() #The next arc
print("Travel")

micah.regen(24) #Morning of day 59
micah.essence_exhange() #The next arc
print("Back at lair, clearing out the hounds, seeing the blue")

micah.regen(24) #Morning of day 60
micah.essence_exhange()
print("Crafting and army scout encounter")

micah.regen(24) #Morning of day 61
micah.essence_exhange()
print("Day 1 marching with village")

micah.regen(24) #Morning of day 62
micah.essence_exhange()
print("Day 2 marching with village")

micah.regen(24) #Morning of day 63
micah.essence_exhange()
print("Day 3 marching with village, arriving")

micah.regen(24) #Morning of day 64
micah.essence_exhange()
print("Prep for travel and twiddling thumbs in town")

micah.regen(24) #Morning of day 65
micah.essence_exhange()
print("Ambush army harried back over the border by silver team")

micah.regen(24) #Morning of day 66
micah.essence_exhange()
print("Travel")

micah.regen(24) #Morning of day 67
micah.essence_exhange()
print("Travel")

micah.regen(24) #Morning of day 68
micah.essence_exhange()
print("Arriving back at quillcaves")"""

## Add 28 days of training

# Day 96?


micah.update_vitals()
micah.update_free_attributes()
micah.printCharSheet(altCol= False)
print(micah.vitals)
print(micah.currVitals)
print(micah.general_statistics)
print(micah.hours)