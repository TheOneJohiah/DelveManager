""" The character class type for the game """

from .base import Attribute

class CharClass:
    """ Class for a character (awakened) """

    def __init__(self,
        name,
        rarity,
        notes,
        attribute_effect = Attribute.fill(),
        tree_effect = {},
        additional_effect = None):

        self.name = name
        self.rarity = rarity
        self.notes = notes
        self.attribute_effect = attribute_effect
        self.tree_effect = tree_effect
        self.additional_effect = additional_effect
