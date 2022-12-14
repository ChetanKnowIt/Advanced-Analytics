library(shiny)

shinyUI(fluidPage(

    titlePanel("Histogram"),

    sidebarLayout(
        sidebarPanel(
            selectInput(inputId = "num_var", 
            label = "Select a Variable",
            choices = list("crim","indus",
                          "nox","age",
                          "dis","medv"))
        ),
        mainPanel(
            plotOutput(outputId = "hist")
        )
    )
))
