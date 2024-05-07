#!/usr/bin/python

from ete3 import Tree
from Bio import SeqIO
import os
import pandas as pd

def best1(og) :
	t = Tree('./Gene_Trees_rename/%s_tree.txt' %og)
	all_nodes = []
	for node in t.traverse("postorder"):
		if node.is_leaf():
			if node.name.split('|')[0] == 'Tdro' :
				all_nodes.append(node.name)
	adict = {}
	for node in all_nodes :
		dismat = []
		for n in t.traverse("postorder"):
			if n.is_leaf():
				if n.name.split('|')[0] == 'Tdro' :
					pass
				else :
					dismat.append(t.get_distance(t&node,n))
		adict[node] = min(dismat)
	return (min(adict,key=adict.get))


for og in open('Tdro.MC.OtherSC.list','r') :
	og = og.strip()
	Tdro_name = best1(og)
	genes = []
	seqindex =  SeqIO.index('./Orthogroup_Sequences/' + og + '.fa','fasta')
	for key in list(seqindex.keys()) :
		if key.split('|')[0] == 'Tdro' :
			pass
		else :
			genes.append(key)
	genes.append(Tdro_name)
	w = open('./Single_Copy_Orthologue_Sequences_TdroBest/%s.fa' %og,'a')
	for gene in genes :
		w.write('>%s\n%s\n' %(gene,str(seqindex[gene].seq)))
	w.close() 