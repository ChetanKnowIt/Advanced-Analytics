setwd("C:/Adv Analytics/Datasets/")
housing <- read.csv("Housing.csv")

ctab <- table(housing$gashw, housing$prefarea)
chisq.test(ctab)
