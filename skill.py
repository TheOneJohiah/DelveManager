#Hard-coded list of all skill trees; add whenever you add skills for a new tree. Recombinants should be added for relevant trees through their own thing (method of Awakened?)
AllTreeList = ["Physical Passive","Physical Utility","Physicality","Equipment Use","Melee Weapons","Heavy Armor","Light Armor","Shieldwielding","Staff Combat","Swordplay","Fencing","Dagger Combat","Hurling","Sharpshooting","Tracking","Threat Attraction","Magical Utility","Aura Metamagic","Offensive Auras","Defensive Auras","Utility Auras","Elemental Archer","Evocation Metamagic","Fire Evocation","Ice Evocation","Hydroevocation","Geoevocation","Earth Manipulation","Arcane Metamagic","Arcane Mysteries","Arcane Utility","Arcane Shifter","Elemental Enhancement","Elemental Inhibition","Psionics","Restoration","Beams","Survivalist Utility","Monster Taming","Divination","Defensive Constructs","Force Metamagic","Blood Magic","Chemistry","Alchemy","Natureworking","Runecrafting","Stoneworking","Armor Crafting","Weapon-Crafting","Artificing","Metalworking"]

class Skill:
    def __init__(self, name, description, tier, tree,cost={'type':"",'value':0}):
        self.name = name
        self.description = description
        self.tier = tier
        self.tree = tree
        self.cost = cost
        self.rank = 1  # Initial rank is 1
        self.cap = 10 # Starting cap for all skills is 10
        self.xp = 0 # starting xp for all skills is 0
        self.banked_xp = 0

    def getNextRankXP(self): return (.5*self.rank*(self.rank - 1) + 1) * 2**self.tier * 100
    
    # Iterate through adding levels during essence exchange
    def add_exp (self):
        currXP = self.xp + self.banked_xp
        nextXP = self.getNextRankXP()

        if currXP >= nextXP:
            while currXP >= nextXP:
                if self.rank == self.cap:
                    max_exp = nextXP - 1
                    self.xp = min(currXP, max_exp)
                    self.banked_xp = 0
                    return True
                currXP -= nextXP
                if self.tree == "Utility Auras":
                    self.cost = self.cost + self.cost/self.rank
                self.rank +=1
                print(self.name+" Leveled up!")
                nextXP = self.getNextRankXP()

        self.xp = currXP
        self.banked_xp = 0

    # Store xp for the next essence exchange
    def bank_exp(self, xp): self.banked_xp += xp

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

# specific skills
# Magical Utility
intrinsic_clarity = Skill("Intrinsic Clarity","Multiply mana regen by 1+(RNK/5)",0,"Magical Utility")
intrinsic_focus = Skill("Intrinsic Focus","Multiply maximum mana by 1+(RNK/5)",0, "Magical Utility")
magical_synergy = Skill("Magical Synergy","Enables limited synergistic cross-coupling of magical attributes <br> [2.5%*RNK] of Focus contributes to M.Regen <br> [2.5%*RNK] of Clarity contributes to Mana <br>  Requires 10 ranks in Intrinsic Clarity <br> Requires 10 ranks in Intrinsic Focus",0, "Magical Utility")

# Restoration
healing_word = Skill("Healing Word","Invoke a word of healing to restore health to a touched entity <br> Heal [10-20]*[RNK]*[1 + .005*FCS] hp <br> Cost: 10mp <br> Cannot Heal Self",0,"Restoration",cost={'type':"MP",'value':10})
stamina_transfer = Skill("Stamina Transfer","Sacrifice a portion of your stamina to energize a touched entity <br> Gives: [20*RNK] sp <br> Cost: [40*RNK] sp",0,"Restoration")
purge_poison = Skill("Purge Poison","Weaken and destroy poisons and toxins (fcs) <br> Reduce Chemical Effect damage by  [20*RNK*(1 + .01*FCS)] <br> Range: Touch<br> Cost: 20mp <br> If damage is reduced to 0, the Effect is ended",1,"Restoration")
regeneration = Skill("Regeneration","Instill a font of life within a target that slowly restores them (fcs) <br> Target recovers (1 + .01*FCS) health every second <br> Range: Touch<br> Cost: 50mp <br> Duration: .5*RNK m",1,"Restoration")
healing_affinity = Skill("Healing Affinity","Multiply intensity of healing skills by [1+0.1*RNK] <br> Requires 10 ranks in Restoration",1,"Restoration")
healers_synergy = Skill("Healers Synergy","Multiply intensity of healing skills by [1+0.002*RNK*restoration_ranks] <br> Requires 50 ranks in Restoration",2,"Restoration")
tissue_scan = Skill("Tissue Scan","Scan the body of a touched entity. <br> Resolution of resulting scan is equal to: [200 + 20*RNK] % of mundane optical vision <br> Cost: 5mp",2,"Restoration")

# Natureworking
natural_intuition = Skill("Natural Intuition","Develop an intuitive understanding of the mechanics of fibres <br> Higher ranks mean greater insight",0,"Natureworking")
cleave_fibers = Skill("Cleave Fibers", "Manipulate the bonds between fibers, binding them together or cutting them apart. <br> Alter volume of [RNK^3] cm<sup>3</sup> <br> Cost: 5*RNK mp",0,"Natureworking",cost={'type':"MP",'value':5})

# Chemistry
chemical_intuition = Skill("Chemical Intuition","Develop an intuitive understanding of the mechanics of mollecules <br> Higher ranks mean greater insight",0,"Chemistry")
dissolve = Skill("Dissolve","Dissolve a material into a solvent <br> Rate: 600/RNK s/m<sup>3</sup> <br> cost: 20*RNK sp",0,"Chemistry",cost={'type': "SP", 'value': 20})
congeal = Skill("Congeal","Extract a material from a solvent <br> Rate: 600/RNK s/L <br> cost: 20*RNK sp",0,"Chemistry",cost={'type': "SP", 'value': 20})

# Alchemy
alchemic_intuition = Skill("Alchemic Intuition","Develop an intuitive understanding of the mechanics of atoms <br> Higher ranks mean greater insight",0,"Alchemy")

# Fire evocation
firebolt = Skill("Firebolt","A bolt of magical fire assails your target",0,"Fire Evocation",cost={'type':"MP",'value':10})

# Geoevocation
stonebolt = Skill("Stonebolt","A magical stone assails your target <br> Deal [(7.5-11)*RNK*(1+FCS/100)] force damage on hit <br> Range: 5*RNK meters <br> Cost: 10mp",0,"Geoevocation",cost={'type':"MP",'value':10})
rock_push = Skill("Rock Push", "Cost proportional to mass",0,"Geoevocation",cost={'type':"MP",'value':1})

# Utility Auras
purify = Skill("Purify","Purify poison, corruption, and contamination <br> Range: [RNK] m <br> [10*RNK] mp/min",0,"Utility Auras",10)

winter = Skill("Winter","Boost M.Regen by [10%*RNK] for all entities <br> Range: [RNK] m <br> Cost: [RNK] mp/hr",0,"Utility Auras",1)