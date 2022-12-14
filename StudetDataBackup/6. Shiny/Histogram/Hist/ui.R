library(shiny)

shinyUI(fluidPage(

    titlePanel("Histogram"),

    sidebarLayout(
        sidebarPanel(
            selectInput(inputId = "num_var", 
            label = "Select a Variable",
            choices = list("Price","MPG.highway",
                          "MPG.city","EngineSize",
                          "Horsepower","Fuel.tank.capacity"))
        ),
        mainPanel(
            plotOutput(outputId = "hist")
        )
    )
))
