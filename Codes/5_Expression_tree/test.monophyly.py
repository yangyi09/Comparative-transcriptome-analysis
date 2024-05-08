from ete3 import Tree
import os
import re
import itertools


def test_monophyly(treefile,groups):
	a = open(treefile).read()
	a = a.strip().replace('-','')
	a = re.sub(':\d+.\d+','',a)
	t = Tree(a)
	return (str(t.check_monophyly(values=groups, target_attr="name")[0]))

all_species = ['Asoj','Pvin','Tdro','Lbou','Lhet']
def get_subset(my_list):
	all_sublist = []
	n = len(my_list)
	for num in range(n) :
		for i in itertools.combinations(my_list,num+1):
			if len(i) > 1 :
				all_sublist.append(i)
	return (all_sublist)


for group in get_subset(all_species) :
	w = open('.'.join(group) + '.monophyly.out','w')
	for file in os.listdir('./gene_tree') :
		if file.endswith('.tre') :
			print (file + '\t' + test_monophyly('./gene_tree/' + file, group),file=w)

