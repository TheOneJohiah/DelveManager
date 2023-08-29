class Overgrowth(DAura):
    def __init__(self):
        super().__init__()
        self.name = 'Overgrowth'
        self.tier = 4
        self.cost_scale = 1

        self.base_power = 7
        self.power_ratio = 1 / 200
        self.power_type = 'focus'

        self.base_cost = 30
        self.base_range = 1
        self.use_unit = 'min'
        self.resource = 'mana'
        self.cost_unit = 'mp/min'
