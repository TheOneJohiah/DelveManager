# Witness my jank!
import awakened as aw;

# Example usage
t = aw.Awakened(name='Teston Lautts',attributes = [10, 10, 10, 10, 10, 60], level = 20, character_class = aw.worker)
t.add_skill(aw.intrinsic_clarity, starting_level=10)
t.add_skill(aw.intrinsic_focus, starting_level=10)
t.add_experience(2000)  # Set the character's current experience
t.printCharSheet()
