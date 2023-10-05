#Hard-coded list of all skill trees; add whenever you add skills for a new tree. Recombinants should be added for relevant trees through their own thing (method of Awakened?)
AllTreeList = ["Physical Passive","Physical Utility","Physicality","Equipment Use","Melee Weapons","Heavy Armor","Light Armor","Shieldwielding","Staff Combat","Swordplay","Fencing","Dagger Combat","Hurling","Sharpshooting","Tracking","Threat Attraction","Magical Utility","Aura Metamagic","Offensive Auras","Defensive Auras","Utility Auras","Elemental Archer","Evocation Metamagic","Fire Evocation","Ice Evocation","Geoevocation","Hydroevocation","Aeroevocation","Earth Manipulation","Water Manipulation","Air Manipulation","Arcane Metamagic","Arcane Mysteries","Arcane Utility","Arcane Shifter","Elemental Enhancement","Elemental Inhibition","Psionics","Restoration","Beams","Survivalist Utility","Monster Taming","Divination","Defensive Constructs","Force Metamagic","Blood Magic","Chemistry","Alchemy","Natureworking","Runecrafting","Stoneworking","Armor Crafting","Weapon Crafting","Artificing","Metalworking"]
for x in range(len(AllTreeList)+1,145): AllTreeList.append("Tree "+str(x))

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
        self.scaling = 0

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

    def get_modifier(self, awakened): return self.mod

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
    def __init__(self, name, description, tier, tree, cost={ 'type': "",'value': 0 }, baseCost = 0, keywords=[]):
        super().__init__(name, description, tier, tree, cost, keywords)
        self.baseCost = baseCost
        self.keywords.append('Sustain')

class Buff(Skill):
    def __init__(self, name, description, tier, tree, keywords=[]):
        super().__init__(name, description, tier, tree, keywords)
        self.keywords.append('Buff')

class Channel(Skill):
    def __init__(self, name, description, tier, tree, cost={ 'type': "",'value': 0 }, keywords=[]):
        super().__init__(name, description, tier, tree, keywords)
        self.cost = cost
        self.keywords.append('Channel')

class Aura(Channel):
    def __init__(self, name, description, tier, tree, cost={ 'type': "",'value': 0 }, keywords=[]):
        super().__init__(name, description, tier, tree, cost, keywords)

    def get_range(self,awakened): return self.rank * 1

# specific skills
class intrinsic_strength(Passive):
    def __init__(self):
        super().__init__("Intrinsic Strength","Multiply maximum Health by 1+(RNK/5)",0,"Physical Utility",keywords=[])
    
    def get_power(self, awakened): return 20*self.rank
    def describe(self,awakened): return f"Boost maximum Health by {self.get_power(awakened)}%"
    def get_modifier(self, awakened): return None

class intrinsic_recovery(Passive):
    def __init__(self):
        super().__init__("Intrinsic Recovery","Multiply Health regen by 1+(RNK/5)",0,"Physical Utility",keywords=[])

    def get_power(self, awakened): return 20*self.rank
    def describe(self,awakened): return f"Boost Health regen by {self.get_power(awakened)}%"
    def get_modifier(self, awakened): return None

class intrinsic_endurance(Passive):
    def __init__(self):
        super().__init__("Intrinsic Endurance","Multiply maximum Stamina by 1+(RNK/5)",0,"Physical Utility",keywords=[])
    
    def get_power(self, awakened): return 20*self.rank
    def describe(self,awakened): return f"Boost maximum Stamina by {self.get_power(awakened)}%"
    def get_modifier(self, awakened): return None

class intrinsic_vigor(Passive):
    def __init__(self):
        super().__init__("Intrinsic Vigor","Multiply mana Stamina by 1+(RNK/5)",0,"Physical Utility",keywords=[])

    def get_power(self, awakened): return 20*self.rank
    def describe(self,awakened): return f"Multiply mana Stamina by {self.get_power(awakened)}%"
    def get_modifier(self, awakened): return None

# Magical Utility
class intrinsic_focus(Passive):
    def __init__(self):
        super().__init__("Intrinsic Focus","Multiply maximum Mana by 1+(RNK/5)",0,"Magical Utility",keywords=[])
    
    def get_power(self, awakened): return 20*self.rank
    def describe(self,awakened): return f"Boost maximum Mana by {self.get_power(awakened)}%"
    def get_modifier(self, awakened): return None

class intrinsic_clarity(Passive):
    def __init__(self):
        super().__init__("Intrinsic Clarity","Multiply Mana regen by 1+(RNK/5)",0,"Magical Utility",keywords=[])

    def get_power(self, awakened): return 20*self.rank
    def describe(self,awakened): return f"Boost Mana regen by {self.get_power(awakened)}%"
    def get_modifier(self, awakened): return None

