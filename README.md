## Side note
From the first project, I have explored the complexity when it comes to picking models. How the fittiest model may cause high variance and how the simplier one can lead to high bias. To avoid and balance these two matters, I was introduced with alot of complex machines that perform beautifully with different dataset. Seemingly, Linear Regression - which is one of the most fundamental approach in model fitting - is being overlooked even though this machine can perform outstandingly with some suitable dataset. Therefore, for this project, I want to dive into the complexity of the Linear Regression Models (LRM) and show that with the right technique, Linear Model can be a powerful visualisation to trend recognisation and data fitting. 

First, what exactly is Linear Regression model? Linear Regression is an approach to graph the relationship between one response variable and one or more explanatory variables, under the assumption of linear relation. If there is only one independent varibale, we will call the model simple linear regression. But if there more than one explaining the dependent variable, we will call it multiple linear regression.

The most simpliest form of LRM is to assume a direct linear relationship between X and Y. However, X can also correlate to other transformations of Y, such as 1/Y, log(Y+1), 1/(Y+1), or square(Y). These transformation can do wonder especially when the condition for linear regression is met. In this project, we will explore what it means to chech for the quality and condition of a dataset and how it can assure the accuracy of our models.

As for now, we will go in to our topic. Our alcohol intakes have always been an interesting topic due to its various explanatory factors,body, mood, food consumption, other substance consumption. There is one article that particularly discuss about how our body takes in various types of alcohol differently even with the same recommended standard drink portion. They take into account that age and gender difference can affect the whole process, alongside other lurking variables such as health conditions and at the time medication intake. We issue an experimental study with 4 types of alcohol and one placebo: Tequila, White wine, Regular Beer, Mai Tai, and Water, and observe with similar age range and gender, how fast different type of alcohol wears off in one’s system.

Similar to the first project, data will be collected from the Island - a virtual simulation of human population that has been developed to support learning and teaching in experimental design, epidemiology and statistical reasoning. Since the citizens on this islad are divided into different group and each group is located at a different part of the island with different drinking habit, it makes more sense to choose randomly 15 people in each group so that our sample size will be 75 people. Then, these subjects will get to try out a random liquor out of the 5 options that we pick. We will have to make sure that the amount of people trying each liquor is even and the rest is juts wait 30 minutes and and use the breathalyzer to test and collect data. It will save time and and cost but still ensure a bias-minimized research.


# Topic: With the same unit of standardo all types of alcohol affect the digestive system the same way? - Project Overview
- Gathered data from simulated islanders using one question
- Used 10-fold Cross Valuation to set up 10 sets of training data and validating data 
- Calculated Mean Squared Prediction Error (MSPE) and drawed its distribution on boxplot based on each type of model and training-validating set we attempt to fit 
- Chose the model with lowest MSPE and narrowest shape in boxplot 
- Used the chosen model as our prediction machine to estimate pattern.

## Code and Resources Used
**R version**: 4.0.4 (2021-02-15)  
**Packages**: tidyverse, rpart, mgcv, MASS, glmnet.  
**Reference book**: An Introduction to Statistical Learning with Applications in R by *Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani   
**Link**: https://static1.squarespace.com/static/5ff2adbe3fe4fe33db902812/t/6009dd9fa7bc363aa822d2c7/1611259312432/ISLR+Seventh+Printing.pdf

## Data set
   **Data2020.csv** : training set
• Target Population: Male drinkers who’re in the age of 20-40
• Study Population: Male drinkers who’re in the age of 20-40 in the Island
• Experimental Unit (subject): Adult male
• Quantitative response variable: Change in BAC levels in the first 30 minutes
• Factor: Tequila, White wine, Regular Beer, Mai Tai, and Water

## Models
- Linear Regression Line
- Hybrid Stepwise
- Ridge Regression
- LASSO using CV with the 1SE min rule for its λ
- Generalized Addictive Models 
- Projection Pursuit Regression with numbers of terms up to 5
- Full regression tree 
- Regression tree using CV with 1SE and min optimal pruning

## Results

We sucessfully generate a boxplot of MSPE distribution throughout models and cross-validation folds.
![image](https://user-images.githubusercontent.com/108549500/195476453-b0ef19b9-6c90-48e8-a19c-133a266a8823.png)
![image](https://user-images.githubusercontent.com/108549500/195476896-8b8089ac-fa38-4ca7-91b5-cec5bb569db4.png)

It's noticeable right away the good performance that comes Generalized Addictive Model.

As we choose GAM to be our optimal machine, the prediction is quickly drawn out with its accuracy upto 90%. Below here is its table and scatterplot.

![image](https://user-images.githubusercontent.com/108549500/195500942-a9145a2e-f794-4cfe-9b4a-4419732d9a0e.png)
![image](https://user-images.githubusercontent.com/108549500/195502148-f6592516-3691-494b-9fd8-7f7ec1aa5b30.png)







