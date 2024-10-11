from Market import Market
from Portfolio import Portfolio
from Probability import Beta_Distribution
import requests as r
import numpy as np

def getMarketPrice(id, yes = True):
    req = r.get("https://gamma-api.polymarket.com/markets/"+str(id))
    ret = None
    if yes:
        ret = float(req.json()["outcomePrices"][1:-1].replace('"','').split(",")[0])
    else:
        ret = float(req.json()["outcomePrices"][1:-1].replace('"','').split(",")[1])
    return ret


distribution1 = Beta_Distribution(0.3, 0.5, 1)
caliBill = Market("Will Cali Pass bill-YES",505867, distribution1, getMarketPrice("505867"), 0,0)
caliBillNo = Market("Will Cali Pass bill-NO",505867, distribution1.inverse(), getMarketPrice("505867",False), 0,0)


portfolio1 = Portfolio([caliBill,caliBillNo], np.array([[1,-1],[-1,1]]))

portfolio1.Optimize(0.8)
print(portfolio1.markets, portfolio1.w, portfolio1.getValue(), portfolio1.getVariance())


