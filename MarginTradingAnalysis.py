# import some data from tushare
import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd


def get_shibor_data(startYear, endYear):
    res = []
    for year in range(startYear, endYear):
        res.append(ts.shibor_data(year))
    df = pd.concat(res)
    return df


test = get_shibor_data(2006, 2017)
plt.plot(test["date"], test["1W"])
