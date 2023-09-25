import awakened as aw;
import delve_Class as dc;
import skill as sk;

#Purify>Winter>Amplify Aura>Intrinsic Clarity>Extend Aura>Aura Focus

daniel = aw.Awakened(name='Daniel',attributes = [10, 10, 10, 10, 10, 10, 10, 10], level = 0, level_cap=0)
daniel.update_level_cap(4)
daniel.add_experience(30)
daniel.update_level_cap(12)
daniel.add_experience(110)

daniel.regen(9.6) #sleeping after all the chaos
daniel.essence_exhange() #First time waking up here
daniel.raise_attribute(5,20) #All in on clarity
daniel.reduce_vital("SP",100) #Workout
daniel.add_skill(sk.purify)
daniel.add_skill(sk.winter)
daniel.cast_skill("Purify",19)

daniel.regen(10) #Time spent during the day
daniel.add_vital("MP",daniel.vitals[5]*0.1*10/24) #Unboosted rank 1 winter
daniel.cast_skill("Purify",12)
daniel.cast_skill("Winter",10)

daniel.regen(14) #Sleeping till Morning of the third day
daniel.essence_exhange() #Second time waking up here
daniel.raise_attribute(5,10) #All in on clarity
daniel.add_skill(sk.amplify_aura)
skillPur = daniel.skills["Purify"]
skillWint = daniel.skills["Winter"]
skillAmp = daniel.skills["Amplify Aura"]
#print(skill.cost['value'])
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)) #Rank 1 winter with rank 1 amp aura, now assuming he runs it constantly
print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1))

daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",17*(1 + skillAmp.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*17*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)

daniel.regen(24) #Morning of the fourth day
daniel.essence_exhange() #First morning after kin warning
#Winter regen for the day
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)) #Rank 1 winter with rank 1 amp aura, now assuming he runs it constantly
print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1))

daniel.raise_attribute(5,10) #All in on clarity
daniel.add_skill(sk.intrinsic_clarity)
daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",20*(1 + skillAmp.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*20*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)

daniel.regen(24) #Morning of the fifth day
daniel.essence_exhange() #Second morning after kin warning
#Winter regen for the day
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1))

daniel.raise_attribute(5,10) #All in on clarity. This is consistently after the winter regen for the day to average out running winter while sleeping
daniel.add_skill(sk.extend_aura)
skillExt = daniel.skills["Extend Aura"]
daniel.reduce_vital("SP",100) #Workout/fighting kin
daniel.cast_skill("Purify",15*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*15*0.2)
skillExt.bank_exp(skillPur.cost['value']*15*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)
skillExt.bank_exp(skillWint.cost['value']*24*0.2)

daniel.add_experience(1500) #kindeaths
daniel.raise_attribute(5,10) #All in on clarity
daniel.set_class(dc.dynamo)

daniel.cast_skill("Purify",43*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*43*0.2)
skillExt.bank_exp(skillPur.cost['value']*43*0.2)

daniel.regen(24) #Morning of the sixth day
daniel.essence_exhange() #Morning after killing kin and getting houses, a day of training
#Winter regen for the day
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1))

daniel.raise_attribute(5,10) #All in on clarity
daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",30*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*30*0.2)
skillExt.bank_exp(skillPur.cost['value']*30*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)
skillExt.bank_exp(skillWint.cost['value']*24*0.2)

daniel.regen(24) #Morning of the seventh day
daniel.essence_exhange() #Morning of training day, got backpacks that evening
daniel.add_skill(sk.intrinsic_focus)
#Winter regen for the day
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1))
print("Day before cave")

daniel.raise_attribute(5,10) #All in on clarity
daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",32*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*32*0.2)
skillExt.bank_exp(skillPur.cost['value']*32*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)
skillExt.bank_exp(skillWint.cost['value']*24*0.2)

daniel.regen(24) #Morning of the eighth day
daniel.essence_exhange() #Morning of cave investigation day
#Winter regen for the day, more training time
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1))
print("Cave and training day")

daniel.raise_attribute(5,10) #All in on clarity
daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",33*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*33*0.2)
skillExt.bank_exp(skillPur.cost['value']*33*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)
skillExt.bank_exp(skillWint.cost['value']*24*0.2)


daniel.regen(24) #Morning of the ninth day
daniel.essence_exhange() #2 of 7 training timelapse
#Winter regen for the day
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
#print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1))
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1))
print("2 of 7")

daniel.add_skill(sk.aura_focus) #FOCUS TIME WOO
daniel.raise_attribute(5,10) #All in on clarity
daniel.reduce_vital("SP",100) #Workout

