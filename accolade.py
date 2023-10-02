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

# Stat accolade
class Stats(Accolade):
    def __init__(self, name, description, rank, numStored, stats=[]):
        super().__init__(name, description, rank, numStored)

        #str/rec/end/vig/foc/cla/per/spd
        self.stats = stats

# % Stat accolade
class PercentStats(Accolade):
    def __init__(self, name, description, rank, numStored, percentStats=[]):
        super().__init__(name, description, rank, numStored)

        #str/rec/end/vig/foc/cla/per/spd
        self.percentStats = percentStats

# Resist accolade
class Resists(Accolade):
    def __init__(self, name, description, rank, numStored, resists=[]):
        super().__init__(name, description, rank, numStored)

        #heat/cold/light/dark/force/arcane/chemical/mental
        self.resists = resists

# Skill accolade

# Voucher accolade
class Voucher(Accolade):
    def __init__(self, name, description, rank, numStored, vouch={}):
        super().__init__(name, description, rank, numStored)

        #A single entry dict of type and amount?
        self.vouch = vouch


greenfort = Accolade("Greenfort","50% stronger grip when climbing",2,0)
lair_of_embers = Resists("The Lair of Embers","+1000 Heat Resistance",3,0,resists=[1000,0,0,0,0,0,0,0])
oh_gods_not_another = Attributes("Oh Gods! Not Another Chem Lair!","+1000 Mana",2,0,attribute=[0,0,0,0,1000,0])

skars_glorious_return = Stats("Skar's Glorious Return","+10 to all main stats",2,0,stats=[10,0,10,0,10,0,0,0])
lava_vents = Stats("Lava Vents","+10 Strength",1,0,stats=[10,0,0,0,0,0,0,0])
flamewillow_grove = Stats("Flamewillow Grove","+10 Recovery",1,0,stats=[0,0,0,10,0,0,0,0])
sphinx_riddle = Stats("Sphinx Riddle","+50% Strength",2,0,stats=[50,0,0,0,0,0,0,0])