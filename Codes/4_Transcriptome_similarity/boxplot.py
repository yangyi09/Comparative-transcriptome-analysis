import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

plt.rcParams['svg.fonttype'] = 'none'
data = pd.read_excel('Spearman.correation.draw.xlsx',header=0)
print (data)


plt.figure (figsize = (6,3))
sns.set_theme(style="white")
sns.boxplot(x="Species", y="R",
            hue="Group", palette=["#00BFC4","#F8766D"],
            data=data)

#plt.show()
plt.savefig('Pairwise.Similarity.svg',format='svg')


for s in list(set(data['Species'].tolist())) :
	a = data[ (data['Species']==s) & (data['Group']=='Dros')]['R'].tolist()
	b = data[ (data['Species']==s) & (data['Group']=='non-Dros')]['R'].tolist()
	print (s,stats.mannwhitneyu(a,b))