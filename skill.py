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

# specific skills
intrinsic_clarity = Skill("Intrinsic Clarity",
                          "Multiply mana regen by 1+(RNK/5)",
                          0,"Magical Utility")
intrinsic_focus = Skill("Intrinsic Focus",
                        "Multiply maximum mana by 1+(RNK/5)",
                        0, "Magical Utility")

healing_word = Skill("Healing Word",
                     "Invoke a word of healing to restore health to a touched entity <br> Heal [10-20]*[RNK]*[1 + .005*FCS] hp <br> Cost: 10mp <br> Cannot Heal Self",
                     0,"Restoration",cost={'type':"MP",'value':10})

natural_intuition = Skill("Natural Intuition",
                          "Develop an intuitive understanding of the mechanics of fibres and polymers <br> Higher ranks mean greater insight",
                          0,"Natureworking")

chemical_intuition = Skill("Chemical Intuition",
                           "Develop an intuitive understanding of the mechanics of compounds <br> Higher ranks mean greater insight",
                           0,"Chemistry")

cleave_fibers = Skill("Cleave Fibers", "Manipulate the bonds between fibers, binding them together or cutting them apart. <br> Alter volume of [RNK^2] cm<sup>3</sup> <br> Cost: 5*RNK mp",0,"Natureworking")
stamina_transfer = Skill("Stamina Transfer","Sacrifice a portion of your stamina to energize a touched entity <br> Gives: [20*RNK] sp <br> Cost: [40*RNK] sp",0,"Restoration")
purge_poison = Skill("Purge Poison","Weaken and destroy poisons and toxins (fcs) <br> Reduce poison damage by  [20*RNK*(1 + .01*FCS)] <br> Range: Touch<br> Cost: 20mp <br> If damage is reduced to 0, the condition is ended",1,"Restoration")
healers_synergy = Skill("Healers Synergy","Multiply intensity of healing skills by [1+0.002*RNK*restoration_ranks] <br> Requires 50 ranks in Restoration",2,"Restoration")
tissue_scan = Skill("Tissue Scan","Scan the body of a touched entity. <br> Resolution of resulting scan is equal to: [200 + 20*RNK] % of mundane optical vision <br> Cost: 5mp",2,"Restoration")