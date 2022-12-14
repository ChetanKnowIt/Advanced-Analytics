library(shiny)
setwd("C:/Adv Analytics/Datasets/")
boston <- read.csv("Boston.csv")
library(ggplot2)
shinyServer(function(input, output) {
  output$hist <- renderPlot({
    plot_title <- paste("Boxplot of",input$num_var)
    df <-data.frame(col1=boston[,input$num_var])
    ggplot(data = df,aes(y=col1))+
      geom_boxplot( color='#2d6cdf', fill='#c5e3f6')+
      labs(y=input$num_var)+
      ggtitle(label = plot_title)+
      theme(plot.title = element_text(color='#2d6cdf', size=34, face="bold.italic", hjust = 0.5))
  })
  
  
  
})
