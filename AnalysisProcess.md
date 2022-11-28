## Machine learning: find a fitting LR model 

1. Data Verification - check for the condition of LRM on given data

When it comes to Linear Regression, it is unreasonable to "blatantly" assume its compatibility with the dataset, instead, it is important to first check the data's quality. We can do it by looking at its distribution on the histogram, the model equation, and the Normal QUantile-quantile plot itself. The conditions we have to check are: 
- Linearity
- Constant Variance
- Independence 
- Randomness
- Normality

![Figure_1](https://user-images.githubusercontent.com/108549500/198199350-85435984-b5fb-40d8-8946-73696a73b6b2.png)   

In this histogram, each category is being graphed based on its percentage of the total count, instead of its actual count. It was done intentionally so that an obvious placebo-like Water would not disrupt the visibility of other observations. A fitted line is also added for each histogram to visualize its distribution. Therefore, by looking at it, we can briefly judge the distribution of BAC based on each category of its independent variable and so far, there were no typos or unusual values that should be noted. However, there are some that I have to point out:  
- Tequila: The distribution seems to be normal with a little bit of right-skewed 
- Water: this treatment group particularly reacts unchanged throughout the sample which perfectly represents a placebo treatment
does not affect BAC level 
- White wine: The distribution seems to be left-skewed 
- Mai Tai: the distribution is right-skewed 
- Regular Beer: The distribution is right-skewed

![image](https://user-images.githubusercontent.com/108549500/198203043-796ea32a-d338-437d-a161-fa7ad737df4b.png)
![Figure_2](https://user-images.githubusercontent.com/108549500/198203368-800557c9-5748-4fa1-9e0e-f22389f2e39b.png)
![Figure_3](https://user-images.githubusercontent.com/108549500/198206205-c39c21b9-5621-432f-9978-7adfa6519c76.png)


- Linearity: Judging from the model summary, BAC and type alcohol have a relatively linear relationship despite some variance at the two ends
- Randomness: This is one of the few conditions that can be confidently assumed due to individual involvement with the data collection process itself
- Independence: Since each treatment groups are mutually exclusive, independence can be satisfactorily assumed
- Normality: According to the Normal QQ plot, this condition is not met because, from the 1st deviation going forward, the distribution is going off the normal line
- Constant Variance: From the residual and fitted, it can be seen that each treatment group’s variances are not constant

There are problems with the condition check that raises the flag that a simple form of LRM might not be suitable for the data, therefore, some transformation will be needed. The 'Type of Alcohol' factor is a categorical variable, so transformation would be done on BAC level exclusively. To keep the simplicity and the digestibility of the project, I decide to only stick with the transformation of only LRM instead of others so that I can showcase its effectiveness. Transformations I consider are: 
- logarithm of BAC+1
- 1/(BAC+1)
- Square root of BAC  

Each will be tried out and graphed to see which one is the most fitted compared to the original model

2. Machine Learning - SLR
From the condition check from the simple LRM before, three criteria were not met. Therefore, we will solely focus on those three criteria when putting each transformation in comparison with the simple LRM and observe any changes or improvements. 
- First is logarithm of BAC+1 or log(BAC+1)
   
![image](https://user-images.githubusercontent.com/108549500/198208433-cda382bc-db00-4a34-99f8-86546ac6c82b.png)
![Figure_4](https://user-images.githubusercontent.com/108549500/198208660-fa7b51eb-b60c-4323-8df8-ad1c68f061af.png) 

- Independence: Yes
- Normality: According to the Normal QQ plot, this condition is improved because, from the positive 1st deviation going forward, the distribution is seemingly going closer to the line than it did before
- Constant Variance: From the residual and fitted, it can be seen that each treatment group’s
variances are not constant

- Square root of BAC

![image](https://user-images.githubusercontent.com/108549500/198209104-6a1b8b9e-e30e-4528-9b70-0a33244c9397.png)
![Figure_5](https://user-images.githubusercontent.com/108549500/198209278-44250446-10df-403c-a097-05b7af830650.png)

- Independence: Yes
- Normality: According to the Normal QQ plot, this condition is improved because, from the positive 1st deviation going forward, the distribution is seemingly going closer to the line than
it did even when using log(BAC+1)
- Constant Variance: From the residual and fitted, it can be seen that this is the most fitted to the constant line compared to other

- 1/(BAC+1)  

![image](https://user-images.githubusercontent.com/108549500/198210869-956a9c0e-ba81-40b0-b85f-259a85765a09.png)
![Figure_6](https://user-images.githubusercontent.com/108549500/198209154-b2261761-a78a-4dd2-bfc9-3939af982c16.png)

- Independence: Yes
- Normality: According to the Normal QQ plot, this condition is getting even more off the normally distributed line
- Constant Variance: From the residual and fitted, it can be seen that each treatment group’s variances are not constant

Out of the three models, it is visible that the square root of BAC is the one transformation that improves the performance of LRM on given data, specifically the two picky conditions, Normality, and Constant variance. Therefore, the final chosen model will be the Linear Regression Model with the square root of BAC.  

## Study of each observation

After figuring out the fitted model, the next step is to use it to access the machine's insight and perform hypothesis testing with the premise of finding if, with the same unit of standard, different alcoholic drinks impact our bodies differently. 

To approach this question, we will use each variable group's means along with a pairwise comparison process and build up hypothesis testing. Assume u1 for the Water group,u2 for the Mai Tai group, u3 for the Regular Beer group, u4 for the Tequila group, and u5 for the White Wine group. The null hypothesis will claim that each group has the same effect as the other and the alternative hypothesis will be u are not equal.  

H0: u1=u2=u3=u4=u5  
H1: u1 >< u2 >< u3 >< u4 >< u5

![image](https://user-images.githubusercontent.com/108549500/198747822-f2fb3c57-59cc-45e5-bf9a-519ba14cd08d.png)

First, just looking at the estimated means and adjusted inference table, we can see that each type of drink has its value mean that differs from each other. The only two that stand close in value are Regular Beer and Tequila, but still not close enough to not reject the null hypothesis. Overall, each observation is performing as expected, with Water as the intended placebo and the other 4 groups(Mai Tai, Regular Beer, Tequila, and White Wine) placing a value significantly away from the mean 0.

Next, we will look at the t-value of each type, by using a Pairwise comparison with Bonferroni correction as Familywise Error Rate Control. The reason for choosing Bonferroni over Fisher's correction and Tukey's correction is because of the Pairwise comparison's nature that carries an increasing probability of false positive in t-value testing and the compatibility Bonferroni correction has with a small number of comparisons. And for this hypothesis, we will use α = 0.05 as the significant criterion. The matrix will be shown below: 

![image](https://user-images.githubusercontent.com/108549500/198751045-66a8ec2f-7238-4e6a-975b-3d9c41e7569d.png)

We can see from the matrix, all possible pairwise comparisons were performed, and the p-values were adjusted using a Bonferroni correction. Setting aside Water, we have 3 more pairs (White Wine - Tequila, White wine - Regular Beer, and white wine - Mai Tai) that differed significantly from each other (adjusted p << α) based on an α-level of 0.05. No other pairwise differences were significant. For our output, because the p-values of those 7 pairs (including water) out of 10 tests are less than the significant criteria, it’s reasonable to reject H0 and conclude a crucial difference among 5 groups.

## Conclusion
 As the data perform within our expectation and there’s no large variance or outlier, we can wrap up the project and state that the effect of real treatment groups is significantly different from the placebo group and each type of alcohol have a significant and different effect on human Blood Alcohol Concentrate level.



