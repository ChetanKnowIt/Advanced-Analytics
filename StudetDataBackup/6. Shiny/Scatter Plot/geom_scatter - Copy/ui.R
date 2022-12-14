library(shiny)

shinyUI(fluidPage(

    titlePanel("Scatter Plot"),

    sidebarLayout(
        sidebarPanel(
            selectInput(inputId = "num_X", 
                  label = "Select X-axis Variable:",
                  choices = list("Price","MPG.city",
                                 "MPG.highway","EngineSize",
                                 "Horsepower","Fuel.tank.capacity")),
            selectInput(inputId = "num_Y", 
                        label = "Select Y-axis Variable:",
                        choices = list("MPG.city","Price",
                                       "EngineSize","MPG.highway",
                                       "Horsepower","Fuel.tank.capacity")),
            selectInput(inputId = "colour",
                        label = "Colour by:",
                        choices = list("AirBags","Origin","DriveTrain"))
        ),
        mainPanel(
            plotOutput(outputId = "scatter")
        )
    )
))
