library(shiny)
setwd("C:/Training/Academy/Statistics (Python)/Datasets")
boston <- read.csv("Boston.csv")
shinyServer(function(input, output) {
     output$scatter <- renderPlot({
       df <- boston[,c(input$num_X, input$num_Y)]
       plot(df[,1], df[,2], xlab = input$num_X, ylab = input$num_Y)
       
     }) 
})
