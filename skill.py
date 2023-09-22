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
                if self.tree == "Utility Auras" or self.name == "Liquefaction":
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

mana_manipulation = Skill("Mana Manipulation","Allows internal control of mana <br> Allows expulsion of mana to environment <br> Allows transfer of mana to and from capacitive items with direct contact <br> Alternative formula [100*RNK*(1+FCS/50)]",1,"Magical Utility",cost={'type':"MP",'value':1}) #Just setting to be 1 to 1 for now

magical_synergy = Skill("Magical Synergy","Enables limited synergistic cross-coupling of magical attributes <br> [2.5%*RNK] of Focus contributes to M.Regen <br> [2.5%*RNK] of Clarity contributes to Mana <br>  Requires 10 ranks in Intrinsic Clarity <br> Requires 10 ranks in Intrinsic Focus",2, "Magical Utility")

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

stone_spear = Skill("Stone Spear","Fire a single large chunk of stone. Sufficient damage can stun target. <br> [30-40*RNK*(1+(FCS*0.75)/100)] force damage <br> Range: 5*RNK m <br> Cost: 50 mp <br> 5 ranks in Stone Spray, Rock Push, Stonebolt",2,"Geoevocation",cost={'type':"MP",'value':50})
stone_synergy = Skill("Stone Synergy","Increase all Stone-keyword spells output by 0.1% per rank of this skill for each rank in any Stone-keyword spells <br> Requires 1 rank in five different Stone-keyword spells",2,"Geoevocation")

# Earth Manipulation
earth_affinity = Skill("Earth Affinity","Boosts skills with the Earth subelement keyword, but not all effects of that element <br> Boost Earth keyword skills by [1+RNK/10] <br> Requires: 1 rank in three Earth keyword skills.",0,"Earth Manipulation")

earthmolding = Skill("Earthmolding","Channeled, freely shape earth <br> Finer control with higher ranks <br> Cost: 1 mp/min",1,"Earth Manipulation",cost={'type':"MP",'value':1})
liquefaction = Skill("Liquefaction","Channeled liquefaction of earthen material. Increases ease of use for molding. Volume depends on intensity <br> Immobilizes entities on contact, sufficient contact leads to suffocation if head is covered <br> Range: 5*RNK m <br> Cost: 5*RNK/s <br> Requires 5 ranks in earthmolding",1,"Earth Manipulation",cost={'type':"MP",'value':5})

stoneset = Skill("Stoneset","Condenses loose earth and mud into stone  <br> Requires physical contact with target material <br> Cost scales with volume <br> Temporary unless boosted <br> Requires 5 ranks in liquefaction",2,"Earth Manipulation",cost={'type':"MP",'value':1}) #Haven't decided on an actual cost yet
stonemolding = Skill("Stonemolding","Channeled, freely shape stone. Finer control with higher ranks <br> Cost: 15 mp/s <br> Requires 5 ranks in earthmolding, liquefaction",2,"Earth Manipulation",cost={'type':"MP",'value':5})

