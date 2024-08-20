""" Module that handles the character, or awakened """

from .base import Attribute
from .base import Resistance
from .base import VitalsStats
from .base import Vitals
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

class AwakenedResistances:
    """ The resistances for the awakened """

    def __init__(self):
        self.total_flat = Resistance.fill()
        self.total_percent = Resistance.fill()
        self.base_flat = Resistance.fill()
        self.accolade_flat = Resistance.fill()
        self.accolade_percent = Resistance.fill()
        self.misc_flat = Resistance.fill()
        self.misc_percent = Resistance.fill()

class AwakenedEquipment:
    """ The equipment the awakened has """
    def __init__(self):
        # Stuff like items and such

        self.head = None
        self.chest = None
        self.legs = None
        self.hands = None
        self.feet = None
        self.rings = None # limit = 10
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
    experience = 0,
    char_class = None,
    date = Moment("0936-06-03-12:00:00:000")
    ):
        self.name = name
        self.date = date
        self.level = level
        self.level_cap = level_cap if level_cap >= level else level
        self.experience = experience
        self.char_class = char_class

        self.attributes = AwakenedAttribs()
        self.attributes.base = attributes

        self.resistances = AwakenedResistances()

        self.vitals = VitalsStats(200, 100, 200, 100, 200, 100)
        self.curr_vitals = Vitals(200, 200, 200)

        self.accolades_percent = {
            "attribPercent": Attribute.fill(),
            "resistPercent": Attribute.fill()
        }