skillFoc = daniel.skills["Aura Focus"]
daniel.cast_skill("Purify",25*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*25*0.2)
skillExt.bank_exp(skillPur.cost['value']*25*0.2)
skillFoc.bank_exp(skillPur.cost['value']*25*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)
skillExt.bank_exp(skillWint.cost['value']*24*0.2)
skillFoc.bank_exp(skillWint.cost['value']*24*0.2)

daniel.regen(24) #Morning of the tenth day
daniel.essence_exhange() #3 of 7 training timelapse
#Winter regen for the day
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
#print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
print("3 of 7")

daniel.raise_attribute(5,10) #All in on clarity
daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",27*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*27*0.2)
skillExt.bank_exp(skillPur.cost['value']*27*0.2)
skillFoc.bank_exp(skillPur.cost['value']*27*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)
skillExt.bank_exp(skillWint.cost['value']*24*0.2)
skillFoc.bank_exp(skillWint.cost['value']*24*0.2)

daniel.regen(24) #Morning of the eleventh day
daniel.essence_exhange() #4 of 7 training timelapse
#Winter regen for the day
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
#print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
print("4 of 7")

daniel.raise_attribute(5,10) #All in on clarity
daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",25*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*25*0.2)
skillExt.bank_exp(skillPur.cost['value']*25*0.2)
skillFoc.bank_exp(skillPur.cost['value']*25*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)
skillExt.bank_exp(skillWint.cost['value']*24*0.2)
skillFoc.bank_exp(skillWint.cost['value']*24*0.2)

daniel.regen(24) #Morning of the twelfth day
daniel.essence_exhange() #5 of 7 training timelapse
#Winter regen for the day
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
#print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
print("5 of 7")

daniel.raise_attribute(5,10) #All in on clarity
daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",29*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*29*0.2)
skillExt.bank_exp(skillPur.cost['value']*29*0.2)
skillFoc.bank_exp(skillPur.cost['value']*29*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)
skillExt.bank_exp(skillWint.cost['value']*24*0.2)
skillFoc.bank_exp(skillWint.cost['value']*24*0.2)

daniel.regen(24) #Morning of the thirteenth day
daniel.essence_exhange() #6 of 7 training timelapse
#Winter regen for the day
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
#print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
print("6 of 7")

daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",29*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*29*0.2)
skillExt.bank_exp(skillPur.cost['value']*29*0.2)
skillFoc.bank_exp(skillPur.cost['value']*29*0.2)
daniel.cast_skill("Winter",24*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*24*0.2)
skillExt.bank_exp(skillWint.cost['value']*24*0.2)
skillFoc.bank_exp(skillWint.cost['value']*24*0.2)

daniel.regen(24) #Morning of the fourteenth day
daniel.essence_exhange() #7 of 7 training timelapse, Skarevening
#Winter regen for the day
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
#print(daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
print("7 of 7, skar evening")

daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",20*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*20*0.2)
skillExt.bank_exp(skillPur.cost['value']*20*0.2)
skillFoc.bank_exp(skillPur.cost['value']*20*0.2)
daniel.cast_skill("Winter",14*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*14*0.2)
skillExt.bank_exp(skillWint.cost['value']*14*0.2)

daniel.regen(14) #regen before fight?
daniel.reduce_vital("SP",100) #Fighting Skar
daniel.cast_skill("Winter",10*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*10*0.2)
skillExt.bank_exp(skillWint.cost['value']*10*0.2)

daniel.regen(10) #Morning of the fifteenth day
daniel.essence_exhange() #Morning after talking to Skar
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)) #Rank 1 winter with rank x amp aura, now assuming he runs it constantly
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
print("Day after Death")

daniel.reduce_vital("SP",50) #Workout
daniel.cast_skill("Purify",19*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*19*0.2)
skillExt.bank_exp(skillPur.cost['value']*19*0.2)
skillFoc.bank_exp(skillPur.cost['value']*19*0.2)
daniel.cast_skill("Winter",20*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*20*0.2)
skillExt.bank_exp(skillWint.cost['value']*20*0.2)
skillFoc.bank_exp(skillWint.cost['value']*20*0.2)
daniel.cast_skill("Winter",4*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*4*0.2)
skillExt.bank_exp(skillWint.cost['value']*4*0.2)

daniel.add_skill(sk.spring)
daniel.add_skill(sk.summer)
skillSpr = daniel.skills["Spring"]
skillSum = daniel.skills["Summer"]

