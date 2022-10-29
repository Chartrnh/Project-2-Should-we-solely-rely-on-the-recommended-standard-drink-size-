library(tidyverse)
library(dplyr)
library(lattice)
library(emmeans)

data <- read.csv("CSV.csv", header=TRUE, sep=",")
data <- subset(data, select=-c(6,7))
data <- rename(data, BAC=colnames(data[6]), Type=colnames(data[5]))

# sqrt Y
summary(fit2 <- lm(sqrt(BAC)~ Type, data=data))
pairwise.t.test(sqrt(data$BAC), data$Type, p.adjust="bonferroni")
