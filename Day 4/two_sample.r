setwd("C:/Adv Analytics/Datasets/")
co2 <- read.csv("CO2.csv")

bartlett.test(co2$uptake ~ co2$Treatment)
