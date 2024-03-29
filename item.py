class Material:
    def __init__(self, name):
        self.name = name

    #def describe(self): return describe(self);
    def describe(self): return "<ul><li>name:"+self.name+"</li></ul>";

global describe
def describe (thing):
    attributes = [attr for attr in dir(thing) if not callable(getattr(thing, attr)) and not attr.startswith("__")]
    descr = "<ul>" #initialize description
    for attr in attributes:
        val = getattr(thing, attr)
        desc = ""
        if callable(hasattr(val, 'describe')): desc = attr.describe()
        elif type(val) == list:
            if not val: desc = "None"
            elif hasattr(val[0], 'describe'):
                desc += "[<ul>"
                for item in val:
                    desc += "<li>"+describe(item)+"</li>"
                desc += "</ul>]"
            else: desc = str(val).replace('<','{').replace('>','}')
        elif hasattr(val,'name'): desc = str(getattr(val,'name'))
        else: desc = str(val).replace('<','{').replace('>','}')

        descr += "<li>"+attr+": "+desc+"</li>"
        #print(descr+"</ul>")
    return descr+"</ul>"

class Enchantment:
    def __init__(self, name, description, mana_cost=0, per_activation=False, active=True, toggleable=False):
        self.name = name
        self.description = description
        self.mana_cost = mana_cost
        self.per_activation = per_activation
        self.active = active
        self.toggleable = toggleable

    def toggle(self):
        #Flip active state if enchantment is toggleable
        if self.toggleable == True:
            self.active = not self.active

    #Call from rune if rune has mana capacitance
    def spend_mana(self, mana_cost, per_activation):
        if per_activation == False:
            return mana_cost
        return True
    
    def describe(self): return describe(self);

class ResistanceEnchantment(Enchantment):
    def __init__(self, name, description, resistance_buff, mana_cost, active=True, toggleable=False):
        super().__init__(name, description, mana_cost, active, toggleable)
        # array [], location 0 through 7, heat/cold/light/dark/force/arcane/chemical/mental
        self.resistance_buff = resistance_buff

class AttributeEnchantment(Enchantment):
    def __init__(self, name, description, attribute_buff, mana_cost, active=True, toggleable=False):
        super().__init__(name, description, mana_cost, active, toggleable)
        # array [], 0 through 7, str/rec/end/vig/foc/cla/per/spd
        self.attribute_buff = attribute_buff

#Durability, hardness, sharpness, weight % increase
class ItemStatEnchantment(Enchantment):
    def __init__(self, name, description, percent_buff, buff_type, mana_cost, active=True, toggleable=False):
        super().__init__(name, description, mana_cost, active, toggleable)
        self.percent_buff = percent_buff
        self.buff_type = buff_type

class MiscellaneousEnchantment(Enchantment):
    def __init__(self, name, description, mana_cost, abstract_effect=None, skill_bonus=None, per_activation=False, active=True, toggleable=False):
        super().__init__(name, description, mana_cost, per_activation, active, toggleable)
        self.abstract_effect = abstract_effect
        self.skill_bonus = skill_bonus

class RepairEnchantment(Enchantment):
    def __init__(self, name, description, mana_cost_per_repair, repair_rate, conditions):
        super().__init__(name, description)
        self.mana_cost_per_repair = mana_cost_per_repair
        self.repair_rate = repair_rate
        self.conditions = conditions

class ManaCapacitanceEnchantment(Enchantment):
    def __init__(self, name, description, storage_capacity, input_efficiency, output_efficiency, mana_leakage_rate):
        super().__init__(name, description)
        self.storage_capacity = storage_capacity

        #Both between 0 and 100%
        self.input_efficiency = input_efficiency
        self.output_efficiency = output_efficiency

        #Some number per time unit
        self.mana_leakage_rate = mana_leakage_rate

