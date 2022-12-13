setwd("C:/Adv Analytics/Datasets/")
pur <- read.csv("Puromycin.csv")
bartlett.test(pur$rate ~ pur$state)
t.test(pur$rate ~ pur$state, var.equal = T)




sop <- read.csv("Soporific.csv")
library(tidyr)
sop_pivot<-pivot_longer(sop, cols = c("Drug.A", "Drug.B"), 
                        names_to  = "DrugType", 
                        values_to= "Effect")
bartlett.test(sop_pivot$Effect ~ sop_pivot$DrugType)
t.test(sop_pivot$Effect ~ sop_pivot$DrugType, var.equal = T)


hop <- read.csv("Housing.csv")
bartlett.test(hop$price~hop$prefarea)
t.test(hop$price~hop$prefarea, var.equal = F)


ecbm <- read.csv("ECONOMIST-BIGMAC_IND.csv")






