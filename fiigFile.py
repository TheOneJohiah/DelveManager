import awakened as aw;
import delve_Class as dc;
import skill as sk;

fiig = aw.Awakened(name='Fiig',attributes = [10, 10, 10, 10, 10, 10, 10, 10], level = 0)
fiig.add_experience(70)
fiig.update_level_cap(4)
fiig.add_experience(120)
fiig.update_level_cap(12)
fiig.reduce_vital("HP", 140) #Losing an arm!!!
fiig.add_vital("HP", 160) #Healing from Grace
fiig.reduce_vital("SP", 110) #Whacking things with clubs and generally running around
fiig.add_experience(700)
fiig.update_level_cap(21)

fiig.regen(9.6) #sleeping after all the chaos
fiig.essence_exhange()

fiig.add_skill(sk.strength_of_arm)
fiig.add_skill(sk.rugged_defense)
fiig.raise_attribute(2, 50)

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever
fiig.regen(10) #Time spent during the day

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(14) #Morning of the third day
fiig.essence_exhange()

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(24) #Morning of the fourth day
fiig.essence_exhange() #First morning after kin warning

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(24) #Morning of the fifth day
fiig.essence_exhange() #Second morning after kin warning

#Fighting kin
fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever
#Get back, get given houses

fiig.regen(24) #Morning of the sixth day
fiig.essence_exhange() #Morning after killing kin and getting houses

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(24) #Morning of the seventh day
fiig.essence_exhange() #Morning of training day, got backpacks that evening

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(24) #Morning of the eighth day
fiig.essence_exhange() #Morning of cave investigation day, day 1 of training timelapse
print("Cave and training day")

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(24) #Morning of the ninth day
fiig.essence_exhange() #2 of 7 training timelapse
print("2 of 7")

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(24) #Morning of the tenth day
fiig.essence_exhange() #3 of 7 training timelapse
print("3 of 7")

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(24) #Morning of the eleventh day
fiig.essence_exhange() #4 of 7 training timelapse
print("4 of 7")

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(24) #Morning of the twelfth day
fiig.essence_exhange() #5 of 7 training timelapse
print("5 of 7")

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(24) #Morning of the thirteenth day
fiig.essence_exhange() #6 of 7 training timelapse
print("6 of 7")

fiig.set_class(dc.tortugo)

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30) #Healing from Grace
fiig.reduce_vital("HP", 120) #Training or whatever

fiig.regen(24) #Morning of the fourteenth day
fiig.essence_exhange() #7 of 7 training timelapse
print("7 of 7, skar evening")

fiig.add_skill(sk.intrinsic_resistance)
fiig.add_skill(sk.turtle_kata)
skillTurt = fiig.skills["Turtle Kata"]

fiig.reduce_vital("HP", 60) #Training or whatever
fiig.regen(14) #regen before fight?

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 120) #Healing from Grace
fiig.reduce_vital("HP", 200) #Training or whatever

fiig.regen(10) #Morning of the fifteenth day
fiig.essence_exhange() #Morning after fighting Skar
print("Eviction day")

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30*15) #Healing from Grace
fiig.reduce_vital("HP", 540) #Training or whatever

fiig.regen(24) #Morning of the sixteenth day
fiig.essence_exhange() #Morning after getting kicked out
print("Day 1 of 7 - training at cave")

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30*15) #Healing from Grace
fiig.reduce_vital("HP", 540) #Training or whatever

fiig.regen(24) #Morning of the seventeeth day
fiig.essence_exhange() #training montage
print("Day 2 of 7 - training at cave")

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30*15) #Healing from Grace
fiig.reduce_vital("HP", 540) #Training or whatever

fiig.regen(24) #Morning of the eighteenth day
fiig.essence_exhange() #training montage
print("Day 3 of 7 - training at cave")

fiig.add_skill(sk.turtle_skin)
fiig.add_skill(sk.heavy_armor)
fiig.raise_attribute(2,10)

fiig.reduce_vital("SP",90) #Training or whatever
fiig.add_vital("HP", 30*15) #Healing from Grace
fiig.reduce_vital("HP", 540) #Training or whatever

