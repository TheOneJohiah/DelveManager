class Material:
    def __init__(self, name):
        self.name = name

class Enchantment:
    def __init__(self, name, description, mana_cost=0, per_activation=False):
        self.name = name
        self.description = description
        self.mana_cost = mana_cost
        self.per_activation = per_activation

    def spend_mana(self, mana_cost, per_activation):
        if per_activation == False:
            return mana_cost
        return True
    
    def describe(self):
        attributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        descr = "<ul>" #initialize description
        for attr in attributes:
            descr += "<li>"+attr+": "+str(getattr(self, attr))+"</li>"
        return descr+"</ul>"

class ResistanceEnchantment(Enchantment):
    def __init__(self, name, description, resistance_buff, mana_cost):
        super().__init__(name, description, mana_cost)
        # array [], location 0 through 7, heat/cold/light/dark/force/arcane/chemical/mental
        self.resistance_buff = resistance_buff

class AttributeEnchantment(Enchantment):
    def __init__(self, name, description, attribute_buff, mana_cost):
        super().__init__(name, description, mana_cost)
        # array [], 0 through 5, str/rec/end/vig/foc/cha
        self.attribute_buff = attribute_buff

#Durability, hardness, sharpness, weight % increase
class ItemStatEnchantment(Enchantment):
    def __init__(self, name, description, percent_buff, buff_type, mana_cost):
        super().__init__(name, description, mana_cost)
        self.percent_buff = percent_buff
        self.buff_type = buff_type

class MiscellaneousEnchantment(Enchantment):
    def __init__(self, name, description, mana_cost, abstract_effect=None, skill_bonus=None, per_activation=False):
        super().__init__(name, description, mana_cost, per_activation)
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
    def __init__(self, name, active=False, enchantments=None, slot_requirement="Any"):
        self.name = name
        self.active = active
        self.enchantments = enchantments if enchantments is not None else []
        self.slot_requirement = slot_requirement

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def deplete_charge(self, enchantments, deplete):
        ##Todo: if item has Capacitance rune, then deplete charge from it.
        ##depletion amount for time passing on passive runes calculated outside this function
        ##if mana below 0, rune deactivates.
        return True
    
    def describe(self):
        attributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        descr = "<ul>" #initialize description
        for attr in attributes:
            descr += "<li>"+attr+": "+str(getattr(self, attr))+"</li>"
        return descr+"</ul>"

class Item:
    def __init__(self, name, description, material, durability, hardness, manaSat, manaConvert, manaDissipate, enchantments=None):
        self.name = name
        self.description = description
        self.material = material
        self.enchantments = enchantments if enchantments is not None else []
        self.durability = durability
        self.hardness = hardness
        self.manaSat = manaSat
        self.manaConvert = manaConvert
        self.manaDissipate = manaDissipate

    def describe(self):
        attributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        descr = "<ul>" #initialize description
        for attr in attributes:
            descr += "<li>"+attr+": "+str(getattr(self, attr))+"</li>"
        return descr+"</ul>"
    
class Equipment(Item):
    def __init__(self, name, description, material, slot, durability, hardness, manaSat, manaConvert, manaDissipate, enchantments=None):
        super().__init__(name, description, material, durability, hardness, manaSat, manaConvert, manaDissipate, enchantments)
        self.slot = slot

class Weapon(Equipment):
    def __init__(self, name, description, material, durability, hardness, manaSat, manaConvert, manaDissipate, slot, weight, sharpness, enchantments=None):
        super().__init__(name, description, material, slot, durability, hardness, manaSat, manaConvert, manaDissipate, enchantments) #Keep track of order!!
        self.weight = weight
        self.sharpness = sharpness

# Creating materials
force_oak = Material("Force Oak")
force_steel = Material("Force Steel")
heat_copper = Material("Heat Copper")
dark_steel = Material("Dark Steel")

# Creating enchantments
resistance_enchantment = ResistanceEnchantment("Grand Arcane Resistance", "Provides resistances", resistance_buff=[0, 0, 0, 0, 0, 5000, 0, 0], mana_cost=100)
attribute_enchantment = AttributeEnchantment("Grand Strength", "Boosts attributes", attribute_buff=[100, 0, 0, 0, 0, 0], mana_cost=100)
mana_capacitance = ManaCapacitanceEnchantment("Lesser Mana Capacitance", "Stores mana", 10000, 0.7, 0.1, 1)
##Placeholder enchantment type variable. Replace with dict? Array?
durability_enchantment = ItemStatEnchantment("Enhanced Durability", "Boosts item durability cap", 10, "durability", mana_cost=20)
blade_sharpness = ItemStatEnchantment("Greater sharpness", "increase to sharpness", 0.49, "sharpness", mana_cost=20)
swing_damage = MiscellaneousEnchantment("Greater sharpness", "increase strike damage when using sword-aspect skills.", mana_cost=20, per_activation=True)

# Creating runes
mana_capacitance_rune = Rune("Lesser Mana Capacitance Rune", enchantments=[mana_capacitance])
grand_arcane_resistance_rune = Rune("Grand Arcane Resistance Rune", "Provides resistances", enchantments=[resistance_enchantment])
enhanced_durability_rune = Rune("Enhanced Durability Rune", enchantments=[durability_enchantment])
greater_sharpness_rune = Rune("Greater Sharpness Rune", enchantments=[blade_sharpness,swing_damage])

# Creating items
sword = Weapon("Sword", "A sharp weapon", material=force_oak, durability=80, hardness=10,
               manaSat=50, manaConvert=30, manaDissipate=5, slot="Hand", weight=5, sharpness=8,
               enchantments=[greater_sharpness_rune,enhanced_durability_rune])