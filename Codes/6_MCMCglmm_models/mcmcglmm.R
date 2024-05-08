library(MCMCglmm)

args <- commandArgs(trailingOnly = TRUE)

i1 = args[1]
i2 = args[2]
o1 = args[3]
o2 = args[4]
o3 = args[5]


set.seed(123)

#data = read.csv('data.csv')
data = read.csv(i1)
#tree = read.tree('Species.r8s.tre')
tree = read.tree(i2)
inv.phylo <- inverseA(tree, nodes = "TIPS", scale = TRUE)$Ainv
prior <- list(G = list(G1 = list(V = 1, nu = 0.002)), R = list(V = 1, nu = 0.002))
#prior <- list(G = list(G1 = list(V = 1, nu = 0.002),G2 = list(V = 1, nu = 0.002)), R = list(V = 1, nu = 0.002))
nitt <- 1000000
burnin <- 100000
thin <- 500
model = MCMCglmm(log(Exp + 1) ~ Host, data = data, random= ~Species,ginverse = list(Species = inv.phylo), family = "gaussian",prior = prior,nitt = nitt, thin = thin, burnin = burnin,  verbose = TRUE)
#model = MCMCglmm(log(Exp + 1) ~ Host, data = data,random= ~Species + Gene ,ginverse = list(Species = inv.phylo), family = "gaussian",prior = prior,nitt = nitt, thin = thin, burnin = burnin,  verbose = TRUE)

saveRDS(model, file = o1)


d = geweke.diag(as.mcmc(model$Sol))
write.csv(d$z,file=o2)
r = summary(model)$solutions
write.csv(r,file=o3)
