import awakened as aw, delve_Class as dc, skill as sk, timeline as tl

micah = aw.Awakened(name='Micah Redacted',attributes = [10, 10, 10, 10, 10, 10, 10, 10], level = 5, level_cap=12)
micah.date = micah.date.plus(tl.Duration(int(51.5*86400000)))
micah.set_class(dc.geomancer)
micah.add_experience(200000)
micah.unlock_tier("Magical Utility",1)
micah.unlock_tier("Magical Utility",2)
micah.unlock_tier("Geoevocation",1)
micah.unlock_tier("Geoevocation",2)
micah.unlock_tier("Earth Manipulation",1)
micah.unlock_tier("Earth Manipulation",2)
micah.update_level_cap(15)
micah.add_experience(200000)
micah.unlock_tier("Earth Manipulation",3)
micah.add_experience(200000)

micah.raise_attribute(4, 75)
micah.raise_attribute(5, 15)
micah.add_skill(sk.stonebolt,8)
micah.add_skill(sk.rock_push,7)
micah.add_skill(sk.intrinsic_focus(),10)
micah.add_skill(sk.intrinsic_clarity(),10)
micah.add_skill(sk.stone_spray,5)
micah.add_skill(sk.stone_spear,11)
micah.add_skill(sk.magical_synergy(),10)
micah.add_skill(sk.earth_affinity,10)
micah.add_skill(sk.earthmolding,7)
micah.add_skill(sk.rooted,9)
micah.add_skill(sk.liquefaction,10)
micah.add_skill(sk.stoneset,5)
micah.add_skill(sk.stonemolding,10)

rock = micah.skills["Rock Push"]
spear = micah.skills["Stone Spear"]
spray = micah.skills["Stone Spray"]
bolt = micah.skills["Stonebolt"]
eMold = micah.skills["Earthmolding"]
root = micah.skills["Rooted"]
stoneSet = micah.skills["Stoneset"]
rock.bank_exp(200)
spear.bank_exp(7625)
bolt.bank_exp(750)
eMold.bank_exp(4300)
root.bank_exp(4300)
stoneSet.bank_exp(1775)

micah.update_level_cap(16)
micah.essence_exhange()

micah.update_vitals()
micah.update_free_attributes()
micah.printCharSheet(altCol= False)
print(micah.vitals)
print(micah.currVitals)
print(micah.general_statistics)