class magical_synergy(Passive):
    def __init__(self):
        super().__init__("Magical Synergy","Enables limited synergistic cross-coupling of magical attributes <br> [2.5%*RNK] of Focus contributes to M.Regen <br> [2.5%*RNK] of Clarity contributes to Mana <br> Requires 10 ranks in Intrinsic Clarity <br> Requires 10 ranks in Intrinsic Focus",2,"Magical Utility")
        
    def get_power(self, awakened): return 2.5*self.rank
    def describe(self, awakened): return f"Enables limited synergistic cross-coupling of magical attributes <br> {self.get_power(awakened)}% of Focus contributes to M.Regen <br> {self.get_power(awakened)}% of Clarity contributes to Mana <br> Requires 10 ranks in Intrinsic Clarity <br> Requires 10 ranks in Intrinsic Focus"

# Restoration
class healing_word(Instant):
    def __init__(self):
        super().__init__("Healing Word","Invoke a word of healing to restore health to a touched entity <br> Heal [10-20]*[RNK]*[1 + .005*FCS] hp <br> Cost: 10mp <br> Cannot Heal Self",0,"Restoration",cost={'type':"MP",'value':10},keywords=["Non-Combat","Healing"])

    def get_power(self, awakened): return 15*self.rank*(1 + awakened.attributes[1][4]/200)*(1 + awakened.get_skill_power("Healing Affinity")/100)
    def describe(self, awakened): return "Invoke a word of healing to restore health to a touched entity <br> Heal "+str(round(self.get_power(awakened)/1.5,2))+"-"+str(round(self.get_power(awakened)/.75,2))+" hp <br> Cost: 10mp <br> Cannot Heal Self"

stamina_transfer = Skill("Stamina Transfer","Sacrifice a portion of your stamina to energize a touched entity <br> Gives: [20*RNK] sp <br> Cost: [40*RNK] sp",0,"Restoration")

class purge_poison(Instant):
    def __init__(self):
        super().__init__("Purge Poison","Weaken and destroy poisons and toxins (fcs) <br> Reduce Chemical Effect damage by [20*RNK*(1 + .01*FCS)] <br> Range: Touch<br> Cost: 20mp <br> If damage is reduced to 0, the Effect is ended",1,"Restoration",cost={'type':"MP",'value':20},keywords=["Non-Combat","Healing"])

    def get_power(self, awakened): return 20*self.rank*(1 + awakened.attributes[1][4]/100)*(1 + awakened.get_skill_power("Healing Affinity")/100)
    def describe(self, awakened): return "Weaken and destroy poisons and toxins (fcs) <br> Reduce Chemical Effect damage by "+str(round(self.get_power(awakened),2))+" <br> Range: Touch<br> Cost: 20mp <br> If damage is reduced to 0, the Effect is ended"

regeneration = Skill("Regeneration","Instill a font of life within a target that slowly restores them (fcs) <br> Target recovers (1 + .01*FCS) health every second <br> Range: Touch<br> Cost: 50mp <br> Duration: .5*RNK m",1,"Restoration")

class healing_affinity(Passive):
    def __init__(self):
        super().__init__("Healing Affinity","Multiply intensity of healing skills by [1+0.1*RNK] <br> Requires 10 ranks in Restoration",1,"Restoration",Modifier(target="Healing"),keywords=["Non-Combat"])

    def get_power(self, awakened): return 10*self.rank
    def describe(self, awakened): return f"Boost intensity of healing skills by {self.get_power(awakened)}%"
    def get_modifier(self, awakened):
        return Modifier(
            target="Healing",
            power_buff=self.get_power(awakened)
        )

healers_synergy = Skill("Healers Synergy","Multiply intensity of healing skills by [1+0.002*RNK*restoration_ranks] <br> Requires 50 ranks in Restoration",2,"Restoration")

tissue_scan = Instant("Tissue Scan","Scan the body of a touched entity. <br> Resolution of resulting scan is equal to: [200 + 20*RNK] % of mundane optical vision <br> Cost: 5mp",2,"Restoration",cost={ 'type': "MP",'value': 5 })

# Natureworking
natural_intuition = Skill("Natural Intuition","Develop an intuitive understanding of the mechanics of fibres <br> Higher ranks mean greater insight",0,"Natureworking")

