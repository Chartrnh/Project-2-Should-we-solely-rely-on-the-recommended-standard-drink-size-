## Side note
From the first project, I have explored the complexity of the Machine Learning process. How the fittest model may cause high variance and how the simpler one can lead to high bias. To avoid and balance these two matters, I introduce a lot of complex machines that perform beautifully with a different datasets. Seemingly, Linear Regression - which is one of the most fundamental approaches in model fitting - is being overlooked even though this machine can perform outstandingly with some suitable dataset. so for this project, I want to dive into the complexity of the Linear Regression Models (LRM) and show that with the right technique, Linear Models can be a powerful visualization for trend recognization and data fitting. 

First, what exactly is the Linear Regression model? Linear Regression is an approach to graph the relationship between one response variable and one or more explanatory variables, under the assumption of a linear relation. If there is only one independent variable, we will call the model simple linear regression. But if there is more than one explaining the dependent variable, we will call it multiple linear regression.

The simplest form of LRM is to assume a direct linear relationship between X and Y. However, X can also correlate to other transformations of Y, such as 1/Y, log(Y+1), 1/(Y+1), or square(Y). These transformations can do wonders especially when the condition for linear regression is met. In this project, we will explore what it means to check for the quality and condition of a dataset and how it can assure the accuracy of our models.

As for now, we will go into our topic. 

Our alcohol intake has always been an interesting topic due to its various explanatory factors, body, mood, food consumption, and other substance consumption. There is one article that particularly discusses how our body takes in various types of alcohol differently even with the same recommended standard drink portion, with the consideration of age and gender difference, alongside other lurking variables such as health conditions and at the time medication intake. We will study this issue with 4 types of alcohol and one placebo: Tequila, White wine, Regular Beer, Mai Tai, and Water, and observe the different effects each type of alcohol brings to one’s system.

Similar to the first project, data will be collected from the Island - a virtual simulation of the human population that has been developed to support learning and teaching in experimental design, epidemiology, and statistical reasoning. Since the citizens on this island are divided into different groups and each group is located at a different part of the island with a different drinking habit, it makes more sense to choose randomly 15 people in each group so that our sample size will be 75 people. Then, these subjects will get to try a random liquor out of the 5 options that we pick. We will have to make sure that the amount of people trying each liquor is even and the rest is just waiting 30 minutes and use the breathalyzer to test and collect data. It will save time and cost but still ensure bias-minimized research.


# Topic: Do all types of alcohol affect the digestive system in the same way? - Project Overview
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
Linear regression with the different forms of a dependent variable
- Y
- Square root of Y 
- Logarithm of Y+1
- 1/(Y+1) 

## Results
After testing out several forms of LRM, I have found LRM with the square root of Y to be a fitting model as it solves the variance on the upper end of the Normal Q-Q plot compared to the simple LRM. We will use it to dive further into the study of each type of alcohol (or in this study calls - observation) 
<img width="301" alt="Figure_2" src="https://user-images.githubusercontent.com/108549500/198194294-3dfb6b23-d74d-44f9-85e0-08a436554738.png">                  <img width="298" alt="Figure_5" src="https://user-images.githubusercontent.com/108549500/198194392-41ee785f-ae30-4a5c-adfc-0e7befed3ab2.png">

With this form of LRM in mind, we also conclude that each type of alcohol has a significant and different effect on human Blood Alcohol Concentrate level, by doing hypothesis testing using pairwise comparison with a Bonferroni correction. The dominance in significant pairs (7 out of 10) affirms our assumption. 

![image](https://user-images.githubusercontent.com/108549500/198751045-66a8ec2f-7238-4e6a-975b-3d9c41e7569d.png)













