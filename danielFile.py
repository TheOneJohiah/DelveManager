import awakened as aw, delve_Class as dc, skill as sk, timeline as tl

#Purify>Winter>Amplify Aura>Intrinsic Clarity>Extend Aura>Aura Focus

daniel = aw.Awakened(name='Daniel',attributes = [10, 10, 10, 10, 10, 10, 10, 10], level = 5, level_cap=12)
daniel.date = daniel.date.plus(tl.Duration(int(50.5*86400000)))
daniel.set_class(dc.dynamo)
daniel.add_experience(200000)
daniel.unlock_tier("Utility Auras",1)
daniel.unlock_tier("Magical Utility",1)
daniel.unlock_tier("Defensive Auras",1)
daniel.unlock_tier("Aura Metamagic",1)
daniel.unlock_tier("Utility Auras",2)
daniel.unlock_tier("Magical Utility",2)
daniel.unlock_tier("Defensive Auras",2)
daniel.unlock_tier("Aura Metamagic",2)
daniel.add_skill(sk.purify,10)
daniel.add_skill(sk.winter,10)
daniel.add_skill(sk.amplify_aura,10)
skillPur = daniel.skills["Purify"]
skillWint = daniel.skills["Winter"]
skillAmp = daniel.skills["Amplify Aura"]
daniel.add_skill(sk.intrinsic_clarity(),10)
daniel.add_skill(sk.intrinsic_focus(),10)
daniel.add_skill(sk.extend_aura,10)
skillExt = daniel.skills["Extend Aura"]
daniel.add_skill(sk.aura_focus,10) #FOCUS TIME WOO
skillFoc = daniel.skills["Aura Focus"]
daniel.add_skill(sk.spring,5)
daniel.add_skill(sk.summer,5)
skillSpr = daniel.skills["Spring"]
skillSum = daniel.skills["Summer"]
daniel.add_skill(sk.fall,9)
skillFal = daniel.skills["Fall"]
daniel.add_skill(sk.aura_synergy,10)
skillSyn = daniel.skills["Aura Synergy"]
daniel.add_skill(sk.aura_IFF,10)
skillIFF = daniel.skills["Aura IFF"]
daniel.update_level_cap(13)
daniel.add_experience(200000)
daniel.unlock_tier("Aura Metamagic",3)
daniel.add_skill(sk.aura_compression,8)
skillCom = daniel.skills["Aura Compression"]

daniel.raise_attribute(5,130)
skillSpr.bank_exp(327)
skillFal.bank_exp(2108)
skillSum.bank_exp(572)
skillCom.bank_exp(16800)

def printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, synRanks):
    danAuras = [[]] * 4
    danAuras[0] = [0]*3 #Winter
    danAuras[1] = [0]*3 #Spring
    danAuras[2] = [0]*3 #Summer
    danAuras[3] = [0]*3 #Fall

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
    danAuras[0][0] = result1 * 100
    danAuras[0][1] = result2 * 100
    danAuras[0][2] = result3 * 100
    print(f"{result1}  {result2} {result3}") #Winter, all buffs | no foc 10 m compression | foc no comp
    result1 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks) * comSprFoc
    result2 = (0.1 * skillSpr.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks) * comSpr
    danAuras[1][0] = result1 * 100
    danAuras[1][1] = result2 * 100
    print(f"{result1}  {result2}") #Spring, all buffs | no foc 10 m compression | foc no comp
    result1 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks) * comSumFoc
    result2 = (0.1 * skillSum.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks) * comSum
    danAuras[2][0] = result1 * 100
    danAuras[2][1] = result2 * 100
    print(f"{result1}  {result2}") #Summer, all buffs | no foc 10 m compression | foc no comp
    result1 = (0.01 * skillFal.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillFoc.rank * 0.2) * (1 + skillSyn.rank*0.001*synRanks) * comFalFoc
    result2 = (0.01 * skillFal.rank) * (1 + skillAmp.rank * 0.1) * (1 + skillSyn.rank*0.001*synRanks) * comFal
    danAuras[3][0] = result1 * 100
    danAuras[3][1] = result2 * 100
    print(f"{result1}  {result2}") #Fall

    return danAuras