class cleave_fibers(Instant):
    def __init__(self):
        super().__init__("Cleave Fibers", "Manipulate the bonds between fibers, binding them together or cutting them apart. <br> Alter volume of [10*RNK]^3 cm<sup>3</sup> <br> Cost: 5*RNK mp",0,"Natureworking",cost={'type':"MP",'value':5},keywords=[])

    def get_power(self, awakened): return 100 * self.rank**3
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

# Runes
runic_intuition = Skill("Runic Intuition","Develop an intuitive understanding of the mechanics of Runes <br> Higher ranks mean greater insight",0,"Runecrafting")

energize_rune = Skill("Energize Rune","Convert up to 10*RNK tel to up to 10*RNK mana, at a rate of 1:1, and invest it into a touched rune",0,"Runecrafting")

class steady_scribing(Passive):
    def __init__(self):
        super().__init__("Steady Scribing", "Greater percision is greater power <br> +2%*RNK*(1 + .005*VGR) boost to the effects of all Rune skills", 0, "Runecrafting", mod=Modifier(target='Runes'), keywords=["Non-Combat","Runecrafting"])

    def get_power(self, awakened): return 5*self.rank*(1 + 0.01*awakened.attributes[1][3])
    def describe(self, awakened): return f"Greater percision is greater power <br> {self.get_power(awakened)}% boost to the effects of all created Runes"
    def get_modifier(self, awakened):
        return Modifier(
            target="Runes",
            power_buff=self.get_power(awakened)
        )
    
class runes_of_resevoirs(Passive):
    def __init__(self):
        super().__init__("Runes of Resevoirs","Gain a greater familiarity with the gathering and storing of energy <br> +2%*RNK*(1 + .005*STR) boost to the effects of relevant created runes  <br> Higher ranks mean stronger insight",1,"Runecrafting",keywords=["Non-Combat","Runes","Runecrafting"])
    
    def get_power(self, awakened): return 2*self.rank*(1 + 0.005*awakened.attributes[1][0])
    def describe(self, awakened): return f"Gain a greater familiarity with the gathering and storing of energy <br> {self.get_power(awakened)}% boost to the effects of relevant created runes  <br> Higher ranks mean stronger insight"
    def get_modifier(self, awakened):
        return Modifier(
            target="N/A",
            power_buff=self.get_power(awakened)
        )

class runes_of_living_enhancement(Passive):
    def __init__(self):
        super().__init__("Runes of Living Enhancement","Gain a greater familiarity with enhancing attributes <br> +2%*RNK*(1 + .005*STR) boost to the effects of relevant created runes  <br> Higher ranks mean stronger insight",1,"Runecrafting",keywords=["Non-Combat","Runes","Runecrafting"])

    def get_power(self, awakened): return 2*self.rank*(1 + 0.005*awakened.attributes[1][0])
    def describe(self, awakened): return f"Gain a greater familiarity with enhancing attributes <br> {self.get_power(awakened)}% boost to the effects of relevant created runes  <br> Higher ranks mean stronger insight"
    def get_modifier(self, awakened):
        return Modifier(
            target="N/A",
            power_buff=self.get_power(awakened)
        )

class runes_of_item_enhancement(Passive):
    def __init__(self):
        super().__init__("Runes of Item Enhancment","Gain a greater familiarity with enhancing the properties of materials <br> +2%*RNK*(1 + .005*STR) boost to the effects of relevant created runes  <br> Higher ranks mean stronger insight",1,"Runecrafting",keywords=["Non-Combat","Runes","Runecrafting"])

    def get_power(self, awakened): return 2*self.rank*(1 + 0.005*awakened.attributes[1][0])
    def describe(self, awakened): return f"Gain a greater familiarity with enhancing the properties of materials <br> {self.get_power(awakened)}% boost to the effects of relevant created runes  <br> Higher ranks mean stronger insight"
    def get_modifier(self, awakened):
        return Modifier(
            target="N/A",
            power_buff=self.get_power(awakened)
        )

class runes_of_defense(Passive):
    def __init__(self):
        super().__init__("Runes of Defense","Gain a greater familiarity with strengthening defenses <br> +2%*RNK*(1 + .005*STR) boost to the effects of relevant created runes  <br> Higher ranks mean stronger insight",1,"Runecrafting",keywords=["Non-Combat","Runes","Runecrafting"])

    def get_power(self, awakened): return 2*self.rank*(1 + 0.005*awakened.attributes[1][0])
    def describe(self, awakened): return f"Gain a greater familiarity with strengthening defenses <br> {self.get_power(awakened)}% boost to the effects of relevant created runes  <br> Higher ranks mean stronger insight"
    def get_modifier(self, awakened):
        return Modifier(
            target="N/A",
            power_buff=self.get_power(awakened)
        )

