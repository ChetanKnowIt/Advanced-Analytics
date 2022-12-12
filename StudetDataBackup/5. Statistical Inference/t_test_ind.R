setwd("C:/Training/Academy/Statistics (Python)/Datasets")
co2 <- read.csv("CO2.csv")

bartlett.test(co2$uptake ~ co2$Treatment)
