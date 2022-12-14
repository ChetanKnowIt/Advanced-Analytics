library(shiny)
setwd("C:/Adv Analytics/Datasets/")
boston <- read.csv("Boston.csv")
library(ggplot2)
shinyServer(function(input, output) {
  output$hist <- renderPlot({
    df <-data.frame(col1=boston[,input$num_var])
    ggplot(data = df,aes(x=col1))+
      geom_histogram(bins=20, color='#2d6cdf', fill='#c5e3f6')+
      labs(x=input$num_var)+
      ggtitle(label = "Histogram of", input$num_var)
  })
  
  
  
})
