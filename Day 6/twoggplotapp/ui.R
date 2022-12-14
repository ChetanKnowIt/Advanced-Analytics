library(shiny)
library(shinythemes)
#Valid themes are: cerulean, cosmo, cyborg, darkly, flatly, journal, lumen, paper, readable, sandstone, simplex, slate, spacelab, superhero, united, yeti.
shinyUI(fluidPage(
  theme = shinytheme("cerulean"),
  titlePanel("Histogram for Boston Dataset"),
  
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
      plotOutput("hist"),
      plotOutput("box")
    )
  )
))
