class Skill:
    def __init__(self, name, description, tier, tree,cost={'type':"",'value':0}):
        self.name = name
        self.description = description
        self.tier = tier
        self.tree = tree
        self.cost = cost
        self.rank = 1  # Initial rank is 1
        self.cap = 10 # Starting cap for all skills is 10
        self.xp = 0 #starting xp for all skills is 0

    def getNextRankXP(self):
        return (.5*self.rank*(self.rank - 1) + 1) * 2**self.tier * 100
    
    def add_exp (self, xp):
        currXP = self.xp + xp
        nextXP = self.getNextRankXP()

        if currXP >= nextXP:
            while currXP >= nextXP:
                currXP -= nextXP
                self.rank +=1
                print(self.name+" Leveled up!")
                nextXP = self.getNextRankXP()

        self.xp = currXP

# Create specific skills
intrinsic_clarity = Skill("Intrinsic Clarity", "Multiply mana regen by 1+(RNK/5)", 0, "Magical Utility")
intrinsic_focus = Skill("Intrinsic Focus", "Multiply maximum mana by 1+(RNK/5)", 0, "Magical Utility")
# ... other skills ...