library(shiny)
setwd("C:/Adv Analytics/Datasets/")
boston <- read.csv("Boston.csv")

shinyServer(function(input, output) {
  output$hist <- renderPlot({
    hist(boston[,input$num_var],
         main=paste("Histogram of", input$num_var),
         xlab=input$num_var)
  })
  
  
  
})
