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
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1))
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
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
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
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
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
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
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
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
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
print((0.1*skillWint.rank)*(1 + skillAmp.rank*0.1)*(1 + skillFoc.rank*0.2))
print("7 of 7, skar evening")

daniel.reduce_vital("SP",100) #Workout
daniel.cast_skill("Purify",20*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
skillAmp.bank_exp(skillPur.cost['value']*20*0.2)
skillExt.bank_exp(skillPur.cost['value']*20*0.2)
skillFoc.bank_exp(skillPur.cost['value']*20*0.2)
daniel.cast_skill("Winter",12*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2))
skillAmp.bank_exp(skillWint.cost['value']*12*0.2)
skillExt.bank_exp(skillWint.cost['value']*12*0.2)
daniel.regen(14) #regen before fight?

#daniel.regen(24) #Morning of the fifteenth day
#daniel.essence_exhange() #Morning after talking to Skar"""

daniel.update_vitals()
daniel.update_free_attributes()
daniel.printCharSheet(altCol= False)
