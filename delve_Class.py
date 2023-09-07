class delve_Class:
    def __init__(self, name, rarity, notes, attribute_effect, tree_effect, additional_effect):
        self.name = name
        self.rarity = rarity
        self.notes = notes
        self.attribute_effect = attribute_effect  # Now an array [str, rec, end, vig, foc, cla]
        self.tree_effect = tree_effect
        self.additional_effect = additional_effect
        
    def meets_requirements(self, awakened):
        ##Todo: Reimplement these requirements in a better way
        return True
    
unclassed = delve_Class("Unclassed", "Common", "Everyone's first class", attribute_effect=[1, 1, 1, 1, 1, 1], tree_effect={}, additional_effect=None)

worker = delve_Class("Worker", "Common", "Warning: Experience may no longer be gained through combat", attribute_effect=[1, 1, 1, 1, 1, 1], tree_effect={}, additional_effect="50% boost to non-combat skills")

# Create specific classes
dynamo = delve_Class("Dynamo", "Rare", "Master of energy manipulation", attribute_effect=[1, 1, 1, 1, 1, 3], tree_effect={}, additional_effect=None)

shieldwielding_defender = delve_Class("Shieldwielding Defender", "Uncommon", "Master of defense with a shield", attribute_effect=[1, 1, 1.5, 1, 1, 1], tree_effect={"Shieldwielding": 3}, additional_effect=None)

geomancer = delve_Class("Geomancer", "Uncommon", "A dirty dude", attribute_effect=[1,1,1,1,1.5,1], tree_effect={"Geoevocation": 3}, additional_effect=None)

life_worker = delve_Class("Life Worker","Rare","Worker specializing in all sorts of organics",[1] * 6,{"Restoration":2,"Natureworking":2,"Chemistry":2},None)