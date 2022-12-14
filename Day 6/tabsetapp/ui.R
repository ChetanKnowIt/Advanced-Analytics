library(shiny)
library(shinythemes)
#Valid themes are: cerulean, cosmo, cyborg, darkly, flatly, journal, lumen, paper, readable, sandstone, simplex, slate, spacelab, superhero, united, yeti.
shinyUI(fluidPage(
  theme = shinytheme("cerulean"),
  titlePanel("Boston Details:"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput(inputId = "num_var",
                  label = "Select A variable: ",
                  choice = list("crim", 
                                "zn",
                                "indus",
                                "nox",
                                "rm",
                                "medv",
                                "age"))
      
    ),
    mainPanel(
      
      tabsetPanel(
        tabPanel("Histogram",plotOutput(outputId = "hist")),
        tabPanel("Boxplot",plotOutput(outputId = "box")),
        tabPanel("Data", dataTableOutput(outputId = "tbl"))
      )
    )
  )
))
