""" Module that handles the character, or awakened """

class Awakened:
    """ A singular character (awakened) for the thing """
    def __init__(self,
    name = "Idie Keigh",
    attributes = [10] * 8,
    level = 0,
    level_cap=5,
    exp = 0,
    c_class = None,
    date = None
    ):

        self.name = name

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
