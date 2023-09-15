#Hard-coded list of all skill trees; add whenever you add skills for a new tree. Recombinants should be added for relevant trees through their own thing (method of Awakened?)
AllTreeList = ["Physical Passive","Physical Utility","Physicality","Equipment Use","Melee Weapons","Heavy Armor","Light Armor","Shieldwielding","Staff Combat","Swordplay","Fencing","Dagger Combat","Hurling","Sharpshooting","Tracking","Threat Attraction","Magical Utility","Aura Metamagic","Offensive Auras","Defensive Auras","Utility Auras","Elemental Archer","Evocation Metamagic","Fire Evocation","Ice Evocation","Geoevocation","Hydroevocation","Aeroevocation","Earth Manipulation","Water Manipulation","Air Manipulation","Arcane Metamagic","Arcane Mysteries","Arcane Utility","Arcane Shifter","Elemental Enhancement","Elemental Inhibition","Psionics","Restoration","Beams","Survivalist Utility","Monster Taming","Divination","Defensive Constructs","Force Metamagic","Blood Magic","Chemistry","Alchemy","Natureworking","Runecrafting","Stoneworking","Armor Crafting","Weapon Crafting","Artificing","Metalworking"]

class Modifier:
    def __init__(self,target=None,power_buff=1,power_flat=0,range_buff=1,range_flat=0,duration_buff=1,duration_flat=0,cost_buff=1,cost_flat=0):
        self.target = target
        self.power_buff = power_buff
        self.power_flat = power_flat
        self.range_buff = range_buff
        self.range_flat = range_flat
        self.duration_buff = duration_buff
        self.duration_flat = duration_flat
        self.cost_buff = cost_buff
        self.cost_flat = cost_flat

class Tier:
    def __init__(self,tier):
        self.tier = tier
        self.lock = True
        self.skills = []

class Tree:
    def __init__(self,name):
        self.name = name
        self.bonus = 0
        self.tiers = {0:Tier(0),1:Tier(1),2:Tier(2),3:Tier(3),4:Tier(4)}
        self.tiers[0].lock = False

    #def count_ranks(self): return 0 #todo: implement? or keep as Awakened method?
    
    def unlock(self, tier): self.tiers[tier].lock = False

    def get_Skill(self,skillN):
        for x in range(5):
            if skillN in self.tiers[x]: return self.tiers[x][skillN]

class Skill:
    def __init__(self, name, description, tier, tree, keywords=[]):
        self.name = name
        self.keywords = []
        self.keywords.extend(keywords)
        self.rank_bonus = 0
        self.description = description
        self.tier = tier
        self.tree = tree
        self.rank = 1  # Initial rank is 1
        self.cap = 10 # Starting cap for all skills is 10
        self.xp = 0 # starting xp for all skills is 0
        self.banked_xp = 0

    def get_power(self,awakened): return 1
    
    def describe(self,awakened): return self.description
    
    def getNextRankXP(self): return int((.5*self.rank*(self.rank - 1) + 1) * 2**self.tier * 100)
    
    # Iterate through adding levels during essence exchange
    def add_exp (self):
        currXP = int(self.xp + self.banked_xp)
        nextXP = self.getNextRankXP()

        if currXP >= nextXP:
            while currXP >= nextXP:
                if self.rank == self.cap: self.currXP = 0; break
                currXP -= nextXP
                self.rank +=1
                print(self.name+" Leveled up!")
                nextXP = self.getNextRankXP()

        self.xp = currXP
        self.banked_xp = 0

    # Store xp for the next essence exchange
    def bank_exp(self, xp): self.banked_xp += xp

class Passive(Skill):
    def __init__(self, name, description, tier, tree, mod=Modifier(), keywords=[]):
        super().__init__(name, description, tier, tree, keywords)
        self.mod = mod
        self.keywords.append('Passive')

    def get_modifier(self): return self.mod

