import awakened as aw, delve_Class as dc, skill as sk, timeline as tl

henrik = aw.Awakened(name='Henrik',attributes = [10, 10, 10, 10, 60, 10, 10, 10], level = 5, level_cap=21)
henrik.date = henrik.date.plus(tl.Duration(int(50.5*86400000)))
henrik.set_class(dc.animus)
henrik.add_experience(200000)
henrik.raise_attribute(4,40)
henrik.unlock_tier("Magical Utility",1)
henrik.unlock_tier("Magical Utility",2)
henrik.unlock_tier("Elemental Enhancement",1)
henrik.unlock_tier("Elemental Enhancement",2)
henrik.unlock_tier("Elemental Archer",1)
henrik.unlock_tier("Elemental Archer",2)
henrik.add_experience(200000)
henrik.unlock_tier("Sharpshooting",1)
henrik.unlock_tier("Sharpshooting",2)
henrik.unlock_tier("Equipment Use",1)
henrik.unlock_tier("Equipment Use",2)
henrik.add_experience(200000)
henrik.add_skill(sk.fire_arrow,10)
henrik.add_skill(sk.ice_arrow,10)
henrik.add_skill(sk.intrinsic_clarity(),10)
henrik.add_skill(sk.intrinsic_focus(),10)
henrik.add_skill(sk.drilling_shot,6)
henrik.add_skill(sk.concussive_blows)
henrik.add_skill(sk.empowered_overwear)
henrik.add_skill(sk.empowered_underwear)
henrik.add_skill(sk.empowered_amulet)
henrik.add_skill(sk.hardened_arrowheads,4)
henrik.add_skill(sk.magical_synergy(),7)
henrik.add_skill(sk.stygian_arrow)
henrik.add_skill(sk.stubbornness)
henrik.add_skill(sk.radiant_arrow,4)

skillHarArr = henrik.skills["Hardened Arrowheads"]
skillRadiant = henrik.skills["Radiant Arrow"]
skillConcuss = henrik.skills["Concussive Blows"]
magicSyn = henrik.skills["Magical Synergy"]
drillShot = henrik.skills["Drilling Shot"]

skillHarArr.bank_exp(165)
skillRadiant.bank_exp(2200)
skillConcuss.bank_exp(80)
magicSyn.bank_exp(3700)
drillShot.bank_exp(1260)

henrik.essence_exhange()

henrik.update_vitals()
henrik.update_free_attributes()
henrik.printCharSheet(altCol= False)
print(henrik.vitals)
print(henrik.currVitals)
print(henrik.general_statistics)