daniel.regen(16) #advance to evening of 50

def overNight(daniel, increment, incrementTotal, boost):
    #Winter focus for 8 [incrementTotal] hours (.33 of) a day
    i=0
    while i<incrementTotal: #Nighttime winter
        daniel.regen(increment,[0,0,boost])
        daniel.cast_skill("Winter",increment*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2)) #Overnight winter regen costs
        i += 1
    daniel.essence_exhange() #End of night

overNight(daniel, 1, 8, 834)
print("Day 51, first delving")

daniel.regen(0.016,[0,0,10628]) #A single minute of regen, ~900 mana
i=0
while i<240: #Training for 4 hours
    daniel.cast_skill("Purify",6) #Getting compression ranked up
    daniel.regen(0.016,[0,0,10628]) #A single minute of regen, ~900 mana
    i += 1
skillCom.bank_exp(skillPur.cost['value']*6*240*0.2)

daniel.cast_skill("Winter",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Winter in the caves
daniel.regen(2.984,[0,0,1070])
daniel.cast_skill("Winter",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Winter in the caves
daniel.regen(3,[0,0,1070])
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(2,[0,0,0])
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(2,[0,0,0])
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(2,[0,0,0])

overNight(daniel, 1, 8, 834)
print("Day 52, Back to town to buy a pair of horses, then off to Deciduous")

daniel.regen(0.016,[0,0,10628]) #A single minute of regen, ~900 mana
i=0
while i<240: #Training for 4 hours
    daniel.cast_skill("Purify",6) #Getting compression ranked up
    daniel.regen(0.016,[0,0,10628]) #A single minute of regen, ~900 mana
    i += 1
skillCom.bank_exp(skillPur.cost['value']*6*240*0.2)

daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(2.984,[0,1070,0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,1070,0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,1070,0])
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(2,[0,0,0])
daniel.cast_skill("Fall",1*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(1,[0,0,0])

overNight(daniel, 1, 8, 834)
print("Day 53, On our way to Doduo")

daniel.regen(0.016,[0,0,10628]) #A single minute of regen, ~900 mana
i=0
while i<240: #Training for 4 hours
    daniel.cast_skill("Purify",6) #Getting compression ranked up
    daniel.regen(0.016,[0,0,10628]) #A single minute of regen, ~900 mana
    i += 1
skillCom.bank_exp(skillPur.cost['value']*6*240*0.2)

daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(2.984,[0,380,0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,380,0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,380,0])
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(2,[0,0,0])
daniel.cast_skill("Fall",1*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(1,[0,0,0])

overNight(daniel, 1, 8, 834)
print("Day 54, Travelling to Diglett")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 39)
print(1 + skillSyn.rank*0.001*39)
print(skillCom.rank)

daniel.regen(0.016,[0,0,11852]) #A single minute of regen, ~900 mana
i=0
while i<240: #Training for 4 hours
    daniel.cast_skill("Purify",6) #Getting compression ranked up
    daniel.regen(0.016,[0,0,11852]) #A single minute of regen, ~900 mana
    i += 1
skillCom.bank_exp(skillPur.cost['value']*6*240*0.2)

daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(2.984,[0,410,0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,410,0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,410,0])
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(2,[0,0,0])
daniel.cast_skill("Fall",1*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(1,[0,0,0])

overNight(daniel, 1, 8, 834)
print("Day 55, Made it to Duodecillion")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 40)
print(1 + skillSyn.rank*0.001*40)
print(skillCom.rank)

daniel.regen(0.016,[0,0,11872]) #A single minute of regen, ~900 mana
i=0
while i<240: #Training for 4 hours
    daniel.cast_skill("Purify",6) #Getting compression ranked up
    daniel.regen(0.016,[0,0,11872]) #A single minute of regen, ~900 mana
    i += 1
skillCom.bank_exp(skillPur.cost['value']*6*240*0.2)

daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(2.984,[0,417,0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,417,0])
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(6,[0,0,0]) #Passing time in the city, not training

overNight(daniel, 1, 8, 840)
print("Day 56, Overnight in Daryl")

printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 40)
print(1 + skillSyn.rank*0.001*40)
print(skillCom.rank)

daniel.regen(0.016,[0,0,11872]) #A single minute of regen, ~900 mana
i=0
while i<240: #Training for 4 hours
    daniel.cast_skill("Purify",6) #Getting compression ranked up
    daniel.regen(0.016,[0,0,11872]) #A single minute of regen, ~900 mana
    i += 1
skillCom.bank_exp(skillPur.cost['value']*6*240*0.2)

daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(2.984,[0,417,0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,417,0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,417,0])
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(2,[0,0,0])
daniel.cast_skill("Fall",1*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(1,[0,0,0])

overNight(daniel, 1, 8, 840)
print("Day 57, Travel")

danAuras = printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 41)
print(1 + skillSyn.rank*0.001*41)
print(skillCom.rank)

daniel.regen(0.016,[0,0,danAuras[0][0]]) #A single minute of regen, ~900 mana
i=0
while i<240: #Training for 4 hours
    daniel.cast_skill("Purify",6) #Getting compression ranked up
    daniel.regen(0.016,[0,0,danAuras[0][0]]) #A single minute of regen, ~900 mana
    i += 1
skillCom.bank_exp(skillPur.cost['value']*6*240*0.2)

daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(2.984,[0,danAuras[1][1],0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,danAuras[1][1],0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,danAuras[1][1],0])
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(2,[0,0,0])
daniel.cast_skill("Fall",1*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(1,[0,0,0])

overNight(daniel, 1, 8, danAuras[0][2])
print("Day 58, Travel")

danAuras = printCompStats(daniel, skillWint, skillSpr, skillSum, skillFal, skillAmp, skillFoc, skillSyn, skillCom, 41)
print(1 + skillSyn.rank*0.001*41)
print(skillCom.rank)

daniel.regen(0.016,[0,0,danAuras[0][0]]) #A single minute of regen, ~900 mana
i=0
while i<240: #Training for 4 hours
    daniel.cast_skill("Purify",6) #Getting compression ranked up
    daniel.regen(0.016,[0,0,danAuras[0][0]]) #A single minute of regen, ~900 mana
    i += 1
skillCom.bank_exp(skillPur.cost['value']*6*240*0.2)

daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(2.984,[0,danAuras[1][1],0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,danAuras[1][1],0])
daniel.cast_skill("Spring",3*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)) #Spring traveling
daniel.regen(3,[0,danAuras[1][1],0])
daniel.cast_skill("Fall",2*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(2,[0,0,0])
daniel.cast_skill("Fall",1*(1 + skillAmp.rank*0.2)*(1 + skillExt.rank*0.2)*(1 + skillFoc.rank*0.2))
daniel.regen(1,[0,0,0])

overNight(daniel, 1, 8, danAuras[0][2])
print("Day 59, Back at lair, clearing out the hounds, seeing the blue")

"""overNight(daniel, 1, 8, danAuras[0][2])
print("Day 60, Crafting and army scout encounter")

overNight(daniel, 1, 8, danAuras[0][2])
print("Day 61, Day 1 marching with village")

overNight(daniel, 1, 8, danAuras[0][2])
print("Day 62, Day 2 marching with village")

daniel.regen(24) #Morning of day 63
daniel.essence_exhange()
print("Day 3 marching with village, arriving")

daniel.regen(24) #Morning of day 64
daniel.essence_exhange()
print("Prep for travel and twiddling thumbs in town")

daniel.regen(24) #Morning of day 65
daniel.essence_exhange()
print("Ambush army harried back over the border by silver team")

daniel.regen(24) #Morning of day 66
daniel.essence_exhange()
print("Travel")

daniel.regen(24) #Morning of day 67
daniel.essence_exhange()
print("Travel")

daniel.regen(24) #Morning of day 68
daniel.essence_exhange()
print("Arriving back at quillcaves")

## Add 28 days of training

# Day 96?


daniel.update_level_cap(16)
daniel.add_experience(230) #XP from lava boy
daniel.essence_exhange()"""

daniel.update_vitals()
daniel.update_free_attributes()
daniel.printCharSheet(altCol= False)
print(daniel.vitals)
print(daniel.currVitals)
print(daniel.general_statistics)