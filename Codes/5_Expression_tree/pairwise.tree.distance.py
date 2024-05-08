#!/usr/bin/python

#from itertools import pairwise

s = ['Btre','Lbou','Ppup','Acal','Gfla','Nvit','Tele','Asoj','Ajap','Hheb','Lhet','Vvel','Pvin','Pven','Csol','Pqin','Aful','Cchi','Tdro']

pairs = []
for i in range(0,len(s)):
	for j in range(i+1,len(s)):
		pairs.append([s[i],s[j]])

from ete3 import Tree

t_s = Tree('SpeciesTree_rooted.txt')
t_t = Tree('nj.VG.Sperman.nw')

a = []
for pair in pairs :
	d_s = t_s.get_distance(pair[0],pair[1])
	d_t = t_t.get_distance(pair[0],pair[1])
	a.append(['-'.join(pair),d_s,d_t])

import pandas as pd

data = pd.DataFrame(a,columns=['Pairs','D_S','D_T'])


import mantel
cor = mantel.test(data['D_S'], data['D_T'])
print (cor)

print (data)
#lm plot
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['svg.fonttype'] = 'none'
g = sns.lmplot(
    data=data,
    x="D_S", y="D_T",
    palette= '#DE817A'
)
plt.show()