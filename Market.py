class Market:
    def __init__(self, name, id, probability, mkt_value, t_end,r):
        self.probability = probability
        self.t_end = t_end
        self.name = name
        self.id = id
        self.mkt_value = mkt_value
        self.r = r
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name

    
    def getValue(self):
        value = (self.probability.getExpectedValue()-self.mkt_value)/(self.mkt_value*(1+self.r)**self.get_t())
        return value
    
    def getVariance(self):
        var = (1/(self.mkt_value*(1+self.r)**self.get_t)**2)*(self.probability.getExpectedValue()-self.probability.getExpectedValue()**2)
        return var
    
    def get_t(self):
        #TODO: calculate remaining time to maturity
        return 0