class Toggle(Passive):
    def __init__(self, name, description, tier, tree, keywords=[]):
        super().__init__(name, description, tier, tree, keywords)
        self.keywords.append('Toggle')
        self.active = True

    def toggle(self): self.active = not self.active
    def on(self): self.active = True
    def off(self): self.active = False

class Kata(Skill):
    def __init__(self, name, description, tier, tree, keywords=[]):
        super().__init__(name, description, tier, tree, keywords)
        self.keywords.append('Kata')

class Instant(Skill):
    def __init__(self, name, description, tier, tree, cost={'type':"",'value':0},keywords=[]):
        super().__init__(name, description, tier, tree, keywords)
        self.keywords.append('Instant')
        self.cost = cost
    
    def get_cost(self): return self.cost

class Evocation(Instant):
    def __init__(self, name, description, tier, tree, cost={'type': "",'value': 0},keywords=[]):
        super().__init__(name, description, tier, tree, cost, keywords)
        self.keywords.append('Evocation')

class Sustain(Instant):
    def __init__(self, name, description, tier, tree, cost={ 'type': "",'value': 0 }, keywords=[]):
        super().__init__(name, description, tier, tree, cost, keywords)
        self.keywords.append('Sustain')

class Buff(Skill):
    def __init__(self, name, description, tier, tree, keywords=[]):
        super().__init__(name, description, tier, tree, keywords)
        self.keywords.append('Buff')

class Channel(Skill):
    def __init__(self, name, description, tier, tree, keywords=[]):
        super().__init__(name, description, tier, tree, keywords)
        self.keywords.append('Channel')

class Aura(Channel):
    def __init__(self, name, description, tier, tree, keywords=[]):
        super().__init__(name, description, tier, tree, keywords)

    def get_range(self,awakened): return self.rank * 1

# specific skills
class intrinsic_strength(Passive):
    def __init__(self):
        super().__init__("Intrinsic Strength","Multiply maximum Health by 1+(RNK/5)",0,"Physical Utility",keywords=[])
    
    def get_power(self, awakened): return (self.rank/5)
    def describe(self,awakened): return f"Multiply maximum Health by {1 + self.get_power(awakened)}"
    def get_modifier(self): return None

class intrinsic_recovery(Passive):
    def __init__(self):
        super().__init__("Intrinsic Recovery","Multiply Health regen by 1+(RNK/5)",0,"Physical Utility",keywords=[])

    def get_power(self, awakened): return (self.rank/5)
    def describe(self,awakened): return f"Multiply Health regen by {1 + self.get_power(awakened)}"
    def get_modifier(self): return None

class intrinsic_endurance(Passive):
    def __init__(self):
        super().__init__("Intrinsic Endurance","Multiply maximum Stamina by 1+(RNK/5)",0,"Physical Utility",keywords=[])
    
    def get_power(self, awakened): return (self.rank/5)
    def describe(self,awakened): return f"Multiply maximum Stamina by {1 + self.get_power(awakened)}"
    def get_modifier(self): return None

class intrinsic_vigor(Passive):
    def __init__(self):
        super().__init__("Intrinsic Vigor","Multiply mana Stamina by 1+(RNK/5)",0,"Physical Utility",keywords=[])

    def get_power(self, awakened): return (self.rank/5)
    def describe(self,awakened): return f"Multiply mana Stamina by {1 + self.get_power(awakened)}"
    def get_modifier(self): return None

# Magical Utility
class intrinsic_focus(Passive):
    def __init__(self):
        super().__init__("Intrinsic Focus","Multiply maximum Mana by 1+(RNK/5)",0,"Magical Utility",keywords=[])
    
    def get_power(self, awakened): return (self.rank/5)
    def describe(self,awakened): return f"Multiply maximum Mana by {1 + self.get_power(awakened)}"
    def get_modifier(self): return None

