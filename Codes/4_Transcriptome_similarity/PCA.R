.libPaths("C:/software/R/R-4.2.1/library")
library(PCAtools)

ematrix = read.csv($ematrix,header=1,row.names='OG')
ematrix = log2(ematrix+1)
head(ematrix)
metadata = read.csv('metadata.csv',header=1,row.names = 1)
p <- pca(ematrix, metadata = metadata, removeVar = 0.1)

biplot(p,
colby = 'host_species',
gridlines.major = FALSE, gridlines.minor = FALSE,
shape = 'clade',legendPosition = 'right')

eigencorplot(p,
    components = getComponents(p, 1:5),
    metavars = c('host_species','clade'),
    col = c('white', 'cornsilk1', 'gold'),
    scale = TRUE,
    plotRsquared = TRUE)