rooted = Skill("Rooted","Harvest the power of the Earth, boosting earth magic and rooting yourself in place. <br> 1+(RNK/20) effectiveness to Earth keyword spells, RNK/10 if environment is majority deepstone <br> User is [1+(RNK/10)*(1+END/100)] times harder to knock back, dependant of material user stands on <br> Automatically deactivates if user loses contact with the ground for more than 3 seconds <br> Requires focus to maintain <br> Requires 5 ranks in Earth Affinity",3,"Earth Manipulation")

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
ice_wall = Skill("Ice Wall","60 * RNK (fcs * 1%) HP <br> 1 * RNK (fcs * 0.1%) hardness <br> Gives +4 * RNK * (fcs * 0.5%) heat resistance to any allies within 1m * RNK of the wall <br> Cast time 10 seconds <br> Cast range 2m * RNK <br> 150 mp cost 30mp/min",1,"Defensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

stone_bunker = Skill("Stone Bunker","Bunker with windows <br> HP 125 * RNK * (fcs * 1%) <br> Hardness: 1.5 * rnk * (fcs * 1%) <br> 30 second cast time <br> Cast range: 3 * RNK.meters <br> 400mp cost.   100mp/min <br> Requires 5 ranks in tighter mana structures",2,"Defensive Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

# Utility Constructs
lamp_post = Skill("Lamp Post","Emits light in a 2 * RNK meter radius <br> 10hp * RNK (fcs 0.5%) <br> Must be within 50m RNK from caster <br> Cost 20 mp 2mp/min sustain <br> Can be carried.",0,"Utility Constructs",cost={'type':"MP",'value':2}) #The per minute cost

war_banner = Skill("War Banner", "Hp 30*RNK (fcs 0.5%) <br> Increases the damage of all constructs by 5% * RNK in a range of 3 * RNK meters. <br> Mp cost 50 * RNK  mana sustain 10 * RNK per minute <br> Cast range 3xRNK meters <br> Requires 8 ranks in an offensive constructs skill",1,"Utility Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes
mana_bank = Skill("Mana Bank","40 hp * RNK (fcs * 0.5%) <br> Transfer 50 * RNK mp/min, split between each person in the mana bank <br> Does not apply to caster <br> Cast time: 10 seconds <br> Cast range 3 x RNK meters <br> Mp cost 100   Sustain cost 100 * RNK mp/min",1,"Utility Constructs",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes
power_station = Skill("Power Station","Multiplies the effect of any utility construct it is connected to by 1+(RNK/10) and it's cost by 1+(RNK/5) <br> Can connect to RNK constructs <br> Has a max range of 15m * RNK <br> Mp cost 150mp sustain cost 30 * RNK mp /min",1,"Utility Constructs")

# Construct Metamagic
flexible_design = Skill("Flexible Design","You can increase the depth, width and height of any construct in any direction by 20% * RNK. <br> Does not affect stats, just size",0,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes
tighter_mana_structures = Skill("Tighter Mana Structures","Increases durability of all constructs by 10% * RNK",0,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

more_pylons = Skill("More Pylons","Adds +1 * RNK to the limit of constructs you can have.",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes
combined_arms = Skill("Combined Arms","Each rank in Offensive Constructs you have increase durability of defensive constructs by (RNK * 0.2%) <br> Each rank in defensive Constructs you have increase damage of offensive constructs by (RNK * 0.2%)",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes
multi_build = Skill("Multi Build","You can start casting 1+(RNK/5) constructs at a time <br> (This means you do not have to wait for a spell to finish casting before you can begin casting the next one)",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes
absorbent_constructs = Skill("Absorbent Constructs","Buffs that aren't from passives become 10% * RNK more powerful when applied to construct",1,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

insulated_walls = Skill("Insulated Walls", "Defensive constructs block environmental piercing and resistance piercing spells by 5% * RNK",2,"Construct Metamagic",cost={'type':"MP",'value':10}) #Arbitrary mana cost for leveling purposes

# Sharpshooting
drilling_shot = Skill("Drilling Shot","Shoot an arrow that spins, dealing increased damage <br> Multiplies base physical damage by [1+(RNK/10)*(1+STR/200)] <br> Cost: 10 sp",0,"Sharpshooting",cost={'type':"SP",'value':10})
seeker_shot = Skill("Seeker Shot","Shoot an arrow that tracks its target <br> Turn speed [(RNK*90)*(1+FCS/200)] deg/s <br> Tracking effect expires after [RNK*10] m <br> Cost: 10 sp",0,"Sharpshooting",cost={'type':"SP",'value':10})

hardened_arrowheads = Skill("Hardened Arrowheads","Hardened Arrowheads <br> Hardness of arrows multiplied by [1+RNK/10] <br> Requires 5 ranks in Sharpshooting",1,"Sharpshooting")
sturdy_bow = Skill("Sturdy Bow","Durability of bows multiplied by [1+RNK/10] <br> Requires 5 ranks in Sharpshooting",1,"Sharpshooting")
strong_draw = Skill("Strong Draw","Bow draw weight multiplied by [1+RNK/10] <br> Toggleable <br> Requires 5 ranks in Sharpshooting",1,"Sharpshooting")
piercing_shot = Skill("Piercing Shot","Shoot an arrow that ignores [RNK*5%] of target’s hardness <br> If physical damage is dealt, arrow pierces through the target <br> After piercing, physical damage to any secondary target is reduced by the hardness of the primary target <br> After piercing, magical damage to any secondary target is reduced by the appropriate resistance of the primary target <br> Effect can recurse indefinitely <br> Cost: 25 sp <br> Requires 5 ranks in Drilling Shot",1,"Sharpshooting",cost={'type':"SP",'value':25})

sharpened_arrowheads = Skill("Sharpened Arrowheads","Multiply physical damage of arrows by [1+RNK/10] <br> Requires 5 ranks in Hardened Arrowheads",2,"Sharpshooting")
endless_quiver = Skill("Endless Quiver","Conjure a copy of any arrow in your possession <br> Copy persists for [RNK] minutes <br> Cost: [100/RNK] sp + [SM] mp <br> Requires 10 ranks in Hardened Arrowheads",2,"Sharpshooting",cost={'type':"SP",'value':1}) #Leaving cost at 1 since it has a rank based formula
pinning_shot = Skill("Pinning Shot","Fire a shot that roots an enemy <br> Effect only activates if physical damage is dealt <br> Cost: 50 sp <br> Root the enemy for r [RNK*6] seconds <br> Requires ranks in Seeker Shot",2,"Sharpshooting",cost={'type':"SP",'value':50})
sniper_shot = Skill("Sniper Shot (Hidden)","Fire a powerful charged shot with extreme range <br> Multiply physical damage by [1+(RNK/3.33)*(1+STR/100)] <br> Arrow is not affected by gravity or wind within 1km <br> Cost: 100 sp <br> Charge time: 10s <br> Hidden Skill, Revealed by Meeting Requirement <br> Requires 10 ranks in Piercing Shot <br> Requires 10 ranks in Drilling Shot",2,"Sharpshooting",cost={'type':"SP",'value':100})

bleeder_shot = Skill("Bleeder Shot","Shoot an arrow that drains the target’s blood <br> Effect only activates if physical damage is dealt to health <br> Target bleeds freely for [RNK] minutes until wound is sealed <br> Bloodless entities are not affected by bleeding <br> Cost: 200 sp <br> Requires 5 ranks in Sharpened Arrowheads <br> Requires 5 ranks in Pinning Shot",3,"Sharpshooting",cost={'type':"SP",'value':200})
splinter_shot = Skill("Splinter Shot","Arrow splits into [2*RNK] arrows just before impact with the original target, striking up to [2*RNK] enemies within [RNK/2] m <br> Split arrows deal [50%/RNK] of the original’s damage <br> Split arrows have [50%/RNK] of the original’s hardness and durability <br> Cost: None <br> Requires 50 ranks in Sharpshooting",3,"Sharpshooting")
multishot = Skill("Multishot (Hidden)","Fire an arrow that splits into [RNK*2] projectiles <br> Each projectile deals 10% of the original damage <br> Arrows fly in a fan up to 45 degrees wide, equally spaced <br> Cost: [10*RNK] mp <br> Hidden Skill, Revealed by Meeting Requirement <br> Requires 10 ranks in Mana Manipulation <br> Requires 10 ranks in Endless Quiver",3,"Sharpshooting",cost={'type':"MP",'value':1}) #Just scales off rank, add to aura section maybe? Arbitrary cost for now
stacked_shot = Skill("Stacked Shot","Up to [1+RNK] Shot skills may be combined <br> Cost: additive <br> Requires 60 ranks in Shot skills",4,"Sharpshooting") #Just use .bank_xp

# Elemental Archer
fire_arrow = Skill("Fire Arrow","Wreathe an arrow in flames <br> [(5~10)*RNK*(1+FCS/200)] Heat on impact <br> Sufficient damage causes ignition <br> Cost: 5 mana",0,"Elemental Archer",cost={'type':"MP",'value':5})
ice_arrow = Skill("Ice Arrow", "Encrust an arrow with ice <br> [(5~10)*RNK*(1+FCS/200)] Cold on impact <br> Sufficient damage causes slow <br> Cost: 5 mana",0,"Elemental Archer",cost={'type':"MP",'value':5})

shock_arrow = Skill("Shock Arrow", "Charge an arrow with lightning <br> [(5~10)*RNK*(1+FCS/200)] Arcane on impact <br> Sufficient damage causes paralysis <br> Cost: 5 mana",1,"Elemental Archer",cost={'type':"MP",'value':5})
poison_arrow = Skill("Poison Arrow","Douse an arrow in poison <br> [(10~20)*RNK*(1+FCS/200)] Chemical over 10 seconds <br> Effect only activates if physical damage is dealt <br> Sufficient damage disrupts regeneration <br> Cost: 5 mana",1,"Elemental Archer",cost={'type':"MP",'value':5})
stone_arrow = Skill("Stone Arrow","Jacket an arrow with stone <br> [(5~10)*RNK*(1+FCS/200)] Force on impact <br> Arrow will not be affected by wind <br> Cost: 5 mana",1,"Elemental Archer",cost={'type':"MP",'value':5})
arrow_affinity = Skill("Arrow Affinity","Multiply elemental damage of arrows by [1+RNK/10] <br> Requires 1 skill of each element <br> Requires at least 10 ranks in Elemental Archery",1,"Elemental Archer")

radiant_arrow = Skill("Radiant Arrow","Envelop an arrow with the power of the sun <br> [(5~10)*RNK*(1+FCS/200)] Light on impact <br> Arrow velocity is increased to maximum <br> Physical damage is not affected <br> Cost: 5 mana <br> Requires 10 ranks in Fire Arrow",2,"Elemental Archer",cost={'type':"MP",'value':5})
stygian_arrow = Skill("Stygian Arrow","Cloak an arrow in the shadow of night <br> [(5~10)*RNK*(1+FCS/200)] Dark on impact <br> Arrow release, impact, and flight are muffled <br> Cost: 5 mana <br> Requires 10 ranks in Ice Arrow",2,"Elemental Archer",cost={'type':"MP",'value':5})

# Elemental Enhancement
concussive_blows = Skill("Concussive Blows","Single target buff, <br> Adds 6 force damage to all attacks <br> within 60 min (1% fcs) <br> Cost: 10 mana",0,"Elemental Enhancement",cost={'type':"MP",'value':10})
stygian_mind = Skill("Stygian Mind","Single target buff, <br> Adds 6 dark damage to all attacks <br> within 60 min (1% fcs) <br> Cost: 10 mana",0,"Elemental Enhancement",cost={'type':"MP",'value':10})
radiant_soul = Skill("Radiant Soul","Single target buff, <br> Adds 6 radiant damage to all attacks <br> within 60 min (1% fcs) <br> Cost: 10 mana",0,"Elemental Enhancement",cost={'type':"MP",'value':10})

frost_raiment = Skill("Frost Raiment","Single target buff, <br> Adds 3 cold damage to all attacks and 3 heat resistance <br> within 60 min (1% fcs) <br> Cost: 10 mana",1,"Elemental Enhancement",cost={'type':"MP",'value':10})
inner_fire = Skill("Inner Fire","Single target buff, <br> Adds 3 heat damage to all attacks and 3 cold resistance <br> within 60 min (1% fcs) <br> Cost: 10 mana",1,"Elemental Enhancement",cost={'type':"MP",'value':10})

stubbornness = Skill("Stubbornness","Single target buff, <br> Adds 6 mental resistance <br> within 60 min (1% fcs) <br> Cost: 10 mana",2,"Elemental Enhancement",cost={'type':"MP",'value':10})
