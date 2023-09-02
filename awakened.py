import math
from jinja2 import Template;

class Class:
    def __init__(self, name, rarity, notes, attribute_effect, tree_effect, additional_effect):
        self.name = name
        self.rarity = rarity
        self.notes = notes
        self.attribute_effect = attribute_effect  # Now an array [str, rec, end, vig, foc, cla]
        self.tree_effect = tree_effect
        self.additional_effect = additional_effect
        
    def meets_requirements(self, awakened):
        ##Todo: Reimplement these requirements in a better way
        return True

unclassed = Class("Unclassed", "Common", "Everyone's first class", attribute_effect=[1, 1, 1, 1, 1, 1], tree_effect={}, additional_effect=None)

worker = Class("Worker", "Common", "Warning: Experience may no longer be gained through combat", attribute_effect=[1, 1, 1, 1, 1, 1], tree_effect={}, additional_effect="50% boost to non-combat skills")

# Create specific classes
dynamo = Class("Dynamo", "Rare", "Master of energy manipulation", attribute_effect=[1, 1, 1, 1, 1, 3], tree_effect={}, additional_effect=None)

shieldwielding_defender = Class("Shieldwielding Defender", "Uncommon", "Master of defense with a shield", attribute_effect=[1, 1, 1.5, 1, 1, 1], tree_effect={"shieldwielding": 3}, additional_effect=None)

geomancer = Class("Geomancer", "Uncommon", "A dirty dude", attribute_effect=[1,1,1,1,1.5,1], tree_effect={"geoevocation": 3}, additional_effect=None)

class Skill:
    def __init__(self, name, description, tier, tree):
        self.name = name
        self.description = description
        self.tier = tier
        self.tree = tree
        self.rank = 1  # Initial rank is 1
        self.cap = 10 # Starting cap for all skills is 10
        self.xp = 0 #starting xp for all skills is 0

    def getNextRankXP(self):
        return (.5*self.rank*(self.rank - 1) + 1) * 2**self.tier * 100

# Create specific skills
intrinsic_clarity = Skill("Intrinsic Clarity", "Multiply mana regen by 1+(RNK/5)", 0, "Magical Utility")
intrinsic_focus = Skill("Intrinsic Focus", "Multiply maximum mana by 1+(RNK/5)", 0, "Magical Utility")
# ... other skills ...

