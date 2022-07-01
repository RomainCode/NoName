

class Upgrade:

    PPS_PERCENT_ALL = 0
    PPS_PERCENT_SPECIFIC = 1
    LOWER_PRICE_ALL = 2
    LOWER_PRICE_SPECIFIC = 3
    INCREASE_DAMAGE_PERCENT = 4



    def __init__(self, type, amount, infos):
        self.type = type
        self.amount = amount
        self.infos = infos

    
    def applay(slef):
        pass


class UpgradableItem:

    def __init__(self):
        self.level = 0
        self.init_cost = 0
        self.cost_multiplier = 1.2
    
    def getNextCost(self):
        return self.init_cost*self.cost_multiplier**(self.level+1)
    
    def getCostOfNNext(self, n):
        return (self.cost_multiplier**n - 1)/(self.cost_multiplier-1)


class GeneratorItem(UpgradableItem):

    def __init__(self):
        super().__init__()
        self.PPS = 0
        self.init_gain = 1
        self.gain_multiplier = 1.05
    
    def getNextGain(self):
        return self.PPS*self.gain_multiplier**(self.level+1)
    
    def getGainOfNNext(self, n):
        return (self.gain_multiplier**n - 1)/(self.gain_multiplier-1)