daniel.regen(24) #Morning of the sixteenth day
daniel.essence_exhange() #Morning after getting kicked out
print("Day 1 of 7 - training at cave")
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.67) #Assume aura focus isn't always active
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*0.32) #8 hours of focusless boost
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))

daniel.reduce_vital("SP",50) #Workout
daniel.cast_skill("Purify",28*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*28*0.2)
skillExt.bank_exp(skillPur.cost['value']*28*0.2)
skillFoc.bank_exp(skillPur.cost['value']*28*0.2)
daniel.cast_skill("Winter",16*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*16*0.2)
skillExt.bank_exp(skillWint.cost['value']*16*0.2)
skillFoc.bank_exp(skillWint.cost['value']*16*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)

daniel.regen(24) #Morning of the seventeeth day
daniel.essence_exhange() #training montage
print("Day 2 of 7 - training at cave")
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.67) #Assume aura focus isn't always active
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*0.32) #8 hours of focusless boost
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))

daniel.reduce_vital("SP",50) #Workout
daniel.cast_skill("Purify",28*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*28*0.2)
skillExt.bank_exp(skillPur.cost['value']*28*0.2)
skillFoc.bank_exp(skillPur.cost['value']*28*0.2)
daniel.cast_skill("Winter",16*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*16*0.2)
skillExt.bank_exp(skillWint.cost['value']*16*0.2)
skillFoc.bank_exp(skillWint.cost['value']*16*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)

daniel.regen(24) #Morning of the eighteenth day
daniel.essence_exhange() #training montage
print("Day 3 of 7 - training at cave")
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.67) #Assume aura focus isn't always active
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*0.32) #8 hours of focusless boost
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))

daniel.reduce_vital("SP",50) #Workout
daniel.cast_skill("Purify",25*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*25*0.2)
skillExt.bank_exp(skillPur.cost['value']*25*0.2)
skillFoc.bank_exp(skillPur.cost['value']*25*0.2)
daniel.cast_skill("Winter",16*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*16*0.2)
skillExt.bank_exp(skillWint.cost['value']*16*0.2)
skillFoc.bank_exp(skillWint.cost['value']*16*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)

daniel.regen(24) #Morning of the nineteenth day
daniel.essence_exhange() #training montage
print("Day 4 of 7 - training at cave")
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.67) #Assume aura focus isn't always active
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*0.32) #8 hours of focusless boost
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))

daniel.reduce_vital("SP",50) #Workout
daniel.cast_skill("Purify",26*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*26*0.2)
skillExt.bank_exp(skillPur.cost['value']*26*0.2)
skillFoc.bank_exp(skillPur.cost['value']*26*0.2)
daniel.cast_skill("Winter",16*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*16*0.2)
skillExt.bank_exp(skillWint.cost['value']*16*0.2)
skillFoc.bank_exp(skillWint.cost['value']*16*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)

daniel.regen(24) #Morning of the twentieth day
daniel.essence_exhange() #training montage
print("Day 5 of 7 - training at cave")
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.67) #Assume aura focus isn't always active
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*0.32) #8 hours of focusless boost
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))

daniel.reduce_vital("SP",50) #Workout
daniel.cast_skill("Purify",26*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*26*0.2)
skillExt.bank_exp(skillPur.cost['value']*26*0.2)
skillFoc.bank_exp(skillPur.cost['value']*26*0.2)
daniel.cast_skill("Winter",16*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*16*0.2)
skillExt.bank_exp(skillWint.cost['value']*16*0.2)
skillFoc.bank_exp(skillWint.cost['value']*16*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)

daniel.regen(24) #Morning of the 21st day
daniel.essence_exhange() #training montage
print("Day 6 of 7 - training at cave")
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.67) #Assume aura focus isn't always active
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*0.32) #8 hours of focusless boost
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))

daniel.reduce_vital("SP",50) #Workout
daniel.cast_skill("Purify",75*(1 + skillAmp.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*75*0.2)
#skillExt.bank_exp(skillPur.cost['value']*29*0.2)
skillFoc.bank_exp(skillPur.cost['value']*75*0.2)
daniel.cast_skill("Winter",16*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*16*0.2)
skillExt.bank_exp(skillWint.cost['value']*16*0.2)
skillFoc.bank_exp(skillWint.cost['value']*16*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)

daniel.regen(24) #Morning of the 22nd day
daniel.essence_exhange() #training montage
print("Day 7 of 7 - training at cave")
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.67) #Assume aura focus isn't always active
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*0.32) #8 hours of focusless boost
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))

