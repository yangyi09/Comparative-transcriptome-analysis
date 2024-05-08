library(OUwie)

t = read.tree('Species.r8s.tre')
dat <- read.csv('tmp.csv', header=F)
dat$V2 = as.character(dat$V2)


BM1 <- OUwie(t, dat, model='BM1',quiet=T)
cat (BM1$AICc)
cat ('\t')

OU1 <- OUwie(t, dat, model='OU1',quiet=T)
cat (OU1$AICc)
cat ('\t')

#OUM <- OUwie(t, dat, model='OUM')

for (i in 1:19) {
	x <- dat
	x[i,2] <- '2'
	OUM <- OUwie(t, x, model='OUM',quiet=T)
	cat (OUM$AICc)
	cat ('\t')
}