class runes_of_complexity(Passive):
    def __init__(self):
        super().__init__("Runes of Complexity","Gain a greater familiarity with connecting similar runes into Rune Complexes <br> +2%*RNK*(1 + .005*STR) boost to the effects of relevant created runes <br> Higher ranks mean stronger insight",1,"Runecrafting",keywords=["Non-Combat","Runes","Runecrafting"])

    def get_power(self, awakened): return 2*self.rank*(1 + 0.005*awakened.attributes[1][0])
    def describe(self, awakened): return f"Gain a greater familiarity with connecting similar runes into Rune Complexes <br> {self.get_power(awakened)}% boost to the effects of relevant created runes  <br> Higher ranks mean stronger insight"
    def get_modifier(self, awakened):
        return Modifier(
            target="N/A",
            power_buff=self.get_power(awakened)
        )

'''
Current list of Runecrafting skills;

T2
```Runes of Skill Imitation
Gain a greater familiarity with imitating other's capabilities through Runes
+2%*RNK*(1 + .005*STR) boost to the effects of relevant created runes
Higher ranks mean stronger insight
```
```Runes of Connection
Gain a greater familiarity with connecting seperate Runes and Rune Complexes into one network
+2%*RNK*(1 + .005*STR) boost to the effects of relevant created runes
Higher ranks mean stronger insight
Requires Runes of Complexity```
T3
```Runes of Skill Enhancement
Gain a greater familiarity with empowering other's capabilities through Runes
+2%*RNK*(1 + .005*STR) boost to the effects of relevant created runes
Higher ranks mean stronger insight
Requires Skill Imitation R5+```
'''

# Fire evocation
firebolt = Instant("Firebolt","A bolt of magical fire assails your target <br> Damage: [(5~7.5)*RNK*(1+FCS/100)] heat damage <br> Range: [10*RNK] m",0,"Fire Evocation",cost={'type':"MP",'value':10})
fire_affinity = Skill("Fire Affinity", "Multiply the intensity of all Fire skills by [1 + .1*RNK]",0,"Fire Evocation")

heat_mastery = Skill("Heat Mastery", "Multiply the intensity of all Heat skills by [1 + .1*RNK]",1,"Fire Evocation")
smoke_burst = Instant("Smoke Burst","Burst forward [RNK] meters in an instant, leaving a trail of fire in your wake. <br> Fire trail deals [(5~7)*RNK*(1+FCS/100)] heat damage to everything it touches <br> Cost: 15mp <br> Note: burst can be in wathever direction the casters decides incluiding to the air <br> Smoke abilities are Fire abilities, subject to fire affinity and heat mastery",1,"Fire Evocation",cost={'type':'mp','value':15})

# Geoevocation
stonebolt = Instant("Stonebolt","A magical stone assails your target <br> Deal [(7.5-11)*RNK*(1+FCS/100)] force damage on hit <br> Range: 5*RNK meters <br> Cost: 10mp",0,"Geoevocation",cost={'type':"MP",'value':10})
rock_push = Instant("Rock Push", "Cost proportional to mass",0,"Geoevocation",cost={'type':"MP",'value':1})
stone_spray = Instant("Stone Spray", "Deal [(6-8)*(1+FCS/100)] force damage per hit. 2*RNK projectiles <br> Range: 1*RNK m <br> Cost: 20 mp <br> 5 ranks in Stonebolt",1,"Geoevocation",cost={'type':"MP",'value':20})

# Utility Auras
purify = Aura("Purify","Purify poison, corruption, and contamination <br> Range: [RNK] m <br> [10*RNK] mp/min",0,"Utility Auras",cost={'type':"MP",'value':10})

winter = Aura("Winter","Boost M.Regen by [10%*RNK] for all entities <br> Range: [RNK] m <br> Cost: [RNK] mp/hr",0,"Utility Auras",cost={'type':"MP",'value':1})

# Aura Metamagic
amplify_aura = Passive("Amplify Aura", "Multiply aura intensity by [1+RNK/10] <br> Boost aura mana cost by [1+RNK/5]",0,"Aura Metamagic")
extend_aura = Passive("Extend Aura", "Extend aura range by [RNK] m <br> Boost aura mana cost by [1+RNK/5]",0,"Aura Metamagic")

aura_focus = Passive("Aura Focus", "Focus on an aura to boost its output <br> Multiply aura intensity by [1+RNK/5] <br> Multiply aura range by [1+RNK/5] <br> Multiply aura mana cost by [1+RNK/5] <br> User loses all external senses while focusing <br> Requires 5 ranks in amplify aura <br> Requires 5 ranks in extend aura",1,"Aura Metamagic")

