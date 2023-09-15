import awakened as aw;
import delve_Class as dc;
import skill as sk;

eric = aw.Awakened(name='Eric',attributes = [10, 10, 10, 10, 10, 10, 10, 10], level = 0, level_cap=0)
eric.add_experience(70) #rat kill
eric.update_level_cap(4) #rat kill
eric.add_skill(sk.rammer)
eric.raise_attribute(5, 10) #points into clarity
eric.add_experience(30) #killing goblin
eric.update_level_cap(12) #killing goblin
eric.reduce_vital("SP", 50) #Whacking things with clubs and generally running around
eric.cast_skill("Rammer",3) #Casting Rammer arbitrary amount of mana spent
eric.add_experience(330) #stonesinger kill
eric.update_level_cap(21) #stonesinger kill

eric.regen(9.6) #sleeping after all the chaos
eric.essence_exhange() #the first morning in this new world
eric.add_skill(sk.more_pylons)
skillPyl = eric.skills["More Pylons"]

eric.add_skill(sk.mana_wall)
eric.add_skill(sk.intrinsic_clarity,1) #regen time
eric.cast_skill("Rammer",13) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",13) #Attacking mana walls with rammer, arbitrary amount of mana spent
skillPyl.bank_exp(0.1*26*10)
eric.raise_attribute(5, 30) #points into clarity

eric.regen(10) #Day passes
eric.cast_skill("Rammer",20) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",20) #Attacking mana walls with rammer, arbitrary amount of mana spent
skillPyl.bank_exp(0.1*40*10)

eric.regen(14) #Night passes, Morning of the third day
eric.essence_exhange()

eric.raise_attribute(5, 10) #points into clarity
eric.add_skill(sk.intrinsic_focus,1) #now he only has to wake up every two hours instead of 45 minutes, for maximum training
eric.reduce_vital("SP",100) #morning workout
eric.cast_skill("Rammer",15) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",15) #Attacking mana walls with rammer, arbitrary amount of mana spent
skillPyl.bank_exp(0.1*30*10)

eric.regen(10) #Day passes
eric.cast_skill("Rammer",24) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",24) #Attacking mana walls with rammer, arbitrary amount of mana spent
skillPyl.bank_exp(0.1*48*10)

eric.regen(12) #Night passes, Morning of the fourth day
eric.essence_exhange() #First morning after kin warning
eric.reduce_vital("SP",90) #morning workout
eric.cast_skill("Rammer",26) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",26) #Attacking mana walls with rammer, arbitrary amount of mana spent
skillPyl.bank_exp(0.1*54*10)

eric.regen(12) #day passes
eric.cast_skill("Rammer",26) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",26) #Attacking mana walls with rammer, arbitrary amount of mana spent
skillPyl.bank_exp(0.1*54*10)

eric.regen(12) #Night passes, Morning of the fifth day
eric.essence_exhange() #Second morning after kin warning
eric.reduce_vital("SP",90) #fighting kin
eric.cast_skill("Rammer",10) #Casting Rammer arbitrary amount of mana spent
eric.add_experience(2100) #kin kills
eric.raise_attribute(5, 10) #points into clarity
eric.set_class(dc.dynamo)
eric.add_skill(sk.combined_arms)
skillArm = eric.skills["Combined Arms"]

eric.essence_exhange() #Morning after killing kin and getting houses, a day of training
eric.raise_attribute(5, 10) #points into clarity
eric.reduce_vital("SP",90) #Morning workout

i=0
while i<24:
    eric.regen(1) #Training on the sixth day
    eric.cast_skill("Rammer",8) #Casting Rammer arbitrary amount of mana spent
    eric.cast_skill("Mana Wall",8) #Attacking mana walls with rammer, arbitrary amount of mana spent
    i += 1
skillPyl.bank_exp(0.1*16*10*24)
skillArm.bank_exp(0.1*16*10*24)

eric.essence_exhange() #Morning of training day, got backpacks that evening
eric.raise_attribute(5, 10) #points into clarity
eric.add_skill(sk.tighter_mana_structures)
skillTight = eric.skills["Tighter Mana Structures"]
eric.reduce_vital("SP",90) #Morning workout

i=0
while i<24:
    eric.regen(1) #Morning of the third day
    eric.cast_skill("Rammer",11) #Casting Rammer arbitrary amount of mana spent
    eric.cast_skill("Mana Wall",10) #Attacking mana walls with rammer, arbitrary amount of mana spent
    i += 1
skillPyl.bank_exp(0.1*21*10*24)
skillArm.bank_exp(0.1*21*10*24)
skillTight.bank_exp(0.1*21*10*24)

