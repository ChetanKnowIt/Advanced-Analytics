setwd("C:/Training/Academy/Statistics (Python)/Datasets")
pg = read.csv("PlantGrowth.csv")

t.test(pg$weight, mu=6, alternative = 't')
t.test(pg$weight, mu=6, alternative = 'g')
t.test(pg$weight, mu=6, alternative = 'l')


co2 <- read.csv("CO2.csv")
t.test(co2$uptake, mu=30, alternative = 'l')

data(Indometh)
t.test(Indometh$conc, mu=0.3, alternative = "g")