daniel.reduce_vital("SP",50) #Workout
daniel.cast_skill("Purify",72*(1 + skillAmp.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*72*0.2)
#skillExt.bank_exp(skillPur.cost['value']*29*0.2)
skillFoc.bank_exp(skillPur.cost['value']*72*0.2)
daniel.cast_skill("Winter",16*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*16*0.2)
skillExt.bank_exp(skillWint.cost['value']*16*0.2)
skillFoc.bank_exp(skillWint.cost['value']*16*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)

daniel.regen(24) #Morning of the 24th day
daniel.essence_exhange() #Gotta open da rocks
print("Opening day")
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.67) #Assume aura focus isn't always active
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*0.32) #8 hours of focusless boost
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))

daniel.reduce_vital("SP",50) #Workout
daniel.cast_skill("Purify",76*(1 + skillAmp.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*76*0.2)
#skillExt.bank_exp(skillPur.cost['value']*29*0.2)
skillFoc.bank_exp(skillPur.cost['value']*76*0.2)
daniel.cast_skill("Winter",16*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*16*0.2)
skillExt.bank_exp(skillWint.cost['value']*16*0.2)
skillFoc.bank_exp(skillWint.cost['value']*16*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)

daniel.regen(24) #Morning of the 24th day
daniel.essence_exhange() #Gotta open da rocks
print("Cave Day 2")
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.67) #Assume aura focus isn't always active
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*0.32) #8 hours of focusless boost
#print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
##print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1))
#print((0.1*skillSpr.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
#print((0.1*skillSum.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))

daniel.cast_skill("Purify",73*(1 + skillAmp.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*73*0.2)
#skillExt.bank_exp(skillPur.cost['value']*29*0.2)
skillFoc.bank_exp(skillPur.cost['value']*73*0.2)
daniel.cast_skill("Winter",20*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*20*0.2)
skillExt.bank_exp(skillWint.cost['value']*20*0.2)
skillFoc.bank_exp(skillWint.cost['value']*20*0.2)
daniel.cast_skill("Winter",4*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*4*0.2)
skillExt.bank_exp(skillWint.cost['value']*4*0.2)

daniel.regen(24) #Morning of the 25th day
daniel.essence_exhange() #Second day of fighting at the cave mouth
print("Cave Day 3, i.e. bear day 2")
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.67) #Assume aura focus isn't always active
daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*0.32) #8 hours of focusless boost
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))


daniel.cast_skill("Purify",85*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
#skillAmp.bank_exp(skillPur.cost['value']*73*0.2)
skillExt.bank_exp(skillPur.cost['value']*85*0.2)
skillFoc.bank_exp(skillPur.cost['value']*85*0.2)
daniel.cast_skill("Winter",20*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*20*0.2)
skillExt.bank_exp(skillWint.cost['value']*20*0.2)
skillFoc.bank_exp(skillWint.cost['value']*20*0.2)
daniel.cast_skill("Winter",4*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*4*0.2)
skillExt.bank_exp(skillWint.cost['value']*4*0.2)

daniel.regen(24) #Morning of the 26th day
daniel.essence_exhange() #Begin timelapse
print("1 of 25 big timelapse")

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33) #Winter focus for 8 hours a day
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Summer