fiig.regen(24) #Morning of the nineteenth day
fiig.essence_exhange() #training montage
"""print("Day 4 of 7 - training at cave")
fiig.add_vital("MP",fiig.vitals[5]*1.7) #regen assuming most of this day was spent within range of Daniel's 270% winter.
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain

fiig.reduce_vital("SP",100) #Workout
fiig.cast_skill("Stone Spear",55)

fiig.regen(24) #Morning of the twentieth day
fiig.essence_exhange() #training montage
print("Day 5 of 7 - training at cave")
fiig.add_vital("MP",fiig.vitals[5]*1.7) #regen assuming most of this day was spent within range of Daniel's 270% winter.
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain

fiig.reduce_vital("SP",100) #Workout
fiig.cast_skill("Stone Spear",65)

fiig.regen(24) #Morning of the 21st day
fiig.essence_exhange() #training montage
print("Day 6 of 7 - training at cave")
fiig.add_vital("MP",fiig.vitals[5]*2) #regen assuming most of this day was spent within range of Daniel's 316% winter.
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain

fiig.reduce_vital("SP",100) #Workout
fiig.cast_skill("Stone Spear",70)

fiig.regen(24) #Morning of the 22nd day
fiig.essence_exhange() #training montage
print("Day 7 of 7 - training at cave")
fiig.add_vital("MP",fiig.vitals[5]*2.3) #regen assuming most of this day was spent within range of Daniel's 334% winter.
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.set_class(dc.geomancer)

fiig.reduce_vital("SP",100) #Workout
fiig.cast_skill("Stone Spear",70)

fiig.regen(24) #Morning of the 23rd day
fiig.essence_exhange() #Gotta open da rocks
fiig.add_vital("MP",fiig.vitals[5]*3.1) #regen assuming most of this day was spent within range of Daniel's 410% winter.
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
print("Opening day")

fiig.add_skill(sk.magical_synergy)
fiig.add_skill(sk.earth_affinity)
skillEtAff = fiig.skills["Earth Affinity"]
fiig.reduce_vital("SP",80) #Helping to clear the rock pile
fiig.cast_skill("Stone Spear",80)
skillEtAff.bank_exp(0.1*80*50)

fiig.regen(24) #Morning of the 24th day
fiig.essence_exhange() #Gotta open da rocks
fiig.add_vital("MP",fiig.vitals[5]*3.2) #regen assuming most of this day was spent within range of Daniel's 430% winter.
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
print("Cave Day 2")
fiig.raise_attribute(4,30)
fiig.add_skill(sk.earthmolding)

fiig.cast_skill("Stone Spear",40)
skillEtAff.bank_exp(0.1*40*50)
fiig.cast_skill("Rock Push",80) #Bears!
skillEtAff.bank_exp(0.1*80)
fiig.add_experience(7392)

fiig.regen(24) #Morning of the 25th day
fiig.essence_exhange() #Second day of fighting at the cave mouth
fiig.add_vital("MP",fiig.vitals[5]*3.2) #regen assuming most of this day was spent within range of Daniel's 430% winter.
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
print("Cave Day 3, i.e. bear day 2")

fiig.cast_skill("Stone Spear",160)
skillEtAff.bank_exp(0.1*160*50)
fiig.add_experience(5400)

fiig.regen(24) #Morning of the 26th day
fiig.essence_exhange() #Begin timelapse
print("1 of 25 big timelapse")

fiig.add_skill(sk.rooted)

fiig.add_vital("MP",fiig.vitals[5]*5.2) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",50)
skillEtAff.bank_exp(0.1*50*50)
fiig.cast_skill("Rooted",300)
skillEtAff.bank_exp(0.1*300*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 27
fiig.essence_exhange() #Begin timelapse
print("2 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*5.2) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 28
fiig.essence_exhange() #Begin timelapse
print("3 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*5.2) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 29
fiig.essence_exhange() #Begin timelapse
print("4 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*5.2) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 30
fiig.essence_exhange() #Begin timelapse
print("5 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*5.2) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",2000)
skillEtAff.bank_exp(0.1*2000)

fiig.regen(24) #Morning of the day 31
fiig.essence_exhange() #Begin timelapse
print("6 of 25 big timelapse")

fiig.add_skill(sk.liquefaction)
skillLiq = fiig.skills["Liquefaction"]

fiig.add_vital("MP",fiig.vitals[5]*5.6) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",1000)
skillEtAff.bank_exp(0.1*1000*skillLiq.cost['value'])

fiig.regen(24) #Morning of the day 32
fiig.essence_exhange() #Begin timelapse
print("7 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*5.6) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",500)
skillEtAff.bank_exp(0.1*500*skillLiq.cost['value'])

fiig.regen(24) #Morning of the day 33
fiig.essence_exhange() #Begin timelapse
print("8 of 25 big timelapse")

fiig.add_skill(sk.stoneset)
fiig.add_skill(sk.stonemolding)

fiig.add_vital("MP",fiig.vitals[5]*5.6) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",250)
skillEtAff.bank_exp(0.1*250*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",250)
skillEtAff.bank_exp(0.1*250*5)
fiig.cast_skill("Stoneset",250)
skillEtAff.bank_exp(0.1*250)

fiig.regen(24) #Morning of the day 34
fiig.essence_exhange() #Begin timelapse
print("9 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*6) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",100)
skillEtAff.bank_exp(0.1*100*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",250)
skillEtAff.bank_exp(0.1*250*5)
fiig.cast_skill("Stoneset",250)
skillEtAff.bank_exp(0.1*250)

fiig.regen(24) #Morning of the day 35
fiig.essence_exhange() #Begin timelapse
print("10 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*6) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",100)
skillEtAff.bank_exp(0.1*100*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",250)
skillEtAff.bank_exp(0.1*250*5)
fiig.cast_skill("Stoneset",250)
skillEtAff.bank_exp(0.1*250)

fiig.regen(24) #Morning of the day 36
fiig.essence_exhange() #Begin timelapse
print("11 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*6.18) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",750)
skillEtAff.bank_exp(0.1*750*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 37
fiig.essence_exhange() #Begin timelapse
print("12 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*7.1) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 38
fiig.essence_exhange() #Begin timelapse
print("13 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*7.5) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 39
fiig.essence_exhange() #Begin timelapse
print("14 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*7.8) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 40
fiig.essence_exhange() #Begin timelapse
print("15 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.04) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 41
fiig.essence_exhange() #Begin timelapse
print("16 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.1) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 42
fiig.essence_exhange() #Begin timelapse
print("17 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.1) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 43
fiig.essence_exhange() #Begin timelapse
print("18 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.16) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 44
fiig.essence_exhange() #Begin timelapse
print("19 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.16) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 45
fiig.essence_exhange() #Begin timelapse
print("20 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.2) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 46
fiig.essence_exhange() #Begin timelapse
print("21 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.2) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
skillEtAff.bank_exp(0.1*100*50)
fiig.cast_skill("Rooted",400)
skillEtAff.bank_exp(0.1*400*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Liquefaction",50)
skillEtAff.bank_exp(0.1*50*skillLiq.cost['value'])
fiig.cast_skill("Stonemolding",2000)
skillEtAff.bank_exp(0.1*2000*5)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 47
fiig.essence_exhange() #Begin timelapse
print("22 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.28) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",150)
skillEtAff.bank_exp(0.1*150*50)
fiig.cast_skill("Rooted",1600)
skillEtAff.bank_exp(0.1*1600*10)
fiig.cast_skill("Earthmolding",1000)
skillEtAff.bank_exp(0.1*1000)
fiig.cast_skill("Stoneset",1000)
skillEtAff.bank_exp(0.1*1000)

fiig.regen(24) #Morning of the day 48
fiig.essence_exhange() #Begin timelapse
print("23 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.28) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
fiig.cast_skill("Rooted",1600)
fiig.cast_skill("Earthmolding",1000)
fiig.cast_skill("Stoneset",1000)
fiig.cast_skill("Rock Push",2000)

fiig.regen(24) #Morning of the day 49
fiig.essence_exhange() #Begin timelapse
print("24 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.28) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Stone Spear",100)
fiig.cast_skill("Rooted",1600)
fiig.cast_skill("Earthmolding",1000)
fiig.cast_skill("Stoneset",1000)
fiig.cast_skill("Rock Push",2000)

fiig.regen(24) #Morning of the day 50
fiig.essence_exhange() #Begin timelapse
print("25 of 25 big timelapse")

fiig.add_vital("MP",fiig.vitals[5]*8.34) #regen with night spent neat Daniel
fiig.add_vital("MP",1000) # Mana bank, edging soulstrain
fiig.cast_skill("Rooted",2000)

fiig.regen(24) #Morning of day 51
fiig.essence_exhange() #The next arc
print("Delveday")

fiig.regen(24) #Morning of day 52
fiig.essence_exhange() #The next arc
print("Dunno yet")"""

fiig.update_vitals()
fiig.update_free_attributes()
fiig.printCharSheet(altCol= False)
print(fiig.vitals)
print(fiig.currVitals)
print(fiig.general_statistics)
print(fiig.hours)