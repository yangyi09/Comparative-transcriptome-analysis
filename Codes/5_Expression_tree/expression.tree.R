.libPaths("C:/software/R/R-4.2.1/library")
library(phytools)

args <- commandArgs(trailingOnly = TRUE)

i1 = args[1]
o1 = args[2]
o2 = args[3]

data = read.csv(i1,row.names =1)
exp.matrix = log2(data+1)

#1-spearman
dist.matrix = as.dist(1-cor(exp.matrix, method = 'spearman'))
nj.tree = nj(dist.matrix)

#bootsrap
#boot.tree = boot.phylo(nj.tree, exp.matrix, FUN = function(x) nj(dist.matrix) ,B = 10000)
boot.tree = boot.phylo(nj.tree, t(exp.matrix), FUN = function(x) nj(as.dist(1-cor(t(x), method = 'spearman'))),B = 10000,trees=TRUE)
write.tree(boot.tree$trees,file=o1)

nj.tree$node.label = round((boot.tree$BP * 100) / 10000)
write.tree(nj.tree,file=o2)



#Euclidean distance
#eucl.matrix = dist(t(exp.matrix), method = 'euclidean')
#nj.eucl = nj(eucl.matrix)
#boot.tree = boot.phylo(nj.eucl, exp.matrix, FUN = function(x) nj(eucl.matrix) ,B = 1000)
#plot(nj.eucl)
#drawSupportOnEdges(boot.tree)
#write.tree(nj.eucl,file='vg.transcriptome.euclidean.nw')


#Random tree
#random_tree = rtree(19, rooted=FALSE,tip.label = c('Btre','Lbou','Ppup','Acal','Gfla','Nvit','Tele','Asoj','Ajap','Hheb','Lhet','Vvel','Pvin','Pven','Csol','Pqin','Aful','Cchi','Tdro'))

#Topology distance
#tree = read.tree('10000.boots.speciesAdd1.tre')
#dis.matrix = dist.topo(tree, method = "PH85")


###top50------>20
###top100----->20

#output distance matrix
#library(phangorn)
#writeDist(dis.matrix,file = 'boots.species.topoDis.phylip')
