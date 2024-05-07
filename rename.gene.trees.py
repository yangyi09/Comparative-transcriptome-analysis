#!/usr/bin/python

import os
from ete3 import Tree





def rename(file) :
	t = Tree('./Gene_Trees/' + file)
	for node in t.traverse("postorder"):
		if node.is_leaf():
			node.name = node.name[1:]
	t.write(format=1,outfile='./Gene_Trees_rename/' + file)

for file in os.listdir('./Gene_Trees') :
	if file.endswith('.txt') :
		rename(file)