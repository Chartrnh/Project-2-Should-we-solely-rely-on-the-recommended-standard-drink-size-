## Side note
From the first project, I have explored the complexity when it comes to considering different models. How the fittiest model may cause high variance and how the simplier one can lead to high bias. To avoid and balance these two matters, I was introduced with alot of complex machines that perform beautifully with different dataset. Seemingly, Linear Regression - which is one of the most fundamental approach in model fitting - is being overlooked even though this machine can perform outstandingly with some suitable dataset. Therefore, for this project, I want to dive into 


As for now, to tackle the complexity of this matter, I will start off with a topic that is just about model selections. Specifically, I will dive into a dataset with 15 explanatory variables and one response variable. The chosen data will attempt to explain the effect that outer factors have on one's choice of meal cost, such as their financial situation, education, number of meals a day, workclass etc, and how we can predict their choice based on these characeristics. The objective of this project is to only focus on finding the most suitable prediction model for it and use it to test on other datasets. 

The data will be collected from the Island - a virtual simulation of human population that has been developed to support learning and teaching in experimental design, epidemiology and statistical reasoning. These simulated islanders will be asked a simple question of how much they spend on a meal, followed some personal questions about theit income, workclass, education and we will use the data to predict individual spending on food and its pattern.

# Topic: What is the optimal machine? - Project Overview
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
- **Data2020.csv** : training set
- **Data2020testX.csv** : prediction testing set  
*Both on the file

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







