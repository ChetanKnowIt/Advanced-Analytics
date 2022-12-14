library(shiny)
setwd("C:/Training/Academy/Statistics (Python)/Datasets")
boston <- read.csv("Boston.csv")
library(ggplot2)
shinyServer(function(input, output) {
     output$box <- renderPlot({
       df <- data.frame(col1=boston[,input$num_var])
       ggplot(data = df, aes(y=col1))+
         geom_boxplot(color='red', fill='pink')+
         labs(x=input$num_var)
     }) 
})
