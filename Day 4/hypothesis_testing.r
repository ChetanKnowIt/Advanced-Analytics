setwd('C:/Adv Analytics/Datasets/')
pg = read.csv('PlantGrowth.csv')

pg$weight
t.test(pg$weight, mu=6, alternative = 't')                     
t.test(pg$weight, mu=6, alternative = 'g')                     
t.test(pg$weight, mu=6, alternative = 'l')                     

(mean(pg$weight)-6)/(sd(pg$weight)/sqrt(30))


co = read.csv('CO2.csv')
t.test(co$uptake, mu=30, alternative = 'l')                     


indo = read.csv('Indometh.csv')
indo
t.test(indo$conc, mu=0.30, alternative = 'g')
t.test(indo$conc, mu=0.30, alternative = 't')
t.test(indo$conc, mu=0.30, alternative = 'l')


ano = read.csv('anorexia.csv')
cont = subset(ano, Treat=="Cont")
cont
t.test(cont$Prewt, cont$Postwt, mu =0, paired = T, alternative = "l")

cbt = subset(ano, Treat=="CBT")
t.test(cbt$Prewt, cbt$Postwt, mu =0, paired = T, alternative = "l")

ft = subset(ano, Treat=="FT")
t.test(ft$Prewt, ft$Postwt, mu =0, paired = T, alternative = "l")



rhu = read.csv('Rheumatic.csv')
t.test(rhu$Before, rhu$After, paired = T, alternative = 'l')

plaque <- read.csv('Plaque.csv')

library(tidyr)

plaque_pivot<-pivot_wider(plaque, id_cols = c("Id", "product"), names_from = "trt", values_from = "score")
p1 <- subset(plaque_pivot, product =="P1")
p2 <- subset(plaque_pivot, product =="P2")
p3 <- subset(plaque_pivot, product =="P3")

t.test(p1$Before, p1$After, paired = T, alternative = 'g')
t.test(p2$Before, p2$After, paired = T, alternative = 'g')
t.test(p3$Before, p3$After, paired = T, alternative = 'g')








