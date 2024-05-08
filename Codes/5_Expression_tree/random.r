library(ape)
r.tre = rtree(19,rooted = FALSE,tip.label =c('Btre','Lbou','Ppup','Acal','Gfla','Nvit','Tele','Asoj','Ajap','Hheb','Lhet','Vvel','Pvin','Pven','Csol','Pqin','Aful','Cchi','Tdro'))
write.tree(r.tre,file = 'tmp.tre')
