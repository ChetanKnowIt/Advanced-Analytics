library(shiny)
setwd("C:/Training/Academy/Statistics (Python)/Datasets")
boston <- read.csv("Boston.csv")
library(ggplot2)
shinyServer(function(input, output) {
    output$hist <- renderPlot({
      df <- data.frame(col1=boston[,input$num_var])
      ggplot(data = df, aes(y=col1))+
        geom_histogram(color='red', fill='pink',bins=20)+
        labs(x=input$num_var)
    })
  
     output$box <- renderPlot({
       df <- data.frame(col1=boston[,input$num_var])
       ggplot(data = df, aes(y=col1))+
         geom_boxplot(color='deepskyblue1', fill='lightskyblue1')+
         labs(x=input$num_var)
     }) 
     
     output$tbl <- renderDataTable({boston})
})
