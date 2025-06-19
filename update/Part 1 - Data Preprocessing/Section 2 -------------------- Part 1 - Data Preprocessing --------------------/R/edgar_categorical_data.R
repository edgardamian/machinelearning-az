#setear el directorio de trabajo
############### 1.setear el directorio de trabajo #############################
getwd()
setwd("~/Documents/GitHub/machinelearning-az/update/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/R")
dir()

########################### 2.Importar el dataset ###############################
dataset = read.csv("Data.csv")
# dataset <- dataset[,2:3]

###################### 4.datos categóricos #######################################
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased,
                           levels = c('No', 'Yes'),
                           labels = c(0, 1))

###################### 5.dividir datos para entrenamiento #######################################
library(caTools)
set.seed(123)
split <- sample.split(dataset$Purchased, SplitRatio = 0.8)
split

training_set <- subset(dataset, split == TRUE)
testing_set <- subset(dataset, split == FALSE)

###################### 6.escalar datos #######################################
# training_set[,2:3] <- scale(training_set[,2:3])
# testing_set[,2:3] <- scale(testing_set[,2:3])

