## Analysis Outlier 

1. Chech the condition of this dataset

When it comes to Linear Regression, it is unreasonable to "blatantly" assume its compatibiltiy to the dataset, instead it is important to first check the data's quality. We can do it by looking at its distribution on histogram and the model equation itself. The conditions we have to check are: 
- Linearity
- Constant Variance
- Independence 
- Randomness
- Normality

![Figure_1](https://user-images.githubusercontent.com/108549500/198199350-85435984-b5fb-40d8-8946-73696a73b6b2.png)   

In this histogram, each category is being graphed based on its percentage of total count, instead of its actual count. It was done intentionally so that a obvious placebo  like Water would not disrupt the visibility of other observations. A fiited line is also added for each histogram to visualise its distribution. Therefore, by looking at it, we can briefly judge the distribution of BAC based on each category of its independent variable and so far, there were no typos or unusual values that should be noted. Specifically:  
- Tequila: The distribution seems to be normal with a little bit right-skewed 
- Water: this treatment group particularly has reaction unchanged throughout the sample which is perfectly represent a placebo treatment
has no effect on BAC level 
- White wine: The distribution seems to be left-skewed 
- Mai Tai: the distribution is right-skewed 
- Reguler Beer: The distribution is right-skewed


Independence: Since each treatment groups are mutually exclusive, independence can besatisfactorily assumed
• Normality: According to the Normal QQ plot, this condition is not met because from the 1st
deviation going foward, the distribution is going off the normal line
• Constant Variance: From the residual and fitted, it can be seen that each treatment group’s
variances are not constant

Description: (a) 
