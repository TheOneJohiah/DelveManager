class Monster:
    def __init__(self, name, description, tier, level, tamed):
        self.name = name
        self.description = description
        self.tier = tier
        self.level = level
        self.tamed = tamed
        self.reward_exp = 25*tier*level

slime = Monster('Slime','Goopy Goober',1,5,False)