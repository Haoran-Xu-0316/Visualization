import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-ticks')
# dataframe全显示
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

c1list=[(16/255,70/255,128/255),(49/255,124/255,183/255),(109/255,173/255,209/255),(182/255,215/255,232/255),(233/255,241/255,244/255),(251/255,227/255,213/255),(246/255,178/255,147/255),(220/255,109/255,87/255),(183/255,34/255,48/255),(109/255,1/255,31/255)]
c2list=[(40/255,86/255,119/255),(177/255,193/255,204/255),(214/255,156/255,147/255),(229/255,207/255,194/255),(141/255,164/255,147/255)]
c3list=[(40/255,86/255,119/255),(177/255,193/255,204/255),(214/255,156/255,147/255),(229/255,207/255,194/255),(141/255,164/255,147/255),(59/255,72/255,47/255)]

C1 = LinearSegmentedColormap.from_list('Blues',c1list,N=256)
C2 = LinearSegmentedColormap.from_list('Blues',c2list,N=256)
C3 = LinearSegmentedColormap.from_list('Blues',c3list,N=256)
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.get_cmap('Blues')
outer_colors = cmap([120,175,200])
inner_colors = cmap([10, 20, 50, 60, 90, 100])

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))
plt.tight_layout()
plt.savefig(r'C:/Users/徐浩然/Desktop/美赛Figure_Template\6.png',dpi=400)

plt.show()