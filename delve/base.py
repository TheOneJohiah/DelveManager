""" Various base classes used in other places """

class Attribute:
    """ Character stat attributes """
    def __init__(self,
    strength, recovery,
    endurance, vigor, focus,
    clarity, perception, speed
    ):
        # str rcv end vgr fcs clr per spd
        self.strength = strength
        self.recovery = recovery
        self.endurance = endurance
        self.vigor = vigor
        self.focus = focus
        self.clarity = clarity
        self.perception = perception
        self.speed = speed

    @classmethod
    def fill(cls, val=0):
        """ Create Attribute filled out with a single value """
        return Attribute(val, val, val, val, val, val, val, val)

    def __iter__(self):
        return iter([self.strength,
            self.recovery,
            self.endurance,
            self.vigor,
            self.focus,
            self.clarity,
            self.perception,
            self.speed])

# TODO: name these variables according to
# what they actually mean in delve
class Vitals:
    """ Character/enemy? vital values """
    def __init__(self,
    health, health2,
    health3, health4,
    health5, health6
    ):
        self.health = health
        self.health2 = health2
        self.health3 = health3
        self.health4 = health4
        self.health5 = health5
        self.health6 = health6

class Item:
    """ Any kind of item """
    def __init__(self, name="Thing", description="A thing!"):
        self.name = name
        self.description = description
        self.type = None
        self.rarity = None

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