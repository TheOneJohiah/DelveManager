# Witness my jank!
import awakened as aw;
import delve_Class as dClass;
import skill as Skill;

# Example usage
t = aw.Awakened(name='Teston Lautts',attributes = [10, 10, 200, 10, 10, 10], level = 20, character_class = dClass.shieldwielding_defender)
t.add_skill(Skill.intrinsic_clarity, starting_level=10)
t.add_skill(Skill.intrinsic_focus, starting_level=10)
t.add_experience(2000)  # Set the character's current experience
t.printCharSheet()
