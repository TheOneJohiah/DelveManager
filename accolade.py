class Accolade:
    def __init__(self, name, description, rank, numStored):
        self.name = name
        self.description = description
        self.rank = rank
        self.numStored = numStored
        self.numActive = 0

# Vitals accolade
class Attributes(Accolade):
    def __init__(self, name, description, rank, numStored, attribute=[]):
        super().__init__(name, description, rank, numStored)

        # Max health/regen/stamina/regen/mana/regen
        self.attribute = attribute
    
    def describe(self):
        desc = ""
        for v in range(6):
            if self.attribute[v]>0: desc += f'+{self.attribute[v]*self.numActive} {["Health","H.Regen","Stamina","S.Regen","Mana","M.Regen"][v]}'
        return desc

# Stat accolade
class Stats(Accolade):
    def __init__(self, name, description, rank, numStored, stats=[]):
        super().__init__(name, description, rank, numStored)

        #str/rec/end/vig/foc/cla/per/spd
        self.stats = stats

    def describe(self):
        desc = ""
        for v in range(8):
            if self.stats[v]>0: desc += f'+{self.stats[v]*self.numActive} {["Strength","Recovery","Endurance","Vigor","Focus","Clarity","Perception","Speed"][v]}'
        return desc

# % Stat accolade
class PercentStats(Accolade):
    def __init__(self, name, description, rank, numStored, percentStats=[]):
        super().__init__(name, description, rank, numStored)

        #str/rec/end/vig/foc/cla/per/spd
        self.percentStats = percentStats

    def describe(self):
        desc = ""
        for v in range(8):
            if self.percentStats[v]>0: desc += f'+{self.percentStats[v]*self.numActive}% boost to the effects {["Strength","Recovery","Endurance","Vigor","Focus","Clarity","Perception","Speed"][v]}'
        return desc

# Resist accolade
class Resists(Accolade):
    def __init__(self, name, description, rank, numStored, resists=[]):
        super().__init__(name, description, rank, numStored)

        #heat/cold/light/dark/force/arcane/chemical/mental
        self.resists = resists

    def describe(self):
        desc = ""
        for v in range(8):
            if self.resists[v]>0: desc += f'+{self.resists[v]*self.numActive} {["Heat","Cold","Light","Dark","Force","Arcane","Chemical","Mental"][v]} Resistance'
        return desc

# Skill accolade

# Voucher accolade
class Voucher(Accolade):
    def __init__(self, name, description, rank, numStored, vouch={}):
        super().__init__(name, description, rank, numStored)

        #A single entry dict of type and amount?
        self.vouch = vouch

    def describe(self): return self.description


#greenfort = Accolade("Greenfort","50% stronger grip when climbing",2,0)
#lair_of_embers = Resists("The Lair of Embers","+1000 Heat Resistance",3,0,resists=[1000,0,0,0,0,0,0,0])
#oh_gods_not_another = Attributes("Oh Gods! Not Another Chem Lair!","+1000 Mana",2,0,attribute=[0,0,0,0,1000,0])

skars_glorious_return = Stats("Skar's Glorious Return","+10 to all main stats",2,0,stats=[10,0,10,0,10,0,0,0])
lava_vents = Stats("Lava Vents","+10 Strength",1,0,stats=[10,0,0,0,0,0,0,0])
flamewillow_grove = Stats("Flamewillow Grove","+10 Vigor",1,0,stats=[0,0,0,10,0,0,0,0])
sphinx_riddle = PercentStats("Sphinx Riddle","+50% Strength",2,0,percentStats=[50,0,0,0,0,0,0,0])