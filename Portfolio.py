
import numpy as np
import scipy

class Portfolio:
    def __init__ (self, markets,covariance_matrix:np.array):
        self.markets = markets
        self.w= np.array([1/len(markets) for market in markets])
        self.covariance_matrix = covariance_matrix
        returns = [market.getValue() for market in markets]
        self.R = np.array(returns)

    
    def Optimize(self,mu):
        #with scipi optimize, find the minimum variance portfolio
        #TODO: min wT times covariance matrix times w, such that Rt times w = mu, and sum(w) = 1, and all market values are positive
        x = self.w
        fun = lambda x: x.T @ self.covariance_matrix @ x 
        cons = ({'type': 'eq', 'fun': lambda x:  self.R.T @ (x) - mu},
                {'type': 'eq', 'fun': lambda x: sum(x) - 1})
        ret = scipy.optimize.minimize(fun, self.w, constraints=cons)
        self.w = ret.x
        return ret

    def getValue(self):
        value = self.w.T.dot(self.R)
        return value
    
    def getVariance(self):
        var = self.w.T.dot(self.covariance_matrix).dot(self.w)
        return var
        