daniel.cast_skill("Purify",44*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
#skillAmp.bank_exp(skillPur.cost['value']*73*0.2)
skillExt.bank_exp(skillPur.cost['value']*44*0.2)
skillFoc.bank_exp(skillPur.cost['value']*44*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Spring",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSpr.cost['value']*8*0.2)
skillExt.bank_exp(skillSpr.cost['value']*8*0.2)
daniel.cast_skill("Spring",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillSpr.cost['value']*8*0.2)
skillExt.bank_exp(skillSpr.cost['value']*8*0.2)
skillFoc.bank_exp(skillSpr.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 27
daniel.essence_exhange() #Begin timelapse
print("2 of 25 big timelapse")

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33) #Winter focus for 8 hours a day
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Summer

daniel.cast_skill("Purify",44*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
#skillAmp.bank_exp(skillPur.cost['value']*73*0.2)
skillExt.bank_exp(skillPur.cost['value']*44*0.2)
skillFoc.bank_exp(skillPur.cost['value']*44*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Spring",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSpr.cost['value']*8*0.2)
skillExt.bank_exp(skillSpr.cost['value']*8*0.2)
daniel.cast_skill("Spring",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillSpr.cost['value']*8*0.2)
skillExt.bank_exp(skillSpr.cost['value']*8*0.2)
skillFoc.bank_exp(skillSpr.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 28
daniel.essence_exhange() #Begin timelapse
print("3 of 25 big timelapse")

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33) #Winter focus for 8 hours a day
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Summer

daniel.cast_skill("Purify",44*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
#skillAmp.bank_exp(skillPur.cost['value']*73*0.2)
skillExt.bank_exp(skillPur.cost['value']*44*0.2)
skillFoc.bank_exp(skillPur.cost['value']*44*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Spring",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSpr.cost['value']*8*0.2)
skillExt.bank_exp(skillSpr.cost['value']*8*0.2)
daniel.cast_skill("Spring",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillSpr.cost['value']*8*0.2)
skillExt.bank_exp(skillSpr.cost['value']*8*0.2)
skillFoc.bank_exp(skillSpr.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 29
daniel.essence_exhange() #Begin timelapse
print("4 of 25 big timelapse")

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33) #Winter focus for 8 hours a day
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Summer

daniel.cast_skill("Purify",43*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
#skillAmp.bank_exp(skillPur.cost['value']*73*0.2)
skillExt.bank_exp(skillPur.cost['value']*43*0.2)
skillFoc.bank_exp(skillPur.cost['value']*43*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Spring",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSpr.cost['value']*8*0.2)
skillExt.bank_exp(skillSpr.cost['value']*8*0.2)
daniel.cast_skill("Spring",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillSpr.cost['value']*8*0.2)
skillExt.bank_exp(skillSpr.cost['value']*8*0.2)
skillFoc.bank_exp(skillSpr.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 30
daniel.essence_exhange() #Begin timelapse
print("5 of 25 big timelapse")

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33) #Winter focus for 8 hours a day
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Summer

daniel.cast_skill("Purify",120*(1 + skillFoc.rank*0.2))
skillFoc.bank_exp(skillPur.cost['value']*120*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Spring",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSpr.cost['value']*8*0.2)
skillExt.bank_exp(skillSpr.cost['value']*8*0.2)
daniel.cast_skill("Spring",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillSpr.cost['value']*8*0.2)
skillExt.bank_exp(skillSpr.cost['value']*8*0.2)
skillFoc.bank_exp(skillSpr.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 31
daniel.essence_exhange() #Begin timelapse
print("6 of 25 big timelapse")

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33) #Winter focus for 8 hours a day
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Summer

daniel.cast_skill("Purify",120*(1 + skillFoc.rank*0.2))
skillFoc.bank_exp(skillPur.cost['value']*120*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Summer",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
daniel.cast_skill("Summer",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
skillFoc.bank_exp(skillSum.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 32
daniel.essence_exhange() #Begin timelapse
print("7 of 25 big timelapse")

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33) #Winter focus for 8 hours a day
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Summer

daniel.cast_skill("Purify",120*(1 + skillFoc.rank*0.2))
skillFoc.bank_exp(skillPur.cost['value']*120*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Summer",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
daniel.cast_skill("Summer",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
skillFoc.bank_exp(skillSum.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 33
daniel.essence_exhange() #Begin timelapse
print("8 of 25 big timelapse")

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33) #Winter focus for 8 hours a day
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Summer

daniel.cast_skill("Purify",115*(1 + skillFoc.rank*0.2))
skillFoc.bank_exp(skillPur.cost['value']*115*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Summer",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
daniel.cast_skill("Summer",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
skillFoc.bank_exp(skillSum.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 34
daniel.essence_exhange() #Begin timelapse
print("9 of 25 big timelapse")

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33) #Winter focus for 8 hours a day
result1 = (0.1 * skillWint.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillWint.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Summer

daniel.cast_skill("Purify",115*(1 + skillFoc.rank*0.2))
skillFoc.bank_exp(skillPur.cost['value']*115*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Summer",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
daniel.cast_skill("Summer",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
skillFoc.bank_exp(skillSum.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 35
daniel.essence_exhange() #Begin timelapse
print("10 of 25 big timelapse")

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33) #Winter focus for 8 hours a day
result1 = (0.1 * skillWint.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillWint.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Spring
result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2)
result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1)
print(f"{result1}  {result2}") #Summer

daniel.cast_skill("Purify",115*(1 + skillFoc.rank*0.2))
skillFoc.bank_exp(skillPur.cost['value']*115*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Summer",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
daniel.cast_skill("Summer",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
skillFoc.bank_exp(skillSum.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 36
daniel.essence_exhange() #Begin timelapse
print("11 of 25 big timelapse")

daniel.add_skill(sk.fall)
skillFal = daniel.skills["Fall"]
daniel.add_skill(sk.aura_synergy)
skillSyn = daniel.skills["Aura Synergy"]
daniel.add_skill(sk.aura_IFF)
skillIFF = daniel.skills["Aura IFF"]

def printStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, synRanks):
    result1 = (0.1 * skillWint.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks)
    result2 = (0.1 * skillWint.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks)
    print(f"{result1}  {result2}") #Spring
    result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks)
    result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks)
    print(f"{result1}  {result2}") #Spring
    result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks)
    result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks)
    print(f"{result1}  {result2}") #Summer
    result1 = (0.01 * skillFal.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks)
    result2 = (0.01 * skillFal.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks)
    print(f"{result1}  {result2}") #Fall

printStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, 31)
print(1 + skillSyn.rank*0.001*31)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*31)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",300) #Getting IFF and synergy ranked up
skillIFF.bank_exp(skillPur.cost['value']*300*0.2)
skillSyn.bank_exp(skillPur.cost['value']*300*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
skillIFF.bank_exp(skillWint.cost['value']*8*0.2)
skillSyn.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Fall",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*3*0.2)
skillExt.bank_exp(skillSum.cost['value']*3*0.2)
skillIFF.bank_exp(skillFal.cost['value']*3*0.2)
skillSyn.bank_exp(skillFal.cost['value']*3*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillFal.cost['value']*8*0.2)
skillExt.bank_exp(skillFal.cost['value']*8*0.2)
skillFoc.bank_exp(skillFal.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)
skillSyn.bank_exp(skillFal.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 37
daniel.essence_exhange() #Begin timelapse
print("12 of 25 big timelapse")

printStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, 32)
print(1 + skillSyn.rank*0.001*32)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*32)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",400) #Getting IFF and synergy ranked up
skillIFF.bank_exp(skillPur.cost['value']*400*0.2)
skillSyn.bank_exp(skillPur.cost['value']*400*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
skillIFF.bank_exp(skillWint.cost['value']*8*0.2)
skillSyn.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*2*0.2)
skillExt.bank_exp(skillSum.cost['value']*2*0.2)
skillIFF.bank_exp(skillFal.cost['value']*2*0.2)
skillSyn.bank_exp(skillFal.cost['value']*2*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillFal.cost['value']*8*0.2)
skillExt.bank_exp(skillFal.cost['value']*8*0.2)
skillFoc.bank_exp(skillFal.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)
skillSyn.bank_exp(skillFal.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 38
daniel.essence_exhange() #Begin timelapse
print("13 of 25 big timelapse")

printStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, 33)
print(1 + skillSyn.rank*0.001*33)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*33)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",400) #Getting IFF and synergy ranked up
skillIFF.bank_exp(skillPur.cost['value']*400*0.2)
skillSyn.bank_exp(skillPur.cost['value']*400*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
skillIFF.bank_exp(skillWint.cost['value']*8*0.2)
skillSyn.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*2*0.2)
skillExt.bank_exp(skillSum.cost['value']*2*0.2)
skillIFF.bank_exp(skillFal.cost['value']*2*0.2)
skillSyn.bank_exp(skillFal.cost['value']*2*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillFal.cost['value']*8*0.2)
skillExt.bank_exp(skillFal.cost['value']*8*0.2)
skillFoc.bank_exp(skillFal.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)
skillSyn.bank_exp(skillFal.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 39
daniel.essence_exhange() #Begin timelapse
print("14 of 25 big timelapse")

printStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, 34)
print(1 + skillSyn.rank*0.001*34)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*34)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting IFF and synergy ranked up
skillIFF.bank_exp(skillPur.cost['value']*420*0.2)
skillSyn.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
skillIFF.bank_exp(skillWint.cost['value']*8*0.2)
skillSyn.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*2*0.2)
skillExt.bank_exp(skillSum.cost['value']*2*0.2)
skillIFF.bank_exp(skillFal.cost['value']*2*0.2)
skillSyn.bank_exp(skillFal.cost['value']*2*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillFal.cost['value']*8*0.2)
skillExt.bank_exp(skillFal.cost['value']*8*0.2)
skillFoc.bank_exp(skillFal.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)
skillSyn.bank_exp(skillFal.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 40
daniel.essence_exhange() #Begin timelapse
print("15 of 25 big timelapse")

printStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, 34)
print(1 + skillSyn.rank*0.001*34)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*34)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting IFF and synergy ranked up
skillIFF.bank_exp(skillPur.cost['value']*420*0.2)
skillSyn.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
skillIFF.bank_exp(skillWint.cost['value']*8*0.2)
skillSyn.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*2*0.2)
skillExt.bank_exp(skillSum.cost['value']*2*0.2)
skillIFF.bank_exp(skillFal.cost['value']*2*0.2)
skillSyn.bank_exp(skillFal.cost['value']*2*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillFal.cost['value']*8*0.2)
skillExt.bank_exp(skillFal.cost['value']*8*0.2)
skillFoc.bank_exp(skillFal.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)
skillSyn.bank_exp(skillFal.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 41
daniel.essence_exhange() #Begin timelapse
print("16 of 25 big timelapse")

printStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, 35)
print(1 + skillSyn.rank*0.001*35)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*35)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting IFF and synergy ranked up
skillIFF.bank_exp(skillPur.cost['value']*420*0.2)
skillSyn.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
skillIFF.bank_exp(skillWint.cost['value']*8*0.2)
skillSyn.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*2*0.2)
skillExt.bank_exp(skillSum.cost['value']*2*0.2)
skillIFF.bank_exp(skillFal.cost['value']*2*0.2)
skillSyn.bank_exp(skillFal.cost['value']*2*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillFal.cost['value']*8*0.2)
skillExt.bank_exp(skillFal.cost['value']*8*0.2)
skillFoc.bank_exp(skillFal.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)
skillSyn.bank_exp(skillFal.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 42
daniel.essence_exhange() #Begin timelapse
print("17 of 25 big timelapse")

printStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, 35)
print(1 + skillSyn.rank*0.001*35)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*35)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting IFF and synergy ranked up
skillIFF.bank_exp(skillPur.cost['value']*420*0.2)
skillSyn.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
skillIFF.bank_exp(skillWint.cost['value']*8*0.2)
skillSyn.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*2*0.2)
skillExt.bank_exp(skillSum.cost['value']*2*0.2)
skillIFF.bank_exp(skillFal.cost['value']*2*0.2)
skillSyn.bank_exp(skillFal.cost['value']*2*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillFal.cost['value']*8*0.2)
skillExt.bank_exp(skillFal.cost['value']*8*0.2)
skillFoc.bank_exp(skillFal.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)
skillSyn.bank_exp(skillFal.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 43
daniel.essence_exhange() #Begin timelapse
print("18 of 25 big timelapse")

daniel.add_skill(sk.aura_compression)
skillCom = daniel.skills["Aura Compression"]

def printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, synRanks):
    comFactor = skillCom.rank * 0.02
    comWintFoc = max(1,1 + (comFactor * (((skillWint.rank + 10) * 3 * (1 + skillSyn.rank*0.001*synRanks)) - 10))) #compress down to 10 meters
    comWint = max(1,1 + (comFactor * (((skillWint.rank + 10) * (1 + skillSyn.rank*0.001*synRanks)) - 10))) #compress down to 10 meters
    comSprFoc = max(1,1 + (comFactor * (((skillSpr.rank + 10) * 3 * (1 + skillSyn.rank*0.001*synRanks)) - 10))) #compress down to 10 meters
    comSpr = max(1,1 + (comFactor * (((skillSpr.rank + 10) * (1 + skillSyn.rank*0.001*synRanks)) - 10))) #compress down to 10 meters
    comSumFoc = max(1,1 + (comFactor * (((skillSum.rank + 10) * 3 * (1 + skillSyn.rank*0.001*synRanks)) - 10))) #compress down to 10 meters
    comSum = max(1,1 + (comFactor * (((skillSum.rank + 10) * (1 + skillSyn.rank*0.001*synRanks)) - 10))) #compress down to 10 meters
    comFalFoc = max(1,1 + (comFactor * (((skillFal.rank + 10) * 3 * (1 + skillSyn.rank*0.001*synRanks)) - 10))) #compress down to 10 meters
    comFal = max(1,1 + (comFactor * (((skillFal.rank + 10) * (1 + skillSyn.rank*0.001*synRanks)) - 6))) #6 meter for fall to just barely break 100% 

    result1 = (0.1 * skillWint.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks) * comWintFoc
    result2 = (0.1 * skillWint.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks) * comWint
    result3 = (0.1 * skillWint.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks) #noncompressed overnight focus boost
    print(f"{result1}  {result2} {result3}") #Winter
    result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks) * comSprFoc
    result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks) * comSpr
    print(f"{result1}  {result2}") #Spring
    result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks) * comSumFoc
    result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks) * comSum
    print(f"{result1}  {result2}") #Summer
    result1 = (0.01 * skillFal.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks) * comFalFoc
    result2 = (0.01 * skillFal.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks) * comFal
    print(f"{result1}  {result2}") #Fall

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 36)
print(1 + skillSyn.rank*0.001*36)
print(skillCom.rank)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*36)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting compression ranked up
skillCom.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
skillIFF.bank_exp(skillWint.cost['value']*8*0.2)
skillSyn.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)
skillSyn.bank_exp(skillFal.cost['value']*8*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillFal.cost['value']*8*0.2)
skillExt.bank_exp(skillFal.cost['value']*8*0.2)
skillFoc.bank_exp(skillFal.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)
skillSyn.bank_exp(skillFal.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 44
daniel.essence_exhange() #Begin timelapse
print("19 of 25 big timelapse")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 36)
print(1 + skillSyn.rank*0.001*36)
print(skillCom.rank)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*36)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting compression ranked up
skillCom.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
skillAmp.bank_exp(skillWint.cost['value']*8*0.2)
skillExt.bank_exp(skillWint.cost['value']*8*0.2)
skillFoc.bank_exp(skillWint.cost['value']*8*0.2)
skillIFF.bank_exp(skillWint.cost['value']*8*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillSum.cost['value']*8*0.2)
skillExt.bank_exp(skillSum.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillFal.cost['value']*8*0.2)
skillExt.bank_exp(skillFal.cost['value']*8*0.2)
skillFoc.bank_exp(skillFal.cost['value']*8*0.2)
skillIFF.bank_exp(skillFal.cost['value']*8*0.2)

