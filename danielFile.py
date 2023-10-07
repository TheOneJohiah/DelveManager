import awakened as aw;
import delve_Class as dc;
import skill as sk;

#Purify>Winter>Amplify Aura>Intrinsic Clarity>Extend Aura>Aura Focus

daniel = aw.Awakened(name='Daniel',attributes = [10, 10, 10, 10, 10, 10, 10, 10], level = 5, level_cap=12)
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
daniel.add_skill(sk.aura_compression,10)
skillCom = daniel.skills["Aura Compression"]

daniel.raise_attribute(5,130)
skillSpr.bank_exp(327)
skillFal.bank_exp(2108)
skillSum.bank_exp(572)

daniel.essence_exhange()

daniel.update_vitals()
daniel.update_free_attributes()
daniel.printCharSheet(altCol= False)
print(daniel.vitals)
print(daniel.currVitals)
print(daniel.general_statistics)