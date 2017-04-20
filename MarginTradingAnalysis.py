# import some data from tushare
import tushare as ts
import matplotlib.pyplot as plt

df = ts.shibor_data(2017)
plt.plot(df["ON"])

