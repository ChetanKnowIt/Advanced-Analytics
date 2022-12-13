setwd("C:/Training/Academy/Statistics (Python)/Datasets")
co2 <- read.csv("CO2.csv")

bartlett.test(co2$uptake ~ co2$Treatment)
t.test(co2$uptake ~ co2$Treatment,
       var.equal=T)

###### Puromycin ##################
data("Puromycin")

bartlett.test(Puromycin$rate ~ Puromycin$state)
t.test(Puromycin$rate ~ Puromycin$state,
       var.equal=T)
# Conclusion: mean rates may be equal

####### Soporific $$$$$$$$
library(tidyr)
soporific <- read.csv("Soporific.csv")

sop1 <- soporific %>% pivot_longer(c(Drug.A,Drug.B),
                                   names_to="Drug", 
                                   values_to = "Effect")
bartlett.test(sop1$Effect ~ sop1$Drug)

t.test(sop1$Effect ~ sop1$Drug, var.equal=T)

# Conclusion: Effects of both drugs may be equal.