from Probability import Beta_Distribution
import numpy as np

class state:
    outcomes: np.array
    def __init__(self, name, prob:Beta_Distribution, value):
        self.name = name
        self.prob = prob
        self.value = value
        self.sd = 0
    
    def __str__(self) -> str:
        return self.name
    def __repr__(self) -> str:
        return self.name
    
    '''
    take n samples from our probability prior, and then run 1 single bernoulli trials at each respective probability.
    1 is democrat win. 0 is republican win.
    Montecarlo simulation of election outcomes outputed as an array, then saved. 
    '''
    def getSample(self, size = 1):
        sample = self.prob.sample(size = size)
        self.outcomes = np.random.Generator.binomial(1,sample,size = size)
        return self.outcomes

    '''
    gets electoral value importance of the state
    '''
    def getValue(self):
        return self.value

#were going to treat 1 as Kamala win 0 as Trump win
class USA:
    results: np.array
    '''initialization of the USA object'''
    def __init__(self, states):
        self.states = states
    ''' Simplified way to load all states at once'''
    def __init__(self,state_names,state_probs,state_values):
        self.states = np.array([state(state_names[i],state_probs[i],state_values[i]) for i in range(len(state_names))])
        self.Simulate()

    '''helper function to get n sampled outcomes from each state'''
    def getSample(self, size = 1):
        return np.array([state.getSample(size = size) for state in self.states])
    
    '''helper function to get EC values of each state in array'''
    def getValues(self):
        return np.array([state.getValue() for state in self.states])
    
    '''Samples from each state, then multiplies by the electoral value of each state.
    outpus and saves result is a large numpy matrix with a single row, and n columns of electoral votes'''
    def Simulate(self):
        votes = self.getSamples(1000)
        electoral_votes = self.getValues()
        self.results = votes @ electoral_votes
        return self.results

    def KamilaWinProbability(self):
        return (self.results > 270).mean()
    
    def KamilaWinVariance(self):
        results = self.results()
        results.var()

class priorGenerator:
    '''
    turns polls into a beta prior for expected results
    '''
    def __init__(self, polls):
        self.polls = polls
        self.a = sum(polls)
        self.b = len(polls) - self.a
        self.prior = Beta_Distribution(self.a,self.b,1)
    
