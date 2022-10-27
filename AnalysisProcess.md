## Analysis Outlier 

1. Data Verification - check for condition of LRM on given data

When it comes to Linear Regression, it is unreasonable to "blatantly" assume its compatibiltiy to the dataset, instead it is important to first check the data's quality. We can do it by looking at its distribution on the histogram, the model equation, and the Normal QUantile-quantile plot itself. The conditions we have to check are: 
- Linearity
- Constant Variance
- Independence 
- Randomness
- Normality

![Figure_1](https://user-images.githubusercontent.com/108549500/198199350-85435984-b5fb-40d8-8946-73696a73b6b2.png)   

In this histogram, each category is being graphed based on its percentage of total count, instead of its actual count. It was done intentionally so that a obvious placebo  like Water would not disrupt the visibility of other observations. A fiited line is also added for each histogram to visualise its distribution. Therefore, by looking at it, we can briefly judge the distribution of BAC based on each category of its independent variable and so far, there were no typos or unusual values that should be noted. However, there are some that I have to point out:  
- Tequila: The distribution seems to be normal with a little bit right-skewed 
- Water: this treatment group particularly has reaction unchanged throughout the sample which is perfectly represent a placebo treatment
has no effect on BAC level 
- White wine: The distribution seems to be left-skewed 
- Mai Tai: the distribution is right-skewed 
- Reguler Beer: The distribution is right-skewed

![image](https://user-images.githubusercontent.com/108549500/198203043-796ea32a-d338-437d-a161-fa7ad737df4b.png)
![Figure_2](https://user-images.githubusercontent.com/108549500/198203368-800557c9-5748-4fa1-9e0e-f22389f2e39b.png)
![Figure_3](https://user-images.githubusercontent.com/108549500/198206205-c39c21b9-5621-432f-9978-7adfa6519c76.png)


- Linearity: Judging from the model summary, BAC and type alcohol have a relatively linear relationship despite some variance at the two ends
- Randomnese: This is one of the few conditions that can be confidently assumed due to individual involvement with the data collection process itself
- Independence: Since each treatment groups are mutually exclusive, independence can besatisfactorily assumed
- Normality: According to the Normal QQ plot, this condition is not met because from the 1st deviation going foward, the distribution is going off the normal line
- Constant Variance: From the residual and fitted, it can be seen that each treatment group’s variances are not constant

There are problems with the condition check that raises the flag that simple form of LRM might not be suitable for the data, therefore, some transformation will be needed. The 'Type of Alcohol' factor is categorical variable, so transformation would be done on BAC level exclusively. To keep the simplicity and the digestability of the project, I decide to only stick with transformation of only LRM for nor instead of others so that I can showcase its effectiveness. Tranformations I consider are: 
- logarithm of BAC+1
- 1/(BAC+1)
- Square root of BAC  

Each will be tried out and graphed to see which one is the most fitted one compared to the original model

2. Machine Learning - SLR
We will put each transformation in comparison with the simple LRM to observe any improvement. 
- First is logarithm of BAC+1 or log(BAC+1)
   
![image](https://user-images.githubusercontent.com/108549500/198208433-cda382bc-db00-4a34-99f8-86546ac6c82b.png)
![Figure_4](https://user-images.githubusercontent.com/108549500/198208660-fa7b51eb-b60c-4323-8df8-ad1c68f061af.png)  

- Square root of BAC
![image](https://user-images.githubusercontent.com/108549500/198209104-6a1b8b9e-e30e-4528-9b70-0a33244c9397.png)
![Figure_5](https://user-images.githubusercontent.com/108549500/198209278-44250446-10df-403c-a097-05b7af830650.png)


- 1/(BAC+1)
![Figure_6](https://user-images.githubusercontent.com/108549500/198209154-b2261761-a78a-4dd2-bfc9-3939af982c16.png)

