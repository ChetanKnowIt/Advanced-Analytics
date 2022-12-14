library(shiny)
library(ggplot2)
setwd("C:/Training/Academy/Statistics (Python)/Datasets")
boston <- read.csv("Boston.csv")
shinyServer(function(input, output) {
     output$scatter <- renderPlot({
       df <- boston[,c(input$num_X, input$num_Y)]
       colnames(df) <- c('col1','col2')
       ggplot(data = df, aes(x=col1, y=col2)) + 
         geom_point() +
         labs(x=input$num_X, y=input$num_Y)    
       }) 
})
