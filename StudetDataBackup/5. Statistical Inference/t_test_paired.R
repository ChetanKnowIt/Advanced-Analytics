setwd("C:/Training/Academy/Statistics (Python)/Datasets")
anorexia <- read.csv("anorexia.csv")

cont <- subset(anorexia, Treat=="Cont")
t.test(cont$Prewt, cont$Postwt, mu = 0, paired = T, alternative = "l")

cbt <- subset(anorexia, Treat=="CBT")
t.test(cbt$Prewt, cbt$Postwt, mu = 0, paired = T, alternative = "l")

ft <- subset(anorexia, Treat=="FT")
t.test(ft$Prewt, ft$Postwt, mu = 0, paired = T, alternative = "l")

############## Rheumatic #####################
rhum <- read.csv("Rheumatic.csv")
t.test(rhum$Before, rhum$After, paired = T, alternative = "l")
#or
t.test(rhum$After, rhum$Before, paired = T, alternative = "g")

################ Plaque ##################
library(tidyr)
plaque <- read.csv("Plaque.csv")

plaq_pivot <- pivot_wider(plaque, id_cols = c("Id","product"),
            names_from = "trt", values_from = "score")

P1 <- subset(plaq_pivot, product=="P1")
t.test(P1$Before, P1$After, paired = T, alternative = 'g')

P2 <- subset(plaq_pivot, product=="P2")
t.test(P2$Before, P2$After, paired = T, alternative = 'g')

P3 <- subset(plaq_pivot, product=="P3")
t.test(P3$Before, P3$After, paired = T, alternative = 'g')

