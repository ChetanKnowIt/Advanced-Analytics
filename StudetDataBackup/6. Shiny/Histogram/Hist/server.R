library(shiny)
setwd("C:/Training/Academy/Statistics (Python)/Datasets")
cars93 <- read.csv("Cars93.csv")
shinyServer(function(input, output) {
     output$hist <- renderPlot({
       hist(cars93[,input$num_var], 
            main=paste("Histogram of", input$num_var))
     }) 
})
