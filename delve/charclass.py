""" The character class type for the game """

class CharClass:
    """ Class for a character (awakened) """

    def __init__(self,
        name,
        rarity,
        notes,
        attribute_effect = [0, 0, 0, 0, 0, 0, 0, 0],
        tree_effect = {},
        additional_effect = None):

        self.name = name
        self.rarity = rarity
        self.notes = notes
        self.attribute_effect = attribute_effect  # Now an array [str, rec, end, vig, foc, cla]
        self.tree_effect = tree_effect
        self.additional_effect = additional_effect