class Rune:
    def __init__(self, name, enchantments=None, slot_requirement="Any"):
        self.name = name
        self.enchantments = enchantments if enchantments is not None else []
        self.slot_requirement = slot_requirement

    def deplete_charge(self, enchantments, amount):
        #TODO: if item has Capacitance rune, then deplete charge from it.
        ##depletion amount for time passing on passive runes calculated outside this function
        ##if mana below 0, rune deactivates.
        return True
    
    def describe(self): return describe(self);


class Item:
    def __init__(self, name, description, material, durability, hardness, manaSat, manaConvert, manaDissipate, runes=None):
        self.name = name
        self.description = description
        self.material = material
        self.runes = runes if runes is not None else []
        self.durability = durability
        self.hardness = hardness
        self.manaSat = manaSat
        self.manaConvert = manaConvert
        self.manaDissipate = manaDissipate

    def toggle_rune(self):
        return True

    def describe(self): return describe(self);
    
class Equipment(Item):
    def __init__(self, name, description, material, slot, durability, hardness, manaSat, manaConvert, manaDissipate, runes=None):
        super().__init__(name, description, material, durability, hardness, manaSat, manaConvert, manaDissipate, runes)
        self.slot = slot

class Weapon(Equipment):
    def __init__(self, name, description, material, durability, hardness, manaSat, manaConvert, manaDissipate, slot, weight, sharpness, runes=None):
        super().__init__(name, description, material, slot, durability, hardness, manaSat, manaConvert, manaDissipate, runes) #Keep track of order!!
        self.weight = weight
        self.sharpness = sharpness

# Creating materials
force_oak = Material("Force Oak")
force_steel = Material("Force Steel")
heat_copper = Material("Heat Copper")
dark_steel = Material("Dark Steel")
grand_arcane_atantum = Material("Grand Arcane Atantum")

# Creating enchantments
resistance_enchantment = ResistanceEnchantment("Grand Arcane Resistance", "Provides resistances", resistance_buff=[0, 0, 0, 0, 0, 5000, 0, 0], mana_cost=100)
attribute_enchantment = AttributeEnchantment("Grand AllStat enchant", "Boosts attributes", attribute_buff=[150, 150, 150, 150, 150, 150, 0, 0], mana_cost=1200, toggleable=True)
mana_capacitance = ManaCapacitanceEnchantment("Lesser Mana Capacitance", "Stores mana", 10000, 0.7, 0.1, 1)
##Placeholder enchantment type variable. Replace with dict? Array?
durability_enchantment = ItemStatEnchantment("Enhanced Durability", "Boosts item durability cap", 10, "durability", mana_cost=20)
blade_sharpness = ItemStatEnchantment("Greater sharpness", "increase to sharpness", 0.49, "sharpness", mana_cost=20)
swing_damage = MiscellaneousEnchantment("Greater sharpness", "increase strike damage when using sword-aspect skills.", mana_cost=20, per_activation=True)

# Creating runes
mana_capacitance_rune = Rune("Lesser Mana Capacitance Rune", enchantments=[mana_capacitance])
grand_arcane_resistance_rune = Rune("Grand Arcane Resistance Rune", enchantments=[resistance_enchantment])
enhanced_durability_rune = Rune("Enhanced Durability Rune", enchantments=[durability_enchantment])
greater_sharpness_rune = Rune("Greater Sharpness Rune", enchantments=[blade_sharpness,swing_damage])
grand_allStat_rune = Rune("Grand AllStat Rune", enchantments=[attribute_enchantment])

# Creating items
sword = Weapon("Sword", "A sharp weapon", material=force_oak, durability=80, hardness=10,
               manaSat=50, manaConvert=30, manaDissipate=5, slot="Hand", weight=5, sharpness=8,
               runes=[greater_sharpness_rune,enhanced_durability_rune])

grand_allstat_ring = Equipment("Grand AllStat Ring", "Boosts attributes", material=grand_arcane_atantum, slot="Ring", 
                durability=1800, hardness=100, manaSat=4100, manaConvert=100, manaDissipate=100, 
                runes=[mana_capacitance_rune, grand_allStat_rune])