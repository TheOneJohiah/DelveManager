# Witness my jank!
import awakened as aw;
from jinja2 import Template;

temp = Template(open('CharSheetTemplate.html').read())

# Example usage
ac = aw.Awakened(name='Teston Lautts',attributes = [10, 10, 10, 10, 10, 60], level = 20, character_class = aw.worker)
ac.add_skill(aw.intrinsic_clarity, starting_level=10)
ac.add_skill(aw.intrinsic_focus, starting_level=10)
ac.add_experience(2000)  # Set the character's current experience

pluscol = False
if (ac.free_attributes > 0 or ac.used_skill_points > 0):
    pluscol = True

sheet = open('CharSheet.html','w')
sheet.write( temp.render(
            pluscol = pluscol,
            Name = ac.name,
            Class = ac.character_class.name,
            Level = ac.level.__str__(),
            LevelCap = ac.level_cap.__str__(),
            FreeStat = ac.free_attributes.__str__(),
            FreeSkill = ac.used_skill_points.__str__(),
            CurrXP = ac.experience.__str__(),
            NextXP = ac.calculate_required_experience().__str__(),
            TotXP = "#todo Add Total XP",
            
            maxHP = ac.vitals[0].__str__(),
            rgnHP = ac.vitals[1].__str__(),
            maxSP = ac.vitals[2].__str__(),
            rgnSP = ac.vitals[3].__str__(),
            maxMP = ac.vitals[4].__str__(),
            rgnMP = ac.vitals[5].__str__(),

            basSTR = ac.attributes[0].__str__(),
            basRCV = ac.attributes[1].__str__(),
            basEND = ac.attributes[2].__str__(),
            basVGR = ac.attributes[3].__str__(),
            basFCS = ac.attributes[4].__str__(),
            basCLR = ac.attributes[5].__str__(),
    ))
sheet.close()