daniel.regen(24) #Morning of the day 45
daniel.essence_exhange() #Begin timelapse
print("20 of 25 big timelapse")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 37)
print(1 + skillSyn.rank*0.001*37)
print(skillCom.rank)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*37)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting compression ranked up
skillCom.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))

daniel.regen(24) #Morning of the day 46
daniel.essence_exhange() #Begin timelapse
print("21 of 25 big timelapse")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 37)
print(1 + skillSyn.rank*0.001*37)
print(skillCom.rank)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*37)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting compression ranked up
skillCom.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))

daniel.regen(24) #Morning of the day 47
daniel.essence_exhange() #Begin timelapse
print("22 of 25 big timelapse")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 38)
print(1 + skillSyn.rank*0.001*38)
print(skillCom.rank)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*38)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting compression ranked up
skillCom.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))

daniel.regen(24) #Morning of the day 48
daniel.essence_exhange() #Begin timelapse
print("23 of 25 big timelapse")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 38)
print(1 + skillSyn.rank*0.001*38)
print(skillCom.rank)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*38)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting compression ranked up
skillCom.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))

daniel.regen(24) #Morning of the day 49
daniel.essence_exhange() #Begin timelapse
print("24 of 25 big timelapse")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 38)
print(1 + skillSyn.rank*0.001*38)
print(skillCom.rank)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*38)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting compression ranked up
skillCom.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))

