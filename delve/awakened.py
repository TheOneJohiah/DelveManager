""" Module that handles the character, or awakened """

from .base import Attribute

class Awakened:
    """ A singular character (awakened) for the thing """
    def __init__(self,
    name = "Idie Keigh",
    attributes = Attribute.fill(10),
    level = 0,
    level_cap=5,
    exp = 0,
    char_class = None,
    date = None
    ):

        self.name = name
        self.level = level
        self.level_cap = level_cap if level_cap >= level else level
        self.exp = exp
        self.char_class = char_class

        # Character stat attributes
        self.attributes = {
            # str rcv end vgr fcs clr per spd
            "effec": Attribute.fill(),
            "total": Attribute.fill(),
            "base": attributes,
            "acco": Attribute.fill(),
            "misc": Attribute.fill(),
            "sync": Attribute.fill(),
        }

        self.accolades_percent = {
            "attribPercent": Attribute.fill(),
            "resistPercent": Attribute.fill()
        }

        # Stuff like items and such
        self.wearables = {
            "Head" : None,
            "Chest" : None,
            "Legs" : None,
            "Hands" : None,
            "Feet" : None,
            "Ring[0]" : None,
            "Ring[1]" : None,
            "Ring[2]" : None,
            "Ring[3]" : None,
            "Ring[4]" : None,
            "Ring[5]" : None,
            "Ring[6]" : None,
            "Ring[7]" : None,
            "Ring[8]" : None,
            "Ring[9]" : None,
            "Amulet" : None,
            "Mainhand" : None,
            "Underwear" : None,
            "Overwear" : None,
            "Offhand" : None
        }
