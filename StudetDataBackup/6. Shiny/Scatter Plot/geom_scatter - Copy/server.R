library(shiny)
library(ggplot2)
setwd("C:/Training/Academy/Statistics (Python)/Datasets")
cars93 <- read.csv("Cars93.csv")
shinyServer(function(input, output) {
     output$scatter <- renderPlot({
       df <- cars93[,c(input$num_X, input$num_Y , input$colour)]
       colnames(df) <- c('col1','col2','col3')
       ggplot(data = df, aes(x=col1, y=col2, color=col3)) + 
         geom_point() +
         labs(x=input$num_X, y=input$num_Y, color=input$colour)
       }) 
})
