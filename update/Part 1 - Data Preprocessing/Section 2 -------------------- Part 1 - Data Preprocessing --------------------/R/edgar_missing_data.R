#setear el directorio de trabajo
############### 1.setear el directorio de trabajo #############################
getwd()
setwd("~/Documents/GitHub/machinelearning-az/update/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/R")
dir()

########################### 2.Importar el dataset ###############################
dataset = read.csv("Data.csv")
# dataset <- dataset[,2:3]

############################## 3.Manejo de datos faltantes ######################
# primera forma de reemplazar datos faltantes en age
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

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
