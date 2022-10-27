## Side note
From the first project, I have explored the complexity when it comes to picking models. How the fittiest model may cause high variance and how the simplier one can lead to high bias. To avoid and balance these two matters, I was introduced with alot of complex machines that perform beautifully with different dataset. Seemingly, Linear Regression - which is one of the most fundamental approach in model fitting - is being overlooked even though this machine can perform outstandingly with some suitable dataset. Therefore, for this project, I want to dive into the complexity of the Linear Regression Models (LRM) and show that with the right technique, Linear Model can be a powerful visualisation to trend recognisation and data fitting. 

First, what exactly is Linear Regression model? Linear Regression is an approach to graph the relationship between one response variable and one or more explanatory variables, under the assumption of linear relation. If there is only one independent varibale, we will call the model simple linear regression. But if there more than one explaining the dependent variable, we will call it multiple linear regression.

The most simpliest form of LRM is to assume a direct linear relationship between X and Y. However, X can also correlate to other transformations of Y, such as 1/Y, log(Y+1), 1/(Y+1), or square(Y). These transformation can do wonder especially when the condition for linear regression is met. In this project, we will explore what it means to chech for the quality and condition of a dataset and how it can assure the accuracy of our models.

As for now, we will go in to our topic. Our alcohol intakes have always been an interesting topic due to its various explanatory factors,body, mood, food consumption, other substance consumption. There is one article that particularly discuss about how our body takes in various types of alcohol differently even with the same recommended standard drink portion. They take into account that age and gender difference can affect the whole process, alongside other lurking variables such as health conditions and at the time medication intake. We issue an experimental study with 4 types of alcohol and one placebo: Tequila, White wine, Regular Beer, Mai Tai, and Water, and observe with similar age range and gender, how fast different type of alcohol wears off in one’s system.

Similar to the first project, data will be collected from the Island - a virtual simulation of human population that has been developed to support learning and teaching in experimental design, epidemiology and statistical reasoning. Since the citizens on this islad are divided into different group and each group is located at a different part of the island with different drinking habit, it makes more sense to choose randomly 15 people in each group so that our sample size will be 75 people. Then, these subjects will get to try out a random liquor out of the 5 options that we pick. We will have to make sure that the amount of people trying each liquor is even and the rest is juts wait 30 minutes and and use the breathalyzer to test and collect data. It will save time and and cost but still ensure a bias-minimized research.


# Topic: Do all types of alcohol affect the digestive system the same way? - Project Overview
- Target Population: Male drinkers who’re in the age of 20-40
- Experimental Unit (subject): Adult male
- Quantitative response variable: Change in BAC levels in the first 30 minutes
- Factor: Tequila, White wine, Regular Beer, Mai Tai, and Water

## Code and Resources Used
**R version**: on JupyterHub  
**Packages**: tidyverse, lattice, emmeans 
**Python version**: Python 3.10.8  
**Modules**: pandas, numpy, ValuesView, matplotlib.pyplot, matplotlib, matplotlib.ticker , seaborn, statsmodels.api, ols  
**Article**: How Long Does Alcohol Stay In Your System?
**Resource**: STAT2 Modeling with Regression and ANOVA - *Ann Cannon; George W. Cobb; Bradley A. Hartlaub; Julie M. Legler; Robin H. Lock; Thomas L. Moore; Allan J. Rossman; Jeffrey A. Witmer*  
**Link**: [https://static1.squarespace.com/static/5ff2adbe3fe4fe33db902812/t/6009dd9fa7bc363aa822d2c7/1611259312432/ISLR+Seventh+Printing.pdf](https://www.addictioncenter.com/alcohol/how-long-is-alcohol-in-your-system/)  
https://www.macmillanlearning.com/college/us/product/STAT2/p/1319054072

## Data set: 
**Data.csv**


## Models
Linear regression with different formation of of dependent variable
- Y
- Square root of Y 
- Logarithm of Y+1
- 1/(Y+1) 

## Results









