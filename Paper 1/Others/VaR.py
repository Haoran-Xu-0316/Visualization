import math
from datetime import datetime

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as sci
import scipy.optimize as sco
import seaborn as sns
import tushare as ts

#全局设置-----------------------------------------------------------------------------------------------------------------
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['Palatino Linotype']
# plt.rcParams["font.weight"] = "bold"
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 1
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

l=['CSI 300 - Gold','CSI 300 - WTI','CSI 300 - Bitcoin','CSI 300 - Bond','Gold - WTI','Gold - Bitcoin','Gold - Bond','WTI - Bitcoin','WTI - Bond','Bitcoin - Bond']

Bond=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\VaR.xlsx', sheet_name='Bond',index_col=0,parse_dates=[0])
Oil=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\VaR.xlsx', sheet_name='Oil',index_col=0,parse_dates=[0])
BTC=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\VaR.xlsx', sheet_name='BTC',index_col=0,parse_dates=[0])
Gold=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\VaR.xlsx', sheet_name='Gold',index_col=0,parse_dates=[0])

HA=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data\Hedging Assets\hedging assets.xlsx', sheet_name='All-log',index_col=0,parse_dates=[0])
C=['#FFDDB7','#9C3434','#B0B1B4','#E3A085','#334666']

#
plt.subplots(figsize=(12,8))
#
plt.subplot(221)

plt.plot(Bond.iloc[:, 24],label='EMV',color=C[0])
plt.plot(Bond.iloc[:, 26],label='GPR',color=C[1])
plt.plot(Bond.iloc[:, 27],label='CPU',color=C[2])
plt.plot(Bond.iloc[:, 25],label='EPU',color=C[3])
plt.plot(Bond.iloc[:, 23],label='TPU',color=C[4])
sl=plt.legend(labels=['Bond'],frameon=False,loc='upper left',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='upper right',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-03-27'))
# plt.axhline(y=WTI,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
# # plt.yticks(np.arange(-0.45,0.20,0.10))
#
plt.subplot(222)
plt.plot(Gold.iloc[:, 24],label='EMV',color=C[0])
plt.plot(Gold.iloc[:, 26],label='GPR',color=C[1])
plt.plot(Gold.iloc[:, 27],label='CPU',color=C[2])
plt.plot(Gold.iloc[:, 25],label='EPU',color=C[3])
plt.plot(Gold.iloc[:, 23],label='TPU',color=C[4])
sl=plt.legend(labels=['Gold'],frameon=False,loc='upper left',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='upper right',labelspacing=0.15)
plt.gca().add_artist(sl)
plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-03-27'))
# plt.axhline(y=BTC,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
#
plt.subplot(223)
plt.plot(Oil.iloc[:, 24],label='EMV',color=C[0])
plt.plot(Oil.iloc[:, 26],label='GPR',color=C[1])
plt.plot(Oil.iloc[:, 27],label='CPU',color=C[2])
plt.plot(Oil.iloc[:, 25],label='EPU',color=C[3])
plt.plot(Oil.iloc[:, 23],label='TPU',color=C[4])
plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-03-27'))
sl=plt.legend(labels=['Oil'],frameon=False,loc='upper left',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='upper right',labelspacing=0.15)
plt.gca().add_artist(sl)

#23/29/35

# plt.axes([0.1, 0.19, 0.22, 0.2])
# plt.plot(Oil.iloc[:, 29],label='TPU')
# plt.plot(Oil.iloc[:, 30],label='EMV')
# plt.plot(Oil.iloc[:, 31],label='EPU')
# plt.plot(Oil.iloc[:, 32],label='GPR')
# plt.plot(Oil.iloc[:, 33],label='CPU')
# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-03-27'))
# plt.tick_params(labelsize=6)     #调整坐标轴数字大小
# plt.legend()                 #plt.legend( prop = {'size':17})   图例字体大小
# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-04-03'))
# plt.axhline(y=Bond,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.20, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
C=['#FFDDB7','#9C3434','#B0B1B4','#E3A085','#334666']

plt.subplot(224)
plt.plot(BTC.iloc[:, 24],label='EMV',color=C[0])
plt.plot(BTC.iloc[:, 26],label='GPR',color=C[1])
plt.plot(BTC.iloc[:, 27],label='CPU',color=C[2])
plt.plot(BTC.iloc[:, 25],label='EPU',color=C[3])
plt.plot(BTC.iloc[:, 23],label='TPU',color=C[4])
plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-03-27'))
sl=plt.legend(labels=['Bitcoin'],frameon=False,loc='upper left',handlelength=0,prop={'style':'italic','weight':'bold'})
plt.legend(frameon=False,loc='upper right',labelspacing=0.15)
plt.gca().add_artist(sl)
# plt.xlim(pd.Timestamp('2013-11-08'), pd.Timestamp('2023-04-03'))
# plt.axhline(y=Gold,color='black',linestyle='--')
# plt.axhline(y=0,color='black',linestyle='-',linewidth=2)
# plt.text(0.5,0.5,'hh')
# plt.fill_between(pd.date_range(start='2019-06', end='2020-09', freq='M'), -0.45,0.30, color='#B3D0AB', alpha=0.4, linewidth=0)
# plt.margins(x=0,y=0)
#
#
#
plt.tight_layout()
#


plt.savefig(r'C:/Users/徐浩然/Desktop/VaR.png',dpi=800)

print(Bond.iloc[:, 23])
plt.show()
