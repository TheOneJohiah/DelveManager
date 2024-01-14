import math
from delve_Class import *
from skill import *
from accolade import *
from item import *
from copy import *
from timeline import *
from jinja2 import Template;

class Awakened:
    def __init__(self, name="Idie Keigh",attributes=[10, 10, 10, 10, 10, 10,10,10], level=0, level_cap=5, experience=0, character_class=unclassed,date=Moment('0936-06-03-12:00:00:000')):
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
        self.attributes[2] = copy(attributes) # 2 = base
        self.attributes[3] = [0] * 8 # 3 = accolades
        self.attributes[4] = [0] * 8 # 4 = misc
        self.attributes[5] = [0] * 9 # 5 = tolerance, [8] = general tolerance
        self.attributes[6] = [1] * 8 # 6 = synchronized
        self.accolades = {}
        self.percentAccolades = [[]] * 2
        self.percentAccolades[0] = [0]*8 # % for attributes
        self.percentAccolades[1] = [0]*8 # % for resists
        self.vitals = [200, 100, 200, 100, 200, 100]
        self.used_skill_points = 0
        self.level = level
        self.level_cap = level_cap if level_cap >= level else level
        self.experience = experience
        self.skills = {}
        self.trees = {}
        self.initialize_trees()
        self.specialization = []
        self.character_class = character_class
        self.banked_xp = 0
        self.total_xp = experience
        self.currVitals = [200,200,200]
        #Needed to prevent recursion
        self.synergy_vitals = [0,0,0,0,0,0]
        self.inventory = {"Head" : None, "Chest" : None, "Legs" : None, "Hands" : None, "Feet" : None, "Ring[0]" : None, "Ring[1]" : None, "Ring[2]" : None, "Ring[3]" : None, "Ring[4]" : None, "Ring[5]" : None, "Ring[6]" : None, "Ring[7]" : None, "Ring[8]" : None, "Ring[9]" : None, "Amulet" : None, "Mainhand" : None, "Underwear" : None, "Overwear" : None, "Offhand" : ""}
        self.resistances = [[]] * 8
        self.resistances[0] = [0] * 8 #total flat
        self.resistances[1] = [0] * 8 #total percent
        self.resistances[2] = [0] * 8 #base flat
        self.resistances[3] = [0] * 8 #base percent
        self.resistances[4] = [0] * 8 #accolade flat
        self.resistances[5] = [0] * 8 #accolade percent
        self.resistances[6] = [0] * 8 #misc flat
        self.resistances[7] = [0] * 8 #misc percent
        self.mods = {}
        self.update_free_attributes()
        self.update_attributes()  # Initialize attributes when the character is created
        self.calculate_resistances()
        self.initialize_vitals()  # Initialize vitals when the character is created
        self.date = date

    def update_attributes(self):
        for x in range(8):
            self.attributes[1][x] = self.attributes[2][x] + self.attributes[3][x] + self.attributes[4][x]
            self.attributes[0][x] = min(self.attributes[6][x], self.attributes[2][x]+self.attributes[3][x]) + min(1, self.attributes[6][x]/(self.attributes[2][x]+self.attributes[3][x]))*min(self.attributes[4][x],self.attributes[5][x])
        self.update_vitals()
        self.calculate_resistances()

    def update_buffs(self):
        #Reset & Repopulate non-base boosts
        self.attributes[3] = [0] * 8
        self.attributes[4] = [0] * 8
        self.resistances[4] = [0] * 8
        self.resistances[5] = [0] * 8
        self.resistances[6] = [0] * 8
        self.resistances[7] = [0] * 8
        self.percentAccolades[0] = [0] * 8  # Reset percentAccolades[0]

        #Update array column [4] with item attribute buffs
        for item in filter(None, list(self.inventory.values())):
            for rune in item.runes:
                for enchant in rune.enchantments: #Add buffs to arrays
                    if hasattr(enchant,'attribute_buff'): self.attributes[4] = [sum(i) for i in zip(self.attributes[4],enchant.attribute_buff)]
                    if hasattr(enchant,'resistance_buff'): self.resistances[6] = [sum(i) for i in zip(self.resistances[6],enchant.resistance_buff)]
        #Do something for spell buffs?
        # Iterate through self.accolades and add their bonuses to self.attributes[3]
        for accolade in self.accolades.values():
            if isinstance(accolade, Stats):  # Check if the accolade is a Stats accolade
                num_active = accolade.numActive  # Get the number of active instances of this accolade
                accolade_stats = [stat * num_active for stat in accolade.stats]  # Multiply accolade stats by numActive
                self.attributes[3] = [a + b for a, b in zip(self.attributes[3], accolade_stats)]
        # Now do the same for PercentStat accolades
        for accolade in self.accolades.values():
            if isinstance(accolade, PercentStats):  # Check if the accolade is a PercentStats accolade
                num_active = accolade.numActive  # Get the number of active instances of this accolade
                accolade_stats = [percentStat * num_active for percentStat in accolade.percentStats]  # Multiply accolade stats by numActive
                self.percentAccolades[0] = [a + b for a, b in zip(self.percentAccolades[0], accolade_stats)]

        self.update_attributes()
    
    def initialize_trees(self):
        for tree in AllTreeList: self.trees.update({tree:Tree(tree)})
    
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

    def max_level_points(self): return self.level + 1
    
    def calculate_used_skill_points(self): return len(self.skills)
    
    def calculate_free_skill_points(self): return self.max_level_points() - self.calculate_used_skill_points()

    def calculate_used_accolade_slots(self):
        used_slots = 0
        
        for accolade in self.accolades.values():
            used_slots += accolade.rank * accolade.numActive

        return used_slots

    def calculate_free_accolade_slots(self): return self.max_level_points() - self.calculate_used_accolade_slots()

    def calculate_health_cap(self):
        base_health = self.attributes[1][0] * 20
        health_multiplier = 100 + self.character_class.attribute_effect[0] + self.percentAccolades[0][0]
        health_multiplier *= 100 + 20*self.get_skill_rank("Intrinsic Strength")
        return base_health * health_multiplier / 10000

    def calculate_health_regen(self):
        base_health_regen = self.attributes[1][1] * 10
        health_regen_multiplier = 100 + self.character_class.attribute_effect[1] + self.percentAccolades[0][1]
        health_regen_multiplier *= 100 + 20*self.get_skill_rank("Intrinsic Recovery")
        return base_health_regen * health_regen_multiplier / 10000

    def calculate_stamina_cap(self):
        base_stamina = self.attributes[1][2] * 20
        stamina_multiplier = 100 + self.character_class.attribute_effect[2] + self.percentAccolades[0][2]
        stamina_multiplier *= 100 + 20*self.get_skill_rank("Intrinsic Endurance")
        return base_stamina * stamina_multiplier / 10000
    
    def calculate_stamina_regen(self):
        base_stamina_regen = self.attributes[1][3] * 10
        stamina_regen_multiplier = 100 + self.character_class.attribute_effect[3] + self.percentAccolades[0][3]
        stamina_regen_multiplier *= 100 + 20*self.get_skill_rank("Intrinsic Vigor")
        return base_stamina_regen * stamina_regen_multiplier / 10000

    def calculate_mana_cap(self):
        synergy_mana = 0
        base_mana_cap = self.attributes[1][4] * 20
        mana_cap_multiplier = 100 + self.character_class.attribute_effect[4] + self.percentAccolades[0][4]

        # Calculate the multiplicative effect based on the skill's rank
        mana_cap_multiplier *= 100 + 20*self.get_skill_rank("Intrinsic Focus")  # 20% increase per rank
        synergy_effect = 2.5*self.get_skill_rank("Magical Synergy")
        synergy_mana = synergy_effect * self.synergy_vitals[5]
        self.synergy_vitals[4] = (base_mana_cap * mana_cap_multiplier)/100

        return (base_mana_cap*mana_cap_multiplier + synergy_mana)/10000

    def calculate_mana_regen(self):
        synergy_mana = 0
        base_mana_regen = self.attributes[1][5] * 10
        mana_regen_multiplier = 100 + self.character_class.attribute_effect[5] + self.percentAccolades[0][5]

        mana_regen_multiplier *= 100 + 20*self.get_skill_rank("Intrinsic Clarity")  # 20% increase per rank
        synergy_effect = self.get_skill_power("Magical Synergy")
        synergy_mana = synergy_effect * self.synergy_vitals[4]
        self.synergy_vitals[5] = (base_mana_regen * mana_regen_multiplier)/100

        return (base_mana_regen*mana_regen_multiplier + synergy_mana)/10000
    
    def calculate_resistances(self):
        end_multiplier = 100 + self.character_class.attribute_effect[2]
        intMult = 100 + 20*self.get_skill_rank("Intrinsic Resistance")
        synMult = .025*self.get_skill_rank("Resistance Synergy")
        baseRes = (self.attributes[1][2] * end_multiplier * intMult / 100000)
        # Remember to include item and other skill effects later
        tots = [0] * 8
        for x in range (8): tots[x] = sum(self.resistances[x])
        self.resistances[2] = [baseRes] * 8
        for x in range(8):
            self.resistances[0][x] = self.resistances[2][x] + self.resistances[4][x] + self.resistances[6][x] + synMult*(tots[2]-self.resistances[2][x] + tots[4]-self.resistances[4][x] + tots[6]-self.resistances[6][x])
            self.resistances[1][x] = self.resistances[3][x] + self.resistances[5][x] + self.resistances[7][x] + synMult*(tots[3]-self.resistances[3][x] + tots[5]-self.resistances[5][x] + tots[7]-self.resistances[7][x])

    def add_equipment (self,item):
        self.inventory[item.slot] = item
        #if rune in item.runes ==  
        self.update_buffs()

    def toggle_equipment (self,item):
        if item in self.inventory:
            self.inventory[item].toggle_rune
            self.update_buffs()
        else: return 0

    def essence_exhange(self):
        currentLvl = self.level
        #All banked xp from stat expenditure or anything else
        self.add_experience(self.banked_xp)
        self.banked_xp = 0
        for skill in list(self.skills.values()):
            if skill.banked_xp > 0:
                self.add_skill_exp(skill.name)
        if currentLvl == self.level:
            print(f"No level up last night. {self.name} is currently level {self.level}")
        else:
            print(f"A new dawn, a new day! {self.name} is now level {self.level}")

    def bank_experience(self, xp): self.banked_xp += xp

    def reduce_vital(self, vital, amount):
        self.add_statistics("total "+vital+" spent",amount) 
        underV = 0
        if vital == "HP": vital = 0
        elif vital == "SP": vital = 1
        elif vital == "MP": vital = 2
        #else: print(type+" is not a vital, goof")

        self.bank_experience(.5*amount)
        if amount > self.currVitals[vital]:
            underV = self.currVitals[vital] - amount #Undervital
            self.currVitals[vital] = 0
            print(str(underV) + ["HP","SP","MP"][vital])
        else:
            self.currVitals[vital] -= amount
        
        if vital == 0:
            for passive in ["Intrinsic Resistance","Turtle Skin","Intrinsic Strength","Intrinsic Recovery"]:
                if passive in self.skills: self.bank_skill_exp(passive, .5*amount)
        if vital == 1:
            for passive in ["Strength of Arm","Intrinsic Endurance","Intrinsic Vigor"]:
                if passive in self.skills: self.bank_skill_exp(passive, .5*amount)
        if vital == 2:
            for passive in ["Intrinsic Clarity","Intrinsic Focus","Magical Synergy"]:
                if passive in self.skills: self.bank_skill_exp(passive, .5*amount)

        return underV
                    
    def add_vital(self, type, amount):
        if type == "HP": type = 0
        elif type == "SP": type = 1
        elif type == "MP": type = 2
        #else: print(type+" is not a vital, goof") 
        
        addN = min(amount, self.vitals[2*type] - self.currVitals[type]) # ensuring regen doesn't overflow cap
        overN = amount - addN #Over-whatever; currently unused, could add an total-overvital statistic?
        self.currVitals[type] += addN

        return addN

    def regen (self, hours, mods=[0,0,0]):
        self.date = self.date.plus(Duration(int(hours*3600000)))
        time = hours/24
        for x in range(3):
            regN = self.add_vital(x,time*self.vitals[2*x + 1]*(1 + .01*mods[x]))
            self.add_statistics("total "+["HP","SP","MP"][x]+" regen",regN)

    def train(self, hours, skills,mods=[0,0,0],spending=[0,0,0]):
        # Break down into health, stamina, and mana skills
        hp_skills = list(filter(lambda s: "HP"==self.skills[s].cost['type'],skills))
        sp_skills = list(filter(lambda s: "SP"==self.skills[s].cost['type'],skills))
        mp_skills = list(filter(lambda s: "MP"==self.skills[s].cost['type'],skills))
        time = hours/24
        for x in range(3):
            vp_skills = [hp_skills,sp_skills,mp_skills][x]
            vp_skills.sort(key=(lambda c: self.skills[c].cost['value']),reverse=True)
            print("V",x,len(vp_skills))
            t = ["HP","SP","MP"][x]
            # Regen
            regN = time*self.vitals[2*x + 1]*(1 + .01*mods[x])
            if (len(vp_skills)>0): self.currVitals[x] += regN
            else: self.add_vital(t,regN)
            self.add_statistics("total "+t+" regen",regN)
            
            #base spending
            self.reduce_vital(t,spending[x])
            
            #dealing with skills
            for sk in vp_skills:
                times = min(hours*3600/self.get_skill_duration(sk),math.floor(self.currVitals[x]/(len(vp_skills)*self.get_skill_cost(sk,1)['value'])))
                print(sk,":",times,self.get_skill_cost(sk,1)['value']*times,self.get_skill_cost(sk,1)['type'])
                self.cast_skill(sk,times)

        self.date = self.date.plus(Duration(int(hours*3600000)))
    
    def train_days(self,days,skills,mods=[0,0,0],dayspending=[0,0,0],sleepmod=[0,0,0],nextskills=[],stats=[0,0,0,0,0,0],cb=None,clear_skills=True):
        for day in range(days):
            print(f"Day {int(Moment('0936-06-03-12:00:00:000').to(self.date).length.in_days()+.5)}")
            self.regen(8,sleepmod)
            self.essence_exhange()
            if self.calculate_free_skill_points()>0 and not len(nextskills)==0: #add new skills
                self.add_skill(nextskills[0])
                if hasattr(nextskills[0],'cost'): skills.append(nextskills[0].name)
                nextskills.pop(0)
            if self.free_attributes>0: #add stats
                div = len(list(filter(lambda x: x>0,stats)))
                inc = 0 if div==0 else int(self.free_attributes/div)
                for st in range(6):
                    self.raise_attribute(st,min(stats[st],inc))
                stats = list(map(lambda x: max(0,x - inc),stats))
            if callable(cb): cb()
            if clear_skills: skills = list(filter(lambda s: not self.skills[s].cap==self.skills[s].rank,skills)) #remove maxxed skills 
            self.train(16,skills,mods,dayspending)
    
    def update_level_cap(self, newLevel): self.level_cap = newLevel

    def count_skills_in_tree(self, tree_name):
        total = 0
        for tier in self.trees[tree_name].tiers:
            total += len(tier.skills)
        return total
    
    def count_ranks_in_tree(self,tree_name):
        total = 0
        for tier in self.trees[tree_name].tiers:
            for skill in tier.skills:
                total += skill.rank
        return total

    def add_mods(self,source,mod): self.mods[source] = mod
    
    def get_mods(self,targets,extra=[]):
        modifier = Modifier(targets,1,0,1,0,1,0,1,0)
        mods = list(filter(lambda m: m.target in targets,list(self.mods.values())))
        "Channel Mastery:2".split(":")[0]
        mods.extend(map(lambda s: self.skills[s.split(":")[0]].get_mod(),extra))
        #mods.extend(map(lambda s: self.skills[s.split(":")[0]].get_mod(s.split(":")[1]),extra))
        for mod in mods:
            modifier.power_buff    *= 1 + .01*mod.power_buff    
            modifier.power_flat    += mod.power_flat    
            modifier.range_buff    *= 1 + .01*mod.range_buff    
            modifier.range_flat    += mod.range_flat    
            modifier.duration_buff *= 1 + .01*mod.duration_buff 
            modifier.duration_flat += mod.duration_flat 
            modifier.cost_buff     *= 1 + .01*mod.cost_buff     
            modifier.cost_flat     += mod.cost_flat    
        return modifier
    
    def get_skill_duration(self,skillN):
        if hasattr(self.skills[skillN],'get_duration'): return self.skills[skillN].get_duration()
        else: return 1

    def get_skill_cost(self,skillN,n): return self.skills[skillN].get_cost(n)
    
    def get_skill_rank(self, skillN):
        if skillN in self.skills: return self.skills[skillN].rank
        else: return 0
    
    def get_skill_power(self, skillN):
        if skillN in self.skills: return self.skills[skillN].get_power()
        else: return 0

    def get_skill_xp(self, skillN):
        if skillN in self.skills: return self.skills[skillN].xp
        else: return 0

    def add_skill(self, skill, starting_level=1):
        if self.trees[skill.tree].tiers[skill.tier].lock: print(f"{skill.tree} Tier {skill.tier} not unlocked!"); return False
        if skill.name in self.skills: print("Skill already aquired!"); return False
                
        self.skills.update({skill.name:skill})
        self.trees[skill.tree].tiers[skill.tier].skills.append(skill.name)
        self.update_vitals()
        self.used_skill_points = self.calculate_used_skill_points()
        skill.awakened = self
        skill.rank = starting_level
        skill.cap = 10 + self.trees[skill.tree].bonus
        skill.on_level_up()
        return True
        
    def update_skill_caps (self):
        # Update the skill's cap to the class-based cap
        for skill in list(self.skills.values()):
            if skill.tree in self.character_class.tree_effect:
                skill.cap = 10 + self.character_class.tree_effect[skill.tree]
    
    def bank_skill_exp (self, skillN, xp): self.skills[skillN].bank_exp(xp) #redirect to skill method
    
    def add_skill_exp (self, skillN): self.skills[skillN].add_exp() #redirect to skill method

    def cast_skill (self, skillN, n, mods=[]):
        self.skills[skillN].modifier = self.get_mods(self.skills[skillN].keywords,mods)
        cost = self.get_skill_cost(skillN,n)
        underV = self.reduce_vital(cost['type'],cost['value'])
        self.bank_skill_exp(skillN,.5*(cost['value'] - underV))
    
    def unlock_tier(self,tree,tier):
        if not self.trees[tree].tiers[tier].lock: print(f"{tree} already unlocked!"); return False
        if self.trees[tree].tiers[tier-1].lock: print(f"Unlock {tree} tier {tier-1} first!"); return False
        cost = 10**(tier+1)
        if self.experience < cost: print(f"Not enough experience for {tree}!"); return False

        self.experience -= cost
        self.trees[tree].unlock(tier)

    def add_accolade(self, accolade, count):
        free_slots = self.calculate_free_accolade_slots()

        # Check if the accolade already exists in self.accolades
        if accolade.name in self.accolades:
            self.accolades[accolade.name].numStored += count  # Increase numStored by one
        else:
            accolade.numStored = count  # Initialize numStored to 1 if it doesn't exist
            self.accolades[accolade.name] = accolade  # Add the accolade to self.accolades

        if free_slots > accolade.rank:
            # Equip automatically, free slots available
            self.activate_accolade(accolade, count, free_slots)

        self.update_buffs()
        return True
    
    def activate_accolade(self, accolade, count, free_slots):
        if accolade.name in self.accolades and self.accolades[accolade.name].numActive < self.accolades[accolade.name].numStored and free_slots >= accolade.rank:
            count = min(count, free_slots // accolade.rank)
            new_active = min(count, self.accolades[accolade.name].numStored - self.accolades[accolade.name].numActive) #Make sure not to activate more than stored
            self.accolades[accolade.name].numActive += new_active  # Increase numActive for the specified accolade
            return True
        else:
            return False  # Return False if the accolade doesn't exist in self.accolades or all are active already or free slots are insufficient
    
    def remove_accolade(self, toRemove, outCount, toAdd=None, inCount=0):
        if toRemove.name in self.accolades and self.accolades[toRemove.name].numActive > 0:
            if outCount >= self.accolades[toRemove.name].numStored:
                # Remove the accolade entirely if outCount is greater than or equal to numStored
                del self.accolades[toRemove.name]
            else:
                # Reduce numActive to numStored if outCount is less than numStored
                self.accolades[toRemove.name].numStored = self.accolades[toRemove.name].numStored - outCount
                if self.accolades[toRemove.name].numStored < self.accolades[toRemove.name].numActive:
                    self.accolades[toRemove.name].numActive = self.accolades[toRemove.name].numStored

            # Autoslot a new accolade if toAdd is not empty and there are any unbound accolades
            if toAdd and inCount > 0:
                free_slots = self.calculate_free_accolade_slots()
                if free_slots >= toAdd.rank:
                    self.activate_accolade(toAdd, inCount, free_slots)
                elif free_slots > 0:
                    return True
                    #TODO: Implement random slotting if free slots remain after
            return True
        self.update_buffs()
        return False  # Return False if toRemove is not in self.accolades or numActive is not greater than 0

    def swap_accolade(self, toAdd, toRemove):

        return True
    
    def set_class(self, character_class):
        if not self.level in [5,25,50,75]:
            print(f"{self.name} not at a class selection level!")   
            return False 
    
        if not character_class.meets_requirements(self): 
            print(f"{self.name} does not meet the requirements for class '{character_class.name}'")
            return False
        
        self.character_class = character_class
        print(f"Class '{character_class.name}' assigned successfully")

        # Update tree effects based on the assigned class
        for tree, bonus in character_class.tree_effect.items(): self.trees[tree].bonus = bonus
        self.update_skill_caps()
        #self.update_attributes()
        self.update_vitals()
        if type(character_class.additional_effect)==Modifier:
            self.add_mods("Class",character_class.additional_effect)

    def calculate_required_experience(self):
        if self.character_class is None or self.level < 5 or self.character_class.rarity in ["Common", "Uncommon"]:
            required_exp = 100 * (self.level ** 2 - self.level) // 2 + 100
        else:
            required_exp = math.floor(2000 * 1.15 ** self.level - 2000)
        return required_exp

    def add_experience(self, amount):
        amount = int(amount)
        current_exp = self.experience  # You should have a variable for tracking the character's experience
        required_exp = self.calculate_required_experience()

        self.total_xp -= current_exp
        
        new_exp = current_exp + amount

        if new_exp >= required_exp:
            while new_exp >= required_exp:
                ##Moved inside the while loop so it rechecks each level when getting lots of xp at once.
                if self.level == 5 and self.character_class == unclassed or self.level == 25 or self.level == self.level_cap:
                    max_exp = required_exp - 1
                    new_exp = min(new_exp, max_exp)
                    self.total_xp += new_exp
                    self.experience = new_exp
                    return True
                new_exp -= required_exp
                self.total_xp += required_exp
                self.level_up()
                required_exp = self.calculate_required_experience()

        self.total_xp += new_exp
        self.experience = new_exp

    def add_statistics(self, location, amount):
        self.general_statistics[location] += amount

    def level_up(self):
        if self.level < self.level_cap:
            self.level += 1
            print(f"Congratulations! {self.name} leveled up to level {self.level}!")
            self.update_free_attributes()

    def genSkillList (self):
        trees = deepcopy(self.trees)

        for tree in list(trees.values()):
            for tier in list(tree.tiers.values()):
                if not tier.skills: tree.tiers.pop(tier.tier)
                else:
                    skills = {}
                    for skill in tier.skills: skills.update({skill:self.skills[skill]})
                    tier.skills = skills
            if not tree.tiers: trees.pop(tree.name)

        return list(trees.values());

    def printCharSheet (self,altCol = False):
        temp = Template(open('CharSheetTemplate.html').read())
        pluscol = self.free_attributes > 0 or self.calculate_free_skill_points() > 0
        sheet = open(self.name+' CharSheet.html','w')
        sheet.write( temp.render(
                    aw = self,
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
                    TotXP = self.total_xp,
                    
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
                    totMSC = sum(self.attributes[4]),
                    
                    tolSTR = self.attributes[5][0],
                    tolRCV = self.attributes[5][1],
                    tolEND = self.attributes[5][2],
                    tolVGR = self.attributes[5][3],
                    tolFCS = self.attributes[5][4],
                    tolCLR = self.attributes[5][5],
                    tolPER = self.attributes[5][6],
                    tolSPD = self.attributes[5][7],
                    totTOL = self.attributes[5][8],
                    
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

                    Items = filter(None,list(self.inventory.values())),

                    totAccAct = self.calculate_used_accolade_slots(),
                    accolades = list(self.accolades.values()),
            ))

        sheet.close()