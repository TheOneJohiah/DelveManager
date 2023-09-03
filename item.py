class Enchantment:
    def __init__(self, name, description, mana_cost, slot_requirement, 
                 resistance_buff=None, attribute_buff=None,
                 abstract_effect=None, skill_bonus=None, 
                 mana_storage=False, mana_input_efficiency=100, 
                 mana_output_efficiency=100, binding_strength="None"):
        self.name = name
        self.description = description
        self.mana_cost = mana_cost
        self.slot_requirement = slot_requirement
        self.resistance_buff = resistance_buff if resistance_buff is not None else {}
        self.attribute_buff = attribute_buff if attribute_buff is not None else [0, 0, 0, 0, 0, 0]
        self.abstract_effect = abstract_effect  # You can define this as needed
        self.skill_bonus = skill_bonus  # You can define this as needed
        self.mana_storage = mana_storage
        self.mana_input_efficiency = mana_input_efficiency
        self.mana_output_efficiency = mana_output_efficiency
        self.binding_strength = binding_strength



class Item:
    def __init__(self, name, description, enchantments=None):
        self.name = name
        self.description = description
        self.enchantments = enchantments if enchantments is not None else []


class Equipment(Item):
    def __init__(self, name, description, durability, hardness, slot, enchantments=None):
        super().__init__(name, description, enchantments)
        self.durability = durability
        self.hardness = hardness
        self.slot = slot


class Weapon(Equipment):
    def __init__(self, name, description, durability, hardness, slot, weight, sharpness, enchantments=None):
        super().__init__(name, description, durability, hardness, slot, enchantments)
        self.weight = weight
        self.sharpness = sharpness



# Creating enchantments
hardness_enchantment = Enchantment("Hardness", "Increases item hardness", mana_cost=10, slot_requirement="Any")
durability_enchantment = Enchantment("Durability", "Increases item durability", mana_cost=15, slot_requirement="Any")
resistance_enchantment = Enchantment("Resistance", "Provides resistance to damage", mana_cost=20, slot_requirement="Chest",
                                        resistance_buff={"Fire": 10, "Ice": 5})
# ... Define more enchantments as needed

# Creating an item with enchantments, attributes, and endurances
attributes = [10, 5, 8, 7, 12, 15]  # Example values for attributes
endurances = [20, 15, 10, 5, 18, 25, 8, 14]  # Example values for endurances
enchanted_item = Equipment("Enchanted Armor", "An armor with enchantments", durability=100, hardness=8, slot="Chest",
                            attributes=attributes, endurance=endurances, enchantments=[hardness_enchantment, durability_enchantment])

# Accessing attributes and endurances of an item
print(f"Attributes: {enchanted_item.attributes}")
print(f"Endurances: {enchanted_item.endurance}")