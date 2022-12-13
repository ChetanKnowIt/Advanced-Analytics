setwd("C:/Training/Academy/Statistics (Python)/Datasets")
housing <- read.csv("Housing.csv")

ctab <- table(housing$gashw, housing$prefarea)
chisq.test(ctab)