class intrinsic_clarity(Passive):
    def __init__(self):
        super().__init__("Intrinsic Clarity","Multiply Mana regen by 1+(RNK/5)",0,"Magical Utility",keywords=[])

    def get_power(self, awakened): return (self.rank/5)
    def describe(self,awakened): return f"Multiply Mana regen by {1 + self.get_power(awakened)}"
    def get_modifier(self): return None


class magical_synergy(Passive):
    def __init__(self):
        super().__init__("Magical Synergy","Enables limited synergistic cross-coupling of magical attributes <br> [2.5%*RNK] of Focus contributes to M.Regen <br> [2.5%*RNK] of Clarity contributes to Mana <br> Requires 10 ranks in Intrinsic Clarity <br> Requires 10 ranks in Intrinsic Focus",0, "Magical Utility")
        
    def get_power(self, awakened): return self.rank/40
    def describe(self, awakened): return f"Enables limited synergistic cross-coupling of magical attributes <br> {100*self.get_power(awakened)}% of Focus contributes to M.Regen <br> {100*self.get_power(awakened)}% of Clarity contributes to Mana <br> Requires 10 ranks in Intrinsic Clarity <br> Requires 10 ranks in Intrinsic Focus"

# Restoration
class healing_word(Instant):
    def __init__(self):
        super().__init__("Healing Word","Invoke a word of healing to restore health to a touched entity <br> Heal [10-20]*[RNK]*[1 + .005*FCS] hp <br> Cost: 10mp <br> Cannot Heal Self",0,"Restoration",cost={'type':"MP",'value':10},keywords=["Healing"])

    def get_power(self, awakened): return 15*self.rank*(1 + awakened.attributes[1][4]/200)*(1 + awakened.get_skill_power("Healing Affinity"))
    def describe(self, awakened): return "Invoke a word of healing to restore health to a touched entity <br> Heal "+str(round(self.get_power(awakened)/1.5,2))+"-"+str(round(self.get_power(awakened)/.75,2))+" hp <br> Cost: 10mp <br> Cannot Heal Self"

stamina_transfer = Skill("Stamina Transfer","Sacrifice a portion of your stamina to energize a touched entity <br> Gives: [20*RNK] sp <br> Cost: [40*RNK] sp",0,"Restoration")

class purge_poison(Instant):
    def __init__(self):
        super().__init__("Purge Poison","Weaken and destroy poisons and toxins (fcs) <br> Reduce Chemical Effect damage by [20*RNK*(1 + .01*FCS)] <br> Range: Touch<br> Cost: 20mp <br> If damage is reduced to 0, the Effect is ended",1,"Restoration",cost={'type':"MP",'value':20},keywords=["Healing"])

    def get_power(self, awakened): return 20*self.rank*(1 + awakened.attributes[1][4]/100)*(1 + awakened.get_skill_power("Healing Affinity"))
    def describe(self, awakened): return "Weaken and destroy poisons and toxins (fcs) <br> Reduce Chemical Effect damage by "+str(round(self.get_power(awakened),2))+" <br> Range: Touch<br> Cost: 20mp <br> If damage is reduced to 0, the Effect is ended"

regeneration = Skill("Regeneration","Instill a font of life within a target that slowly restores them (fcs) <br> Target recovers (1 + .01*FCS) health every second <br> Range: Touch<br> Cost: 50mp <br> Duration: .5*RNK m",1,"Restoration")
class healing_affinity(Passive):
    def __init__(self):
        super().__init__("Healing Affinity","Multiply intensity of healing skills by [1+0.1*RNK] <br> Requires 10 ranks in Restoration",1,"Restoration",Modifier(target="Healing"),keywords=[])

    def get_power(self, awakened): return 0.1*self.rank
    def describe(self, awakened): return f"Multiply intensity of healing skills by {1 + self.get_power(awakened)}"
    def get_modifier(self):
        return Modifier(
            target="Healing",
            power_buff=self.get_power()
        )

