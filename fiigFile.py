import awakened as aw, delve_Class as dc, skill as sk, timeline as tl

fiig = aw.Awakened(name='Fiig',attributes = [10, 10, 60, 10, 10, 10, 10, 10], level = 5, level_cap=21)
fiig.date = fiig.date.plus(tl.Duration(int(18.5*86400000)))

fiig.set_class(dc.tortugo)

fiig.add_experience(3415)
fiig.unlock_tier("Physical Passives",1)
fiig.unlock_tier("Physical Passives",2)
fiig.raise_attribute(2, 10)

fiig.add_skill(sk.strength_of_arm,4)
fiig.add_skill(sk.rugged_defense,5)
fiig.add_skill(sk.turtle_skin)
fiig.add_skill(sk.heavy_armor)
fiig.add_skill(sk.intrinsic_resistance,3)
fiig.add_skill(sk.turtle_kata)

skillStrength = fiig.skills["Strength of Arm"]
skillRuggDef = fiig.skills["Rugged Defense"]
skillTurtSkin = fiig.skills["Turtle Skin"]
skillIntrinResis = fiig.skills["Intrinsic Resistance"]
skillTurt = fiig.skills["Turtle Kata"]

skillStrength.bank_exp(110)
skillRuggDef.bank_exp(590)
skillIntrinResis.bank_exp(10)

fiig.essence_exhange()

fiig.update_vitals()
fiig.update_free_attributes()
fiig.printCharSheet(altCol= False)
print(fiig.vitals)
print(fiig.currVitals)
print(fiig.general_statistics)