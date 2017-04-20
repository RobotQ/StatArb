# import some data from tushare
import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd

res = []
years = range(2006, 2017)
for year in years:
    res.append(ts.shibor_data(year))

df = pd.concat(res)
plt.plot(df["date"], df["1W"])