class Awakened:
    def __init__(self, name="Idie Keigh",attributes=[10, 10, 10, 10, 10, 10], vitals=[200, 100, 200, 100, 200, 100], level=0, level_cap=5, experience=0, character_class=unclassed):
        # Health/stamina/mana regenned, 3: damage absorbed, 4: melee kills, 5: ranged kills, 6: magic kills
        self.general_statistics = [0] * 8  # Create a list for general statistics

        self.name = name
        self.attributes = attributes
        self.vitals = vitals
        self.used_skill_points = 0
        self.level = level
        self.level_cap = level_cap
        self.experience = experience
        self.skills = {}
        self.specialization = []
        self.character_class = character_class
        self.currVitals = [200,200,200]
        self.update_free_attributes()
        self.initialize_vitals()  # Initialize vitals when the character is created


    def initialize_vitals(self):
        self.vitals[0] = self.calculate_health_cap()
        self.currVitals[0] = self.calculate_health_cap()
        self.vitals[1] = self.calculate_health_regen()
        self.vitals[2] = self.calculate_stamina_cap()
        self.currVitals[1] = self.calculate_stamina_cap()
        self.vitals[3] = self.calculate_stamina_regen()
        self.vitals[4] = self.calculate_mana_cap()
        self.currVitals[2] = self.calculate_mana_cap()
        self.vitals[5] = self.calculate_mana_regen()

    def update_free_attributes(self):
        self.free_attributes = 70 + (self.level * 10) - sum(self.attributes)

    def max_skill_points(self):
        return self.level + 1
    
    def calculate_used_skill_points(self):
        return len(self.skills)
    
    def calculate_free_skill_points(self):
        return self.max_skill_points() - self.calculate_used_skill_points()

    def calculate_health_cap(self):
        base_health = self.attributes[0] * 20
        health_multiplier = self.character_class.attribute_effect[0]

        return base_health * health_multiplier

    def calculate_health_regen(self):
        base_health_regen = self.attributes[1] * 10
        health_regen_multiplier = self.character_class.attribute_effect[1]

        return base_health_regen * health_regen_multiplier

    def calculate_stamina_cap(self):
        base_stamina = self.attributes[2] * 20
        stamina_multiplier = self.character_class.attribute_effect[2]

        return base_stamina * stamina_multiplier
    
    def calculate_stamina_regen(self):
        base_stamina_regen = self.attributes[3] * 10
        stamina_regen_multiplier = self.character_class.attribute_effect[3]

        return base_stamina_regen * stamina_regen_multiplier

    def calculate_mana_cap(self):
        base_mana_cap = self.attributes[4] * 20
        mana_cap_multiplier = self.character_class.attribute_effect[4]

        for skill in self.skills:
            if skill.name == "Intrinsic Focus":
                # Calculate the multiplicative effect based on the skill's rank
                mana_cap_multiplier *= (1 + skill.rank * 0.2)  # 20% increase per rank

        return base_mana_cap * mana_cap_multiplier

    def calculate_mana_regen(self):
        base_mana_regen = self.attributes[5] * 10
        mana_regen_multiplier = self.character_class.attribute_effect[5]

        for skill in self.skills:
            if skill.name == "Intrinsic Clarity":
                # Calculate the multiplicative effect based on the skill's rank
                mana_regen_multiplier *= (1 + skill.rank * 0.2)  # 20% increase per rank

        return base_mana_regen * mana_regen_multiplier

    def count_skills_in_tree(self, tree_name):
        return sum(1 for skill in self.skills if skill.tree == tree_name)

    def add_skill(self, skill, starting_level=1):
        if skill.name in self.skills:
                print("Skill already aquired!")
                return False
                # What about granted skills, or True Jacks? Think
        
        self.skills.update({skill.name:skill})
        return True
        
    def update_skill_caps (self):
        # Update the skill's cap to the class-based cap
        for skill in list(skill.values()):
            if skill.tree in self.character_class.tree_effect:
                tree_cap = 10 + self.character_class.tree_effect[skill.tree]
                if skill.cap < tree_cap:
                    skill.cap = tree_cap
    
    def add_skill_exp (self, skillN, xp):
        # Find Skill in skills, get xp
        currXP = self.skills[skillN].xp + xp
        nextXP = self.skills[skillN].getNextRankXP()

        if currXP >= nextXP:
            while currXP >= nextXP:
                currXP -= nextXP
                self.skills[skillN].rank +=1
                print(self.skills[skillN].name+" Leveled up!")
                nextXP = self.skills[skillN].getNextRankXP()

        self.skills[skillN].xp = currXP
        # consider making this a method of Skill?

        
    def set_class(self, character_class):
        if self.level != 5 or self.level != 25:
            print(f"Character not at a class selection level!'")
            return False
    
        if character_class.meets_requirements(self):
            self.character_class = character_class
            print(f"Class '{character_class.name}' assigned successfully")

            # Update tree effects based on the assigned class
            for tree, bonus in character_class.tree_effect.items():
                if tree in character_class.tree_effect:
                    self.tree_effect[tree] += bonus
                else:
                    self.tree_effect[tree] = bonus
        else:
            print(f"Character does not meet the requirements for class '{character_class.name}'")

    def calculate_required_experience(self):
        if self.character_class is None or self.level < 5 or self.character_class.rarity in ["Common", "Uncommon"]:
            required_exp = 100 * (self.level ** 2 - self.level) // 2 + 100
        else:
            required_exp = math.floor(2000 * 1.15 ** self.level - 2000)
        return required_exp

    def add_experience(self, amount):
        current_exp = self.experience  # You should have a variable for tracking the character's experience
        required_exp = self.calculate_required_experience()

        new_exp = current_exp + amount

        if self.level == 5 and self.character_class == unclassed or self.level == 25 or self.level == self.level_cap:
                max_exp = required_exp - 1
                new_exp = min(new_exp, max_exp)

        if new_exp >= required_exp:
            while new_exp >= required_exp:
                new_exp -= required_exp
                self.level_up()
                required_exp = self.calculate_required_experience()

        self.experience = new_exp

    def add_statistics(self, location, amount):
        self.general_statistics[location] += amount

    def level_up(self):
        if self.level < self.level_cap:
            self.level += 1
            print(f"Congratulations! You have leveled up to level {self.level}!")
            self.update_free_attributes()

    def display_required_experience(self):
        current_exp = self.experience  # You should have a variable for tracking the character's experience
        required_exp = self.calculate_required_experience()
        difference = required_exp - current_exp

        print(f"Current Experience: {current_exp}")
        print(f"Required Experience for Level {self.level + 1}: {required_exp}")
        print(f"Difference: {difference}")

    def display_stats(self):
        print(f"Stats: {self.attributes}")
        self.initialize_vitals()
        print(f"Current vitals: {self.vitals}")
        print(f"Free Attributes: {self.free_attributes}")
        print(f"Used Skill Points: {self.calculate_used_skill_points()}")
        print(f"Free Skill Points: {self.calculate_free_skill_points()}")
        print(f"Level: {self.level}")
        print(f"Level Cap: {self.level_cap}")
        print(f"Class: {self.character_class.name}")

    # Awful, innefficient, but best that I can think of
    def genSkillList (self):
        tr = []
        for skill in list(self.skills.values()):
            tr.append(skill.tree)
        tr = list(set(tr))

        trees = []

        for tree in tr:
            trr = {"name":tree,"tiers":{"0": {"t":0,"skills":[]},
                                        "1": {"t":1,"skills":[]}, 
                                        "2": {"t":2,"skills":[]}, 
                                        "3": {"t":3,"skills":[]}, 
                                        "4": {"t":4,"skills":[]}}}
            for skill in list(self.skills.values()):                      
                if skill.tree == tree:
                    trr["tiers"][str(skill.tier)]["skills"].append(skill)
                    
            for tier in list(trr["tiers"].values()):
                if not tier["skills"]: trr["tiers"].pop(str(tier["t"]))
            trees.append(trr)

        return trees;

    def printCharSheet (self,altCol = False):
        temp = Template(open('CharSheetTemplate.html').read())
        pluscol = False
        if (self.free_attributes > 0 or self.used_skill_points > 0):
            pluscol = True

        sheet = open(self.name+' CharSheet.html','w')
        sheet.write( temp.render(
                    pluscol = pluscol,
                    altcol = altCol,
                    Name = self.name,
                    Class = self.character_class.name,
                    Level = self.level,
                    LevelCap = self.level_cap,
                    FreeStat = self.free_attributes,
                    FreeSkill = self.calculate_free_skill_points(),
                    CurrXP = self.experience,
                    NextXP = self.calculate_required_experience(),
                    TotXP = "#todo Add Total XP",
                    
                    maxHP = self.vitals[0],
                    rgnHP = self.vitals[1],
                    maxSP = self.vitals[2],
                    rgnSP = self.vitals[3],
                    maxMP = self.vitals[4],
                    rgnMP = self.vitals[5],

                    curHP = self.currVitals[0],
                    curSP = self.currVitals[1],
                    curMP = self.currVitals[2],

                    basSTR = self.attributes[0],
                    basRCV = self.attributes[1],
                    basEND = self.attributes[2],
                    basVGR = self.attributes[3],
                    basFCS = self.attributes[4],
                    basCLR = self.attributes[5],

                    trees = self.genSkillList()
                    
            ))

        sheet.close()
