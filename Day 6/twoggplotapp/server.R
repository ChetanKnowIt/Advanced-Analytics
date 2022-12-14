library(shiny)
setwd("C:/Adv Analytics/Datasets/")
boston <- read.csv("Boston.csv")
library(ggplot2)
shinyServer(function(input, output) {
  output$box <- renderPlot({
    df <-data.frame(col1=boston[,input$num_var])
    ggplot(data = df,aes(y=col1))+
      geom_boxplot( color='#2d6cdf', fill='#c5e3f6')+
      labs(y=input$num_var)+
      ggtitle(label = paste("Boxplot of",input$num_var))+
      theme(plot.title = element_text(size=16, face="bold", hjust = 0.5),
    axis.title.y = element_text(size=14, face="bold"))
  })
  
  output$hist <- renderPlot({
    df <-data.frame(col1=boston[,input$num_var])
    ggplot(data = df,aes(x=col1))+
      geom_histogram(bins=20, color='#2d6cdf', fill='#c5e3f6')+
      labs(x=input$num_var)+
      ggtitle(label = paste("Histogram of",input$num_var))+
      theme(plot.title = element_text(size=16, face="bold", hjust = 0.5),
            axis.title.x = element_text(size=14, face="bold"),
            axis.title.y = element_text(size=14, face="bold"))
    
  })
  
  
})
