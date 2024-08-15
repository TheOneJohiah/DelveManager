""" Module that handles the character, or awakened """

from .base import Attribute
from .time import Moment

class AwakenedAttribs:
    """ The attributes of the awakened """

    def __init__(self):
        self.effective = Attribute.fill()
        self.total = Attribute.fill()
        self.base = Attribute.fill()
        self.accolade = Attribute.fill()
        self.misc = Attribute.fill()
        self.sync = Attribute.fill()

class AwakenedEquipment:
    """ The equipment the awakened has """
    def __init__(self):
        # Stuff like items and such

        self.head = None
        self.chest = None
        self.legs = None
        self.hands = None
        self.feet = None
        self.rings = None
        self.amulet = None
        self.mainhand = None
        self.underwear = None
        self.overwear = None
        self.offhand = None

class Awakened:
    """ A singular character (awakened) for the thing """
    def __init__(self,
    name = "Idie Keigh",
    attributes = Attribute.fill(10),
    level = 0,
    level_cap=5,
    exp = 0,
    char_class = None,
    date = Moment("0936-06-03-12:00:00:000")
    ):
        self.name = name
        self.date = date
        self.level = level
        self.level_cap = level_cap if level_cap >= level else level
        self.exp = exp
        self.char_class = char_class

        self.attributes = AwakenedAttribs()
        self.attributes.base = attributes

        self.accolades_percent = {
            "attribPercent": Attribute.fill(),
            "resistPercent": Attribute.fill()
        }

