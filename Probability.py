

'''
Our main kind of distribution is the Beta distribution.
'''
import numpy as np


class Beta_Distribution:
    def __init__(self, a, b, c, *, lamb=4):
        self.a = a
        self.b = b
        self.c = c
        self.lamb = lamb
        self.r = self.c - self.a

        self.alpha = 1 + self.lamb * (self.b - self.a) / self.r
        self.beta = 1 + self.lamb * (self.c - self.b) / self.r
    
    def inverse(self):
        return Beta_Distribution(1-self.a, 1-self.b, 1-self.c, lamb=self.lamb)
    
    def getExpectedValue(self):
        ret = self.alpha / (self.alpha + self.beta)
        return (ret)

    def sample(self, size = 1):
        return self.a + np.random.beta(self.alpha, self.beta, size=size) * self.r