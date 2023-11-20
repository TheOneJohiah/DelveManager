import awakened as aw, delve_Class as dc, skill as sk, timeline as tl

mo = aw.Awakened(name='Mo',attributes = [10, 10, 10, 10, 10, 10, 10, 10], level = 5, level_cap=21)
mo.date = mo.date.plus(tl.Duration(int(50.5*86400000)))
mo.add_skill(sk.firebolt,10)
mo.add_experience(10000)
mo.raise_attribute(4, 54)
mo.raise_attribute(5, 6)

mo.unlock_tier("Fire Evocation",1)
mo.add_experience(10000)
mo.unlock_tier("Fire Evocation",2)
mo.add_experience(10000)
mo.unlock_tier("Fire Manipulation",1)
mo.add_experience(10000)
mo.unlock_tier("Fire Manipulation",2)
mo.add_experience(10000)

mo.add_skill(sk.smoke_burst,9) #Flame burst time
mo.add_skill(sk.fire_affinity,8) #Unlocked with five ranks in fire evocation
mo.add_skill(sk.heat_mastery,6) #Unlocked with firebolt level 5
mo.add_skill(sk.smoke_cloud)
skillFiAff = mo.skills["Fire Affinity"]
skillHeMas = mo.skills["Heat Mastery"]
skillSmCld = mo.skills["Smoke Cloud"]
skillSmBst = mo.skills["Smoke Burst"]

skillFiAff.bank_exp(1046)
skillHeMas.bank_exp(2346)
skillSmBst.bank_exp(6650)

mo.essence_exhange()

mo.update_vitals()
mo.update_free_attributes()
mo.printCharSheet(altCol= False)
print(mo.vitals)
print(mo.currVitals)
print(mo.general_statistics)