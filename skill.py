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

    def getNextRankXP(self):
        return (.5*self.rank*(self.rank - 1) + 1) * 2**self.tier * 100
    
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
                    self.cost['value'] = self.cost['value'] + (self.cost['value'] // self.rank)
                self.rank +=1
                print(self.name+" Leveled up!")
                nextXP = self.getNextRankXP()

        self.xp = currXP
        self.banked_xp = 0

    # Store xp for the next essence exchange
    def bank_exp(self, xp):
        self.banked_xp += xp
        # print(f"XP {xp} banked for {self.name}") # Was just a debug output

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
healers_synergy = Skill("Healers Synergy","Multiply intensity of healing skills by [1+0.002*RNK*restoration_ranks] <br> Requires 50 ranks in Restoration",2,"Restoration")
tissue_scan = Skill("Tissue Scan","Scan the body of a touched entity. <br> Resolution of resulting scan is equal to: [200 + 20*RNK] % of mundane optical vision <br> Cost: 5mp",2,"Restoration")

# Natureworking
natural_intuition = Skill("Natural Intuition","Develop an intuitive understanding of the mechanics of fibres <br> Higher ranks mean greater insight",0,"Natureworking")
cleave_fibers = Skill("Cleave Fibers", "Manipulate the bonds between fibers, binding them together or cutting them apart. <br> Alter volume of [RNK^3] cm<sup>3</sup> <br> Cost: 5*RNK mp",0,"Natureworking",cost={'type':"MP",'value':5})

# Chemistry
chemical_intuition = Skill("Chemical Intuition","Develop an intuitive understanding of the mechanics of mollecules <br> Higher ranks mean greater insight",0,"Chemistry")

# Alchemy
alchemic_intuition = Skill("Alchemic Intuition","Develop an intuitive understanding of the mechanics of atoms <br> Higher ranks mean greater insight",0,"Chemistry")

# Fire evocation
firebolt = Skill("Firebolt","A bolt of magical fire assails your target <br> Damage: [(5~7.5)*RNK*(1+FCS/100)] heat damage <br> Range: [10*RNK] m",0,"Fire Evocation",cost={'type':"MP",'value':10})
fire_affinity = Skill("Fire Affinity", "Multiply the intensity of all Fire skills by [1 + .1*RNK]",0,"Fire Evocation")

heat_mastery = Skill("Heat Mastery", "Multiply the intensity of all Heat skills by [1 + .1*RNK]",1,"Fire Evocation")

# Fire Manipulation
smoke_burst = Skill("Smoke Burst","Burst forward [RNK] meters in an instant, leaving a trail of fire in your wake. <br> Fire trail deals [(5~7)*RNK*(1+FCS/100)] heat damage to everything it touches <br> Cost: 15mp <br> Note: burst can be in wathever direction the casters decides incluiding to the air <br> Smoke abilities are Fire abilities, subject to fire affinity and heat mastery",1,"Fire Manipulation",cost={'type':'mp','value':15})

# Geoevocation
stonebolt = Skill("Stonebolt","A magical stone assails your target <br> Deal [(7.5-11)*RNK*(1+FCS/100)] force damage on hit <br> Range: 5*RNK meters <br> Cost: 10mp",0,"Geoevocation",cost={'type':"MP",'value':10})
rock_push = Skill("Rock Push", "Cost proportional to mass",0,"Geoevocation",cost={'type':"MP",'value':1})
stone_spray = Skill("Stone Spray", "Deal [(6-8)*(1+FCS/100)] force damage per hit. 2*RNK projectiles <br> Range: 1*RNK m <br> Cost: 20 mp <br> 5 ranks in Stonebolt",1,"Geoevocation",cost={'type':"MP",'value':20})

# Utility Auras
purify = Skill("Purify","Purify poison, corruption, and contamination <br> Range: [RNK] m <br> [10*RNK] mp/min",0,"Utility Auras",cost={'type':"MP",'value':10})

spring = Skill("Spring","Boost S.Regen by [10%*RNK] for all entities <br> Range: [RNK] m <br> Cost: [RNK] mp/hr",0,"Utility Auras",cost={'type':"MP",'value':1})

summer = Skill("Summer","Boost H.Regen by [10%*RNK] for all entities <br> Range: [RNK] m <br> Cost: [RNK] mp/hr",0,"Utility Auras",cost={'type':"MP",'value':1})

fall = Skill("Fall","Fall (hidden) <br> Reduce the need for food and water for all entities by [1%*RNK] <br> Range: [RNK] m <br> Cost: [RNK] mp/hr <br> Hidden Skill, Revealed by Meeting Requirement <br> Requires 5 ranks in Spring <br> Requires 5 ranks in Summer <br> Requires 5 ranks in Winter",0,"Utility Auras",cost={'type':"MP",'value':1})

winter = Skill("Winter","Boost M.Regen by [10%*RNK] for all entities <br> Range: [RNK] m <br> Cost: [RNK] mp/hr",0,"Utility Auras",cost={'type':"MP",'value':1})

# Aura Metamagic
amplify_aura = Skill("Amplify Aura", "Multiply aura intensity by [1+RNK/10] <br> Boost aura mana cost by [1+RNK/5]",0,"Aura Metamagic",cost={'type':"MP",'value':1})
extend_aura = Skill("Extend Aura", "Extend aura range by [RNK] m <br> Boost aura mana cost by [1+RNK/5]",0,"Aura Metamagic",cost={'type':"MP",'value':1})

aura_focus = Skill("Aura Focus", "Focus on an aura to boost its output <br> Multiply aura intensity by [1+RNK/5] <br> Multiply aura range by [1+RNK/5] <br> Multiply aura mana cost by [1+RNK/5] <br> User loses all external senses while focusing <br> Requires 5 ranks in amplify aura <br> Requires 5 ranks in extend aura",1,"Aura Metamagic",cost={'type':"MP",'value':1})
aura_synergy = Skill("Aura Synergy", "Aura Synergy <br> Increase all aura output by [0.1%*RNK] for each rank in any aura <br> Requires 1 rank in five different Auras",1,"Aura Metamagic")

aura_IFF = Skill("Aura IFF", "Aura IFF <br> User may exempt entities from direct aura effects at will <br> Selected entities receive [1-0.1*RNK] aura output <br> Requires 10 ranks in Amplify Aura <br> Requires 10 ranks in Extend Aura <br> Requires 10 ranks in Aura Focus",2,"Aura Metamagic")

aura_compression = Skill("Aura Compression","Aura Compression <br> Compress aura output, reducing range to boost intensity <br> Increase intensity by [0.2%*RNK] per meter of compression <br> Requires 50 ranks in Aura Metamagic <br> Requires 10 ranks in Aura IFF",3,"Aura Metamagic")

# Offensive Constructs
rammer = Skill("Rammer","A floating block of stone <br> Deals 3 (rnk * fcs * 0.5%) force damage by ramming into enemies. <br> 30 HP * RNK * (fcs * 0.5%) <br> Hardness:1*rnk (fcs * 0.2%) <br> Range: 30 * RNK meters <br> Costs 40 mana, 5mp/min to sustain.",0,"Offensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

magic_missile_turret = Skill("Magic Missile Turret","Hp 30 * RNK * (fcs * 0.5%) <br> Shoots a missile dealing 4-6  * RNK * (fcs * 0.75%) arcane damage every 5 seconds <br> Can target up to 1+RNK/5 targets <br> Causes mild disorientation <br> Cast range: 3xRNK meters <br> Mp cost 100   30mp/min",1,"Offensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

ominous_eye = Skill("Ominous Eye", "Summon Ominous Eye <br> Looks like a dark crystal eye <br> 20 hp (fcs * 0.5%) <br> Deals 5 * RNK * (fcs * 0.75%) dark damage every 3 seconds to enemies hit by it's eye beam. <br> Range: 10m * RNK <br> Enough damage will interrupt stamina regen on enemies. <br> Cast range 3xRNK meters <br> Cost 80mp 60mp/min",1,"Offensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

granite_golem = Skill("Granite Golem","50 hp * rnk (fcs * 1%) <br> Hardness: 2 * RNK * (fcs * 0.2%) <br> Deals 4 * RNK * (fcs * 0.5%) force damage. <br> Is intelligent enough to hold on to enemies and attempt to stop them from moving. <br> It is quite slow <br> Cast time: 20s <br> Cast range 3.x rnk meters <br> 250mp cost | 40mp/min sustain cost",1,"Offensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

# Defensive Constructs

mana_wall = Skill("Mana Wall","a wall of pure mana. <br> 50 HP (RNK * FCS * 1%) <br> Takes double damage from metal <br> Cast time 10 seconds <br> Cast range: 3xRNK meters <br> Mana cost 100mp 5mp/min",0,"Defensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

stone_tower = Skill("Stone Tower","Stone Tower with a ladder <br> 100 hp * RNK (fcs * 1%) <br> Hardness 1 * rnk (fcs * 0.5%) <br> 15 second cast time <br> Cost 300mp 100mp/min",1,"Defensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

stone_bunker = Skill("Stone Bunker","Bunker with windows <br> HP 125 * RNK * (fcs * 1%) <br> Hardness: 1.5 * rnk * (fcs * 1%) <br> 30 second cast time <br> Cast range: 3 * RNK.meters <br> 400mp cost.   100mp/min <br> Requires 5 ranks in tighter mana structures",2,"Defensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

# Utility Constructs

war_banner = Skill("War Banner", "Hp 30*RNK (fcs 0.5%) <br> Increases the damage of all constructs by 5% * RNK in a range of 3 * RNK meters. <br> Mp cost 50 * RNK  mana sustain 1 * RNK per minute <br> Cast range 3xRNK meters <br> Requires 8 ranks in an offensive constructs skill",1,"Utility Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

mana_bank = Skill("Mana Bank","40 hp * RNK (fcs * 0.5%) <br> Transfer 50 * RNK mp/min, split between each person in the mana bank <br> Does not apply to caster <br> Cast time: 10 seconds <br> Cast range 3 x RNK meters <br> Mp cost 100   Sustain cost 100 * RNK mp/min",1,"Utility Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

# Construct Metamagic

flexible_design = Skill("Flexible Design","You can increase the depth, width and height of any construct in any direction by 20% * RNK. <br> Does not affect stats, just size",0,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes
                        
tighter_mana_structures = Skill("Tighter Mana Structures","Increases durability of all constructs by 10% * RNK",0,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

more_pylons = Skill("More Pylons","Adds +1 * RNK to the limit of constructs you can have.",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

combined_arms = Skill("Combined Arms","Each rank in Offensive Constructs you have increase durability of defensive constructs by (RNK * 0.2%) <br> Each rank in defensive Constructs you have increase damage of offensive constructs by (RNK * 0.2%)",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

multi_build = Skill("Multi Build","You can start casting 1+(RNK/5) constructs at a time <br> (This means you do not have to wait for a spell to finish casting before you can begin casting the next one)",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

absorbent_constructs = Skill("Absorbent Constructs","Buffs that aren't from passives become 10% * RNK more powerful when applied to construct",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

insulated_walls = Skill("Insulated Walls", "Defensive constructs block environmental piercing and resistance piercing spells by 5% * RNK",2,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes