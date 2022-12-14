library(shiny)

shinyUI(fluidPage(

    titlePanel("Boxplot"),

    sidebarLayout(
        sidebarPanel(
            selectInput(inputId = "num_var", 
            label = "Select a Variable",
            choices = list("crim","indus",
                          "nox","age",
                          "dis","medv"))
        ),
        mainPanel(
            plotOutput(outputId = "box")
        )
    )
))