daniel.regen(24) #Morning of the day 50
daniel.essence_exhange() #Begin timelapse
print("25 of 25 big timelapse")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 39)
print(1 + skillSyn.rank*0.001*39)
print(skillCom.rank)

daniel.add_vital("MP",daniel.vitals[5]*(0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2)*0.33*(1 + skillSyn.rank*0.001*39)) #Winter focus for 8 hours a day
daniel.cast_skill("Purify",420) #Getting compression ranked up
skillCom.bank_exp(skillPur.cost['value']*420*0.2)
daniel.cast_skill("Winter",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
daniel.cast_skill("Fall",8*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))

daniel.regen(24) #Morning of day 51
daniel.essence_exhange() #The next arc
print("Delveday")

daniel.regen(24) #Morning of day 52
daniel.essence_exhange() #The next arc
print("Back to town")

daniel.regen(24) #Morning of day 53
daniel.essence_exhange() #The next arc
print("On our way to Doduo")

daniel.regen(24) #Morning of day 54
daniel.essence_exhange() #The next arc
print("Travelling to Diglett")

daniel.regen(24) #Morning of day 55
daniel.essence_exhange() #The next arc
print("Made it to Duodecillion")

daniel.regen(24) #Morning of day 56
daniel.essence_exhange() #The next arc
print("Overnight in Daryl")

daniel.regen(24) #Morning of day 57
daniel.essence_exhange() #The next arc
print("Travel")

daniel.regen(24) #Morning of day 58
daniel.essence_exhange() #The next arc
print("Travel")

daniel.regen(24) #Morning of day 59
daniel.essence_exhange() #The next arc
print("Back at lair")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 39)
print(1 + skillSyn.rank*0.001*39)
print(skillCom.rank)


daniel.update_vitals()
daniel.update_free_attributes()
daniel.printCharSheet(altCol= False)
print(daniel.vitals)
print(daniel.currVitals)
print(daniel.general_statistics)
print(daniel.hours)