eric.essence_exhange() #Morning of cave investigation day
print("Cave and training day")
eric.raise_attribute(5, 10) #points into clarity
eric.add_skill(sk.mana_bank)

eric.reduce_vital("SP",90) #Workout
eric.cast_skill("Rammer",315) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",315) #Attacking mana walls with rammer, arbitrary amount of mana spent
skillPyl.bank_exp(0.1*315*10*2)
skillArm.bank_exp(0.1*315*10*2)
skillTight.bank_exp(0.1*315*10*2)

eric.regen(24) #Morning of the ninth day
eric.essence_exhange() #2 of 7 training timelapse
eric.raise_attribute(5, 10) #points into clarity
eric.add_skill(sk.stone_tower)

eric.reduce_vital("SP",90) #Workout
eric.cast_skill("Rammer",385) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",385) #Attacking mana walls with rammer, arbitrary amount of mana spent
skillPyl.bank_exp(0.1*385*10*2)
skillArm.bank_exp(0.1*385*10*2)
skillTight.bank_exp(0.1*385*10*2)

eric.regen(24) #Morning of the tenth day
eric.essence_exhange() #3 of 7 training timelapse
eric.raise_attribute(5, 10) #points into clarity
eric.add_skill(sk.magic_missile_turret)

eric.reduce_vital("SP",90) #Workout
eric.cast_skill("Rammer",460) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",460) #Attacking mana walls with rammer, arbitrary amount of mana spent
skillPyl.bank_exp(0.1*460*10*2)
skillArm.bank_exp(0.1*460*10*2)
skillTight.bank_exp(0.1*460*10*2)

eric.regen(24) #Morning of the eleventh day
eric.essence_exhange() #4 of 7 training timelapse
print("4 of 7")
eric.add_vital("MP",eric.vitals[5]*0.45) #regen assuming most of this day was spent within range of Daniel's 76% winter.
eric.raise_attribute(5, 10) #points into clarity
eric.add_skill(sk.magical_synergy)

eric.reduce_vital("SP",90) #Workout
eric.cast_skill("Rammer",735) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",735) #Attacking mana walls with rammer, arbitrary amount of mana spent
skillPyl.bank_exp(0.1*735*10*2)
skillArm.bank_exp(0.1*735*10*2)
skillTight.bank_exp(0.1*735*10*2)

eric.regen(24) #Morning of the twelfth day
eric.essence_exhange() #5 of 7 training timelapse
print("5 of 7")
eric.add_vital("MP",eric.vitals[5]*0.80) #regen assuming most of this day was spent within 2 meters of Daniel's 115% winter.
eric.raise_attribute(5, 10) #points into clarity
eric.add_skill(sk.ominous_eye)

eric.reduce_vital("SP",90) #Workout
eric.cast_skill("Rammer",100) #Casting Rammer arbitrary amount of mana spent
eric.cast_skill("Mana Wall",300) #Attacking mana walls with rammer, arbitrary amount of mana spent
eric.cast_skill("Mana Bank",1600)
skillPyl.bank_exp(0.1*2000*10)
skillArm.bank_exp(0.1*2000*10)
skillTight.bank_exp(0.1*2000*10)

eric.regen(24) #Morning of the thirteenth day
eric.essence_exhange() #6 of 7 training timelapse
print("6 of 7")
eric.add_vital("MP",eric.vitals[5]*0.85) #regen assuming most of this day was spent within range of Daniel's 120% winter.
eric.raise_attribute(5, 10) #points into clarity
eric.add_skill(sk.war_banner)

eric.reduce_vital("SP",90) #Workout
eric.cast_skill("Mana Bank",2100)
skillPyl.bank_exp(0.1*2100*10)
skillArm.bank_exp(0.1*2100*10)
skillTight.bank_exp(0.1*2100*10)

eric.regen(24) #Morning of the fourteenth day
eric.essence_exhange() #7 of 7 training timelapse
print("7 of 7, skar evening")
eric.add_vital("MP",eric.vitals[5]*0.40) #regen assuming most of this day was spent within range of Daniel's 68% winter.
eric.raise_attribute(5, 10) #points into clarity
eric.add_skill(sk.flexible_design)
skillFlex = eric.skills["Flexible Design"]

eric.reduce_vital("SP",90) #Workout
eric.cast_skill("Mana Bank",1200)
skillPyl.bank_exp(0.1*1200*10)
skillArm.bank_exp(0.1*1200*10)
skillTight.bank_exp(0.1*1200*10)
skillFlex.bank_exp(0.1*1200*10)

eric.regen(14) #regen before fight?
print(eric.currVitals[2])

eric.update_vitals()
eric.update_free_attributes()
eric.printCharSheet(altCol= False)
print(eric.general_statistics)
