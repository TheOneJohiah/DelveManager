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

class Vitals:
    """ Vitals values """
    def __init__(self,
        health,
        stamina,
        mana
        ):
        self.health = health
        self.stamina = stamina
        self.mana = mana

class VitalsStats:
    """ vital values """
    def __init__(self,
    health_max, health_regen,
    stamina_max, stamina_regen,
    mana_max, mana_regen
    ):
        self.health_max = health_max
        self.health_regen = health_regen
        self.stamina_max = stamina_max
        self.stamina_regen = stamina_regen
        self.mana_max = mana_max
        self.mana_regen = mana_regen

class Resistance:
    """ Collection of resistances """
    def __init__(self,
    heat, cold,
    light, dark, force,
    arcane, chemical, mental
    ):
        self.heat = heat
        self.cold = cold
        self.light = light
        self.dark = dark
        self.force = force
        self.arcane = arcane
        self.chemical = chemical
        self.mental = mental

    @classmethod
    def fill(cls, val=0):
        """ Create Attribute filled out with a single value """
        return Resistance(val, val, val, val, val, val, val, val)

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