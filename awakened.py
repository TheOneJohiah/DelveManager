import math
import delve_Class as dc
import skill as sk
from jinja2 import Template;

class Awakened:
    def __init__(self, name="Idie Keigh",attributes=[10, 10, 10, 10, 10, 10,10,10], vitals=[200, 100, 200, 100, 200, 100], level=0, level_cap=5, experience=0, character_class=dc.unclassed):
        # Health/stamina/mana regenned, 3: damage absorbed, 4: melee kills, 5: ranged kills, 6: magic kills
        self.general_statistics = {"total HP regen":0,
                                   "total HP spent":0,
                                   "total SP regen":0,
                                   "total SP spent":0,
                                   "total MP regen":0,
                                   "total MP spent":0,
                                   "melee kills":0,
                                   "ranged kills":0,
                                   "magical kills":0}  # Create a dict for general statistics

        self.name = name
        self.attributes = [[]] * 7 
        self.attributes[0] = [0] * 8 # 0 = effective
        self.attributes[1] = [0] * 8 # 1 = total
        self.attributes[2] = attributes # 2 = base
        self.attributes[3] = [0] * 8 # 3 = accolades
        self.attributes[4] = [0] * 8 # 4 = misc
        self.attributes[5] = [0] * 9 # 5 = tolerance, [8] = general tolerance
        self.attributes[6] = [1] * 8 # 6 = synchronized
        self.vitals = vitals
        self.used_skill_points = 0
        self.level = level
        self.level_cap = level_cap
        self.experience = experience
        self.skills = {}
        self.specialization = []
        self.tree_effect = {}
        self.character_class = character_class
        self.banked_xp = 0
        self.currVitals = [200,200,200]
        #Needed to prevent recursion
        self.synergy_vitals = [0,0,0,0,0,0]
        self.inventory = {"Head" : None, "Chest" : None, "Legs" : None, "Hands" : None, "Feet" : None, "Ring[0]" : None, "Ring[1]" : None, "Ring[2]" : None, "Ring[3]" : None, "Ring[4]" : None, "Ring[5]" : None, "Ring[6]" : None, "Ring[7]" : None, "Ring[8]" : None, "Ring[9]" : None, "Amulet" : None, "Mainhand" : None, "Underwear" : None, "Overwear" : None, "Offhand" : ""}
        self.update_free_attributes()
        self.update_attributes()  # Initialize attributes when the character is created
        self.resistances = [[]] * 8
        self.resistances[0] = [0] * 8 #total flat
        self.resistances[1] = [0] * 8 #total percent
        self.resistances[2] = [0] * 8 #base flat
        self.resistances[3] = [0] * 8 #base percent
        self.resistances[4] = [0] * 8 #accolade flat
        self.resistances[5] = [0] * 8 #accolade percent
        self.resistances[6] = [0] * 8 #misc flat
        self.resistances[7] = [0] * 8 #misc percent
        self.calculate_resistances()
        self.initialize_vitals()  # Initialize vitals when the character is created

    def update_attributes(self):
        for x in range(8):
            self.attributes[1][x] = self.attributes[2][x] + self.attributes[3][x] + self.attributes[4][x]
            self.attributes[0][x] = min(self.attributes[6][x], self.attributes[2][x]+self.attributes[3][x]) + min(1, self.attributes[6][x]/(self.attributes[2][x]+self.attributes[3][x]))*min(self.attributes[4][x],self.attributes[5][x])
        self.update_vitals()

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

        #Call a second time now that they've set the synergy_values. Ew. I guess technically only needed for characters that start with magical synergy.
        self.vitals[4] = self.calculate_mana_cap()
        self.currVitals[2] = self.calculate_mana_cap()
        self.vitals[5] = self.calculate_mana_regen()

    def update_vitals(self):
        self.vitals[0] = self.calculate_health_cap()
        self.vitals[1] = self.calculate_health_regen()
        self.vitals[2] = self.calculate_stamina_cap()
        self.vitals[3] = self.calculate_stamina_regen()
        self.vitals[4] = self.calculate_mana_cap()
        self.vitals[5] = self.calculate_mana_regen()

    def raise_attribute(self,index,amount):
        if (amount > self.free_attributes):
            amount = self.free_attributes
            print ("Tried to spend too many stat points! Reduced to "+str(amount))

        self.attributes[2][index] += amount
        self.update_attributes()
        self.update_vitals()
        self.update_free_attributes()
    
    def update_free_attributes(self): self.free_attributes = 90 + (self.level * 10) - sum(self.attributes[2])

    def max_skill_points(self): return self.level + 1
    
    def calculate_used_skill_points(self): return len(self.skills)
    
    def calculate_free_skill_points(self): return self.max_skill_points() - self.calculate_used_skill_points()

    def calculate_health_cap(self):
        base_health = self.attributes[1][0] * 20
        health_multiplier = self.character_class.attribute_effect[0]

        return base_health * health_multiplier

    def calculate_health_regen(self):
        base_health_regen = self.attributes[1][1] * 10
        health_regen_multiplier = self.character_class.attribute_effect[1]

        return base_health_regen * health_regen_multiplier

    def calculate_stamina_cap(self):
        base_stamina = self.attributes[1][2] * 20
        stamina_multiplier = self.character_class.attribute_effect[2]

        return base_stamina * stamina_multiplier
    
    def calculate_stamina_regen(self):
        base_stamina_regen = self.attributes[1][3] * 10
        stamina_regen_multiplier = self.character_class.attribute_effect[3]

        return base_stamina_regen * stamina_regen_multiplier

    def calculate_mana_cap(self):
        synergy_mana = 0
        base_mana_cap = self.attributes[1][4] * 20
        mana_cap_multiplier = self.character_class.attribute_effect[4]

        # Calculate the multiplicative effect based on the skill's rank
        mana_cap_multiplier *= (1 + self.get_skill_rank("Intrinsic Focus") * 0.2)  # 20% increase per rank
        synergy_effect = 0.025 * self.get_skill_rank("Magical Synergy")
        synergy_mana = synergy_effect * self.synergy_vitals[5]
        self.synergy_vitals[4] = (base_mana_cap * mana_cap_multiplier)

        return (base_mana_cap * mana_cap_multiplier) + synergy_mana

    def calculate_mana_regen(self):
        synergy_mana = 0
        base_mana_regen = self.attributes[1][5] * 10
        mana_regen_multiplier = self.character_class.attribute_effect[5]

        mana_regen_multiplier *= (1 + self.get_skill_rank("Intrinsic Clarity") * 0.2)  # 20% increase per rank
        synergy_effect = 0.025 * self.get_skill_rank("Magical Synergy")
        synergy_mana = synergy_effect * self.synergy_vitals[4]
        self.synergy_vitals[5] = (base_mana_regen * mana_regen_multiplier)

        return (base_mana_regen * mana_regen_multiplier) + synergy_mana
    
    def calculate_resistances(self):
        end_multiplier = self.character_class.attribute_effect[2]
        intMult = 1 + .2*self.get_skill_rank("Intrinsic Resistance")
        synMult = .025*self.get_skill_rank("Resistance Synergy")
        baseRes = (self.attributes[1][2] * end_multiplier * intMult / 10)
        # Remember to include item and other skill effects later
        tots = [0] * 8
        for x in range (8): tots[x] = sum(self.resistances[x])
        self.resistances[2] = [baseRes] * 8
        for x in range(8):
            self.resistances[0][x] = self.resistances[2][x] + self.resistances[4][x] + self.resistances[6][x] + synMult*(tots[2]-self.resistances[2][x] + tots[4]-self.resistances[4][x] + tots[6]-self.resistances[6][x])
            self.resistances[1][x] = self.resistances[3][x] + self.resistances[5][x] + self.resistances[7][x] + synMult*(tots[3]-self.resistances[3][x] + tots[5]-self.resistances[5][x] + tots[7]-self.resistances[7][x])

    def add_equipment (self,item): self.inventory[item.slot] = item
    
    def essence_exhange(self):
        #All banked xp from stat expenditure or anything else
        self.add_experience(self.banked_xp)
        self.banked_xp = 0
        for skill in list(self.skills.values()):
            if skill.banked_xp > 0:
                self.add_skill_exp(skill.name)

    def bank_experience(self, xp): self.banked_xp += xp

    def reduce_vital(self, type, amount):
        self.add_statistics("total "+type+" spent",amount) 

        if type == "HP": type = 0
        elif type == "SP": type = 1
        elif type == "MP": type = 2
        else: print(type+" is not a vital, goof") 
        
        self.currVitals[type] -= amount
        self.bank_experience(.5*amount)

        if type == 2:
            for skill in list(self.skills.values()):
                if skill.name == "Intrinsic Clarity":
                    self.bank_skill_exp(skill.name, .5*amount)
                elif skill.name == "Intrinsic Focus":
                    self.bank_skill_exp(skill.name, .5*amount)
                elif skill.name == "Magical Synergy":
                    self.bank_skill_exp(skill.name, .5*amount)
                    
    def add_vital(self, type, amount):
        if type == "HP": type = 0
        elif type == "SP": type = 1
        elif type == "MP": type = 2
        else: print(type+" is not a vital, goof") 
        
        self.currVitals[type] += amount

    def regen (self, hours):
        time = hours/24
        for x in range(3):
            regN = min( time*self.vitals[2*x + 1], self.vitals[2*x] - self.currVitals[x]) # ensuring regen doesn't overflow cap
            overN = time*self.vitals[2*x + 1] - regN #Over-whatever; currently unused, could add an total-overvital statistic?
            self.currVitals[x] += regN
            self.add_statistics("total "+["HP","SP","MP"][x]+" regen",regN)


    def count_skills_in_tree(self, tree_name):
        return sum(1 for skill in self.skills if skill.tree == tree_name)

    def get_skill_rank(self, skillN):
        if skillN in self.skills: return self.skills[skillN].rank
        else: return 0
    
    def add_skill(self, skill, starting_level=1):
        if skill.name in self.skills:
                print("Skill already aquired!")
                return False
                # What about granted skills, or True Jacks? Think
        
        self.skills.update({skill.name:skill})
        self.update_vitals()
        self.used_skill_points = self.calculate_used_skill_points()
        if skill.tree in self.character_class.tree_effect: skill.cap = 10 + self.character_class.tree_effect[skill.tree]
        return True
        
    def update_skill_caps (self):
        # Update the skill's cap to the class-based cap
        for skill in list(self.skills.values()):
            if skill.tree in self.character_class.tree_effect:
                skill.cap = 10 + self.character_class.tree_effect[skill.tree]
    
    def bank_skill_exp (self, skillN, xp): self.skills[skillN].bank_exp(xp) #redirect to skill method
    def add_skill_exp (self, skillN): self.skills[skillN].add_exp() #redirect to skill method

    def cast_skill (self, skillN, n):
        skill = self.skills[skillN]
        self.reduce_vital(skill.cost['type'],skill.cost['value']*n)
        skill.bank_exp(.5*n*skill.cost['value'])
    
    def set_class(self, character_class):
        if not self.level in [5,25,50,75]:
            print(f"{self.name} not at a class selection level!")   
            return False 
    
        if character_class.meets_requirements(self):
            self.character_class = character_class
            print(f"Class '{character_class.name}' assigned successfully")

            # Update tree effects based on the assigned class
            for tree, bonus in character_class.tree_effect.items(): self.tree_effect[tree] = bonus
            self.update_skill_caps()
        else:
            print(f"{self.name} does not meet the requirements for class '{character_class.name}'")

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

        if new_exp >= required_exp:
            while new_exp >= required_exp:
                ##Moved inside the while loop so it rechecks each level when getting lots of xp at once.
                if self.level == 5 and self.character_class == dc.unclassed or self.level == 25 or self.level == self.level_cap:
                    max_exp = required_exp - 1
                    new_exp = min(new_exp, max_exp)
                    return True
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

    # Awful, innefficient, but best that I can think of
    def genSkillList (self):
        tr = []
        for skill in list(self.skills.values()):
            tr.append(skill.tree)
        tr = sorted(list(set(tr)))

        trees = []

        for tree in tr:
            trr = {"name":tree,"tiers":{"0": {"t":0,"skills":[]},
                                        "1": {"t":1,"skills":[]}, 
                                        "2": {"t":2,"skills":[]}, 
                                        "3": {"t":3,"skills":[]}, 
                                        "4": {"t":4,"skills":[]}}}
            for skill in list(self.skills.values()):                      
                if skill.tree == tree: trr["tiers"][str(skill.tier)]["skills"].append(skill)
                    
            for tier in list(trr["tiers"].values()):
                if not tier["skills"]: trr["tiers"].pop(str(tier["t"]))
            trees.append(trr)

        return trees;

    def printCharSheet (self,altCol = False):
        temp = Template(open('CharSheetTemplate.html').read())
        pluscol = self.free_attributes > 0 or self.calculate_free_skill_points() > 0

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

                    effSTR = self.attributes[0][0],
                    effRCV = self.attributes[0][1],
                    effEND = self.attributes[0][2],
                    effVGR = self.attributes[0][3],
                    effFCS = self.attributes[0][4],
                    effCLR = self.attributes[0][5],
                    effPER = self.attributes[0][6],
                    effSPD = self.attributes[0][7],

                    totSTR = self.attributes[1][0],
                    totRCV = self.attributes[1][1],
                    totEND = self.attributes[1][2],
                    totVGR = self.attributes[1][3],
                    totFCS = self.attributes[1][4],
                    totCLR = self.attributes[1][5],
                    totPER = self.attributes[1][6],
                    totSPD = self.attributes[1][7],

                    basSTR = self.attributes[2][0],
                    basRCV = self.attributes[2][1],
                    basEND = self.attributes[2][2],
                    basVGR = self.attributes[2][3],
                    basFCS = self.attributes[2][4],
                    basCLR = self.attributes[2][5],
                    basPER = self.attributes[2][6],
                    basSPD = self.attributes[2][7],

                    accSTR = self.attributes[3][0],
                    accRCV = self.attributes[3][1],
                    accEND = self.attributes[3][2],
                    accVGR = self.attributes[3][3],
                    accFCS = self.attributes[3][4],
                    accCLR = self.attributes[3][5],
                    accPER = self.attributes[3][6],
                    accSPD = self.attributes[3][7],
                    
                    mscSTR = self.attributes[4][0],
                    mscRCV = self.attributes[4][1],
                    mscEND = self.attributes[4][2],
                    mscVGR = self.attributes[4][3],
                    mscFCS = self.attributes[4][4],
                    mscCLR = self.attributes[4][5],
                    mscPER = self.attributes[4][6],
                    mscSPD = self.attributes[4][7],
                    
                    tolSTR = self.attributes[5][0],
                    tolRCV = self.attributes[5][1],
                    tolEND = self.attributes[5][2],
                    tolVGR = self.attributes[5][3],
                    tolFCS = self.attributes[5][4],
                    tolCLR = self.attributes[5][5],
                    tolPER = self.attributes[5][6],
                    tolSPD = self.attributes[5][7],
                    
                    synSTR = self.attributes[6][0],
                    synRCV = self.attributes[6][1],
                    synEND = self.attributes[6][2],
                    synVGR = self.attributes[6][3],
                    synFCS = self.attributes[6][4],
                    synCLR = self.attributes[6][5],
                    synPER = self.attributes[6][6],
                    synSPD = self.attributes[6][7],

                    fltHE = self.resistances[0][0],
                    fltCO = self.resistances[0][1],
                    fltLI = self.resistances[0][2],
                    fltDA = self.resistances[0][3],
                    fltFO = self.resistances[0][4],
                    fltAR = self.resistances[0][5],
                    fltCH = self.resistances[0][6],
                    fltME = self.resistances[0][7],
                    perHE = self.resistances[1][0],
                    perCO = self.resistances[1][1],
                    perLI = self.resistances[1][2],
                    perDA = self.resistances[1][3],
                    perFO = self.resistances[1][4],
                    perAR = self.resistances[1][5],
                    perCH = self.resistances[1][6],
                    perME = self.resistances[1][7],
                    ENDfltHE = self.resistances[2][0],
                    ENDfltCO = self.resistances[2][1],
                    ENDfltLI = self.resistances[2][2],
                    ENDfltDA = self.resistances[2][3],
                    ENDfltFO = self.resistances[2][4],
                    ENDfltAR = self.resistances[2][5],
                    ENDfltCH = self.resistances[2][6],
                    ENDfltME = self.resistances[2][7],
                    ENDperHE = self.resistances[3][0],
                    ENDperCO = self.resistances[3][1],
                    ENDperLI = self.resistances[3][2],
                    ENDperDA = self.resistances[3][3],
                    ENDperFO = self.resistances[3][4],
                    ENDperAR = self.resistances[3][5],
                    ENDperCH = self.resistances[3][6],
                    ENDperME = self.resistances[3][7],
                    ACCfltHE = self.resistances[4][0],
                    ACCfltCO = self.resistances[4][1],
                    ACCfltLI = self.resistances[4][2],
                    ACCfltDA = self.resistances[4][3],
                    ACCfltFO = self.resistances[4][4],
                    ACCfltAR = self.resistances[4][5],
                    ACCfltCH = self.resistances[4][6],
                    ACCfltME = self.resistances[4][7],
                    ACCperHE = self.resistances[5][0],
                    ACCperCO = self.resistances[5][1],
                    ACCperLI = self.resistances[5][2],
                    ACCperDA = self.resistances[5][3],
                    ACCperFO = self.resistances[5][4],
                    ACCperAR = self.resistances[5][5],
                    ACCperCH = self.resistances[5][6],
                    ACCperME = self.resistances[5][7],
                    MSCfltHE = self.resistances[6][0],
                    MSCfltCO = self.resistances[6][1],
                    MSCfltLI = self.resistances[6][2],
                    MSCfltDA = self.resistances[6][3],
                    MSCfltFO = self.resistances[6][4],
                    MSCfltAR = self.resistances[6][5],
                    MSCfltCH = self.resistances[6][6],
                    MSCfltME = self.resistances[6][7],
                    MSCperHE = self.resistances[7][0],
                    MSCperCO = self.resistances[7][1],
                    MSCperLI = self.resistances[7][2],
                    MSCperDA = self.resistances[7][3],
                    MSCperFO = self.resistances[7][4],
                    MSCperAR = self.resistances[7][5],
                    MSCperCH = self.resistances[7][6],
                    MSCperME = self.resistances[7][7],

                    trees = self.genSkillList(),

                    Items = filter(None,list(self.inventory.values()))
                    
            ))

        sheet.close()