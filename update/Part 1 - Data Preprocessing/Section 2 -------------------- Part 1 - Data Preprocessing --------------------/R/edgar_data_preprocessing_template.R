#setear el directorio de trabajo
getwd()
setwd("~/Documents/GitHub/machinelearning-az/update/Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/R")
dir()

# importar el dataset
dataset = read.csv("Data.csv")

#completar datos faltantes
# Taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
dataset$Age[is.na(dataset$Age)] <- mean(dataset$Age, na.rm = TRUE)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)
dataset$Salary[is.na(dataset$Salary)] <- mean(dataset$Salary, na.rm = TRUE)

###################### datos factoriales #######################################