healers_synergy = Skill("Healers Synergy","Multiply intensity of healing skills by [1+0.002*RNK*restoration_ranks] <br> Requires 50 ranks in Restoration",2,"Restoration")
tissue_scan = Skill("Tissue Scan","Scan the body of a touched entity. <br> Resolution of resulting scan is equal to: [200 + 20*RNK] % of mundane optical vision <br> Cost: 5mp",2,"Restoration")

# Natureworking
natural_intuition = Skill("Natural Intuition","Develop an intuitive understanding of the mechanics of fibres <br> Higher ranks mean greater insight",0,"Natureworking")

class cleave_fibers(Instant):
    def __init__(self):
        super().__init__("Cleave Fibers", "Manipulate the bonds between fibers, binding them together or cutting them apart. <br> Alter volume of [RNK^3] cm<sup>3</sup> <br> Cost: 5*RNK mp",0,"Natureworking",cost={'type':"MP",'value':5},keywords=[])

    def get_power(self, awakened): return self.rank**3
    def get_cost(self): return {'type':"MP",'value':5*self.rank}
    def describe(self, awakened): return f"Manipulate the bonds between fibers, binding them together or cutting them apart. <br> Alter volume of {self.get_power(awakened)} cm<sup>3</sup> <br> Cost: {self.get_cost()['value']} mp"

# Chemistry
chemical_intuition = Skill("Chemical Intuition","Develop an intuitive understanding of the mechanics of molecules <br> Higher ranks mean greater insight",0,"Chemistry")

class dissolve(Instant):
    def __init__(self):
        super().__init__("Dissolve","Dissolve a material into a solvent <br> Rate: 600/RNK s/m<sup>3</sup> <br> cost: 20*RNK sp",0,"Chemistry",cost={'type': "SP", 'value': 20},keywords=["Crafting","Chemistry"])

    def get_power(self, awakened): return 600/self.rank
    def get_cost(self): return {'type':"SP",'value':20*self.rank}
    def describe(self, awakened): return f"Dissolve a material into a solvent <br> Rate: {self.get_power(awakened)} s/m<sup>3</sup> <br> cost: {self.get_cost()['value']} sp"

class congeal(Instant):
    def __init__(self):
        super().__init__("Congeal","Extract a material from a solvent <br> Rate: 600/RNK s/L <br> cost: 20*RNK sp",0,"Chemistry",cost={'type': "SP", 'value': 20},keywords=["Crafting","Chemistry"])

    def get_power(self, awakened): return 600/self.rank
    def get_cost(self): return {'type':"SP",'value':20*self.rank}
    def describe(self, awakened): return f"Extract a material from a solvent <br> Rate: {self.get_power(awakened)} s/L <br> cost: {self.get_cost()['value']} sp"

# Alchemy
alchemic_intuition = Skill("Alchemic Intuition","Develop an intuitive understanding of the mechanics of atoms <br> Higher ranks mean greater insight",0,"Alchemy")

# Fire evocation
firebolt = Instant("Firebolt","A bolt of magical fire assails your target",0,"Fire Evocation",cost={'type':"MP",'value':10})

# Geoevocation
stonebolt = Instant("Stonebolt","A magical stone assails your target <br> Deal [(7.5-11)*RNK*(1+FCS/100)] force damage on hit <br> Range: 5*RNK meters <br> Cost: 10mp",0,"Geoevocation",cost={'type':"MP",'value':10})
rock_push = Instant("Rock Push", "Cost proportional to mass",0,"Geoevocation",cost={'type':"MP",'value':1})

# Utility Auras
purify = Instant("Purify","Purify poison, corruption, and contamination <br> Range: [RNK] m <br> [10*RNK] mp/min",0,"Utility Auras",cost={'type':"MP",'value':1})

winter = Instant("Winter","Boost M.Regen by [10%*RNK] for all entities <br> Range: [RNK] m <br> Cost: [RNK] mp/hr",0,"Utility Auras",cost={'type':"MP",'value':1})