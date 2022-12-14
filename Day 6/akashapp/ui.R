library(shiny)
library(shinythemes)
#Valid themes are: cerulean, cosmo, cyborg, darkly, flatly, journal, lumen, paper, readable, sandstone, simplex, slate, spacelab, superhero, united, yeti.
shinyUI(fluidPage(
  theme = shinytheme("cerulean"),
    titlePanel("Histogram"),

    sidebarLayout(
        sidebarPanel(
          selectInput(inputId = "num_var",
                     label = "Select A variable: ",
                     choice = list("Price","MPG.highway",
                                   "MPG.city","EngineSize","Horsepower","Fuel.tank.capacity"))

        ),

        mainPanel(
            plotOutput("hist")
        )
    )
))
