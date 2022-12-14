library(shiny)

shinyUI(fluidPage(

    titlePanel("Scatter Plot"),

    sidebarLayout(
        sidebarPanel(
            selectInput(inputId = "num_X", 
                  label = "Select X-axis Variable",
                  choices = list("crim","indus",
                                "nox","age",
                                "dis","medv")),
            selectInput(inputId = "num_Y", 
                        label = "Select Y-axis Variable",
                        choices = list("age", "crim","indus",
                                       "nox",
                                       "dis","medv"))
        ),
        mainPanel(
            plotOutput(outputId = "scatter")
        )
    )
))