# Offensive Constructs
rammer = Sustain("Rammer","A floating block of stone <br> Deals 3 (rnk * fcs * 0.5%) force damage by ramming into enemies. <br> 30 HP * RNK * (fcs * 0.5%) <br> Hardness:1*rnk (fcs * 0.2%) <br> Range: 30 * RNK meters <br> Costs 40 mana, 5mp/min to sustain.",0,"Offensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

magic_missile_turret = Sustain("Magic Missile Turret","Hp 30 * RNK * (fcs * 0.5%) <br> Shoots a missile dealing 4-6  * RNK * (fcs * 0.75%) arcane damage every 5 seconds <br> Can target up to 1+RNK/5 targets <br> Causes mild disorientation <br> Cast range: 3xRNK meters <br> Mp cost 100   30mp/min",1,"Offensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

ominous_eye = Sustain("Ominous Eye", "Summon Ominous Eye <br> Looks like a dark crystal eye <br> 20 hp (fcs * 0.5%) <br> Deals 5 * RNK * (fcs * 0.75%) dark damage every 3 seconds to enemies hit by it's eye beam. <br> Range: 10m * RNK <br> Enough damage will interrupt stamina regen on enemies.",1,"Offensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

granite_golem = Sustain("Granite Golem","50 hp * rnk (fcs * 1%) <br> Hardness: 2 * RNK * (fcs * 0.2%) <br> Deals 4 * RNK * (fcs * 0.5%) force damage. <br> Is intelligent enough to hold on to enemies and attempt to stop them from moving. <br> It is quite slow <br> Cast time: 20s <br> Cast range 3.x rnk meters <br> 250mp cost | 40mp/min sustain cost",1,"Offensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

# Defensive Constructs
mana_wall = Sustain("Mana Wall","a wall of pure mana. <br> 50 HP (RNK * FCS * 1%) <br> Takes double damage from metal <br> Cast time 10 seconds <br> Cast range: 3xRNK meters <br> Mana cost 100mp 5mp/min",0,"Defensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

stone_tower = Sustain("Stone Tower","Stone Tower with a ladder <br> 100 hp * RNK (fcs * 1%) <br> Hardness 1 * rnk (fcs * 0.5%) <br> 15 second cast time <br> Cost 300mp 100mp/min",1,"Defensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

stone_bunker = Sustain("Stone Bunker","Bunker with windows <br> HP 125 * RNK * (fcs * 1%) <br> Hardness: 1.5 * rnk * (fcs * 1%) <br> 30 second cast time <br> Cast range: 3 * RNK.meters <br> 400mp cost.   100mp/min <br> Requires 5 ranks in tighter mana structures",2,"Defensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

# Utility Constructs
war_banner = Sustain("War Banner", "Hp 30*RNK (fcs 0.5%) <br> Increases the damage of all constructs by 5% * RNK in a range of 3 * RNK meters. <br> Mp cost 50 * RNK  mana sustain 1 * RNK per minute <br> Cast range 3xRNK meters <br> Requires 8 ranks in an offensive constructs skill",1,"Utility Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

mana_bank = Sustain("Mana Bank","40 hp * RNK (fcs * 0.5%) <br> Transfer 50 * RNK mp/min, split between each person in the mana bank <br> Does not apply to caster <br> Cast time: 10 seconds <br> Cast range 3 x RNK meters <br> Mp cost 100   Sustain cost 100 * RNK mp/min",1,"Utility Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

# Construct Metamagic
flexible_design = Sustain("Flexible Design","You can increase the depth, width and height of any construct in any direction by 20% * RNK. <br> Does not affect stats, just size",0,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes
                        
tighter_mana_structures = Sustain("Tighter Mana Structures","Increases durability of all constructs by 10% * RNK",0,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

more_pylons = Sustain("More Pylons","Adds +1 * RNK to the limit of constructs you can have.",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

combined_arms = Sustain("Combined Arms","Each rank in Offensive Constructs you have increase durability of defensive constructs by (RNK * 0.2%) <br> Each rank in defensive Constructs you have increase damage of offensive constructs by (RNK * 0.2%)",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

multi_build = Sustain("Multi Build","You can start casting 1+(RNK/5) constructs at a time <br> (This means you do not have to wait for a spell to finish casting before you can begin casting the next one)",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

absorbent_constructs = Sustain("Absorbent Constructs","Buffs that aren't from passives become 10% * RNK more powerful when applied to construct",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

insulated_walls = Sustain("Insulated Walls", "Defensive constructs block environmental piercing and resistance piercing spells by 5% * RNK",2,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes