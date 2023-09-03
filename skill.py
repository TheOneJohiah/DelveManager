class Skill:
    def __init__(self, name, description, tier, tree):
        self.name = name
        self.description = description
        self.tier = tier
        self.tree = tree
        self.rank = 1  # Initial rank is 1
        self.cap = 10 # Starting cap for all skills is 10
        self.xp = 0 #starting xp for all skills is 0

    def getNextRankXP(self):
        return (.5*self.rank*(self.rank - 1) + 1) * 2**self.tier * 100

# Create specific skills
intrinsic_clarity = Skill("Intrinsic Clarity", "Multiply mana regen by 1+(RNK/5)", 0, "Magical Utility")
intrinsic_focus = Skill("Intrinsic Focus", "Multiply maximum mana by 1+(RNK/5)", 0, "Magical Utility")
# ... other skills ...