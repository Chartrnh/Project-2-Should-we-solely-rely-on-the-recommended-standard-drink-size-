from typing import ValuesView
import pandas as pd 

#Cleaning data
data = pd.read_csv("data.csv")
data = data.iloc[:-1, :-1]
data = data.drop(columns = ['BAC level (g/dL) after drink', 'BAC level (g/dL) 30 minutes after drink'])
data = data.rename(columns = {'BAC (mg/dl) per half an hour ': "BAC", "Type of Alcohol" : "Type"})
print(data.dtypes)
print(data.describe())
print(pd.unique(data['Type']))

#Plot 
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns
from matplotlib.ticker import PercentFormatter


for i in range(0,5):
    x = pd.unique(data['Type'])[i]
    data1 = data[data['Type']==x]
    sns.histplot(data1['BAC'], bins=6,alpha = 0.5, linewidth=0, kde=True)
   

plt.gca().yaxis.set_major_formatter(PercentFormatter(14))
plt.xlabel("Data")
plt.ylabel("Percentage of total")
plt.title("Histogram for each Type of liquor")
plt.legend(labels=['Tequila', 'White Wine', 'Regular Beer', 'Mai Tai'], loc = "upper right")
plt.show(block=False)



#LNR 
import statsmodels.api as sm 
from statsmodels.formula.api import ols 

mod = ols('BAC ~ Type', data=data).fit()
aov_table = sm.stats.anova_lm(mod, typ = 2)

#ANOVA table and summary table of linear regression model 
print(aov_table)

print(mod.summary())

# Normal QQ model and fitted model 
sm.qqplot(mod.resid, line = 's')
plt.title("Normal QQ of LR with variable BAC")
plt.show(block=False)

fig = plt.figure(figsize=(14, 8))

# creating regression plots
sm.graphics.plot_regress_exog(mod, 'Type[T.Regular Beer]', fig=fig)
plt.show(block=False)


#Log(Y+1)
data['logY'] = np.log(data['BAC'] + 1)
mod1 = ols('logY~Type', data=data).fit()
aov_table1 = sm.stats.anova_lm(mod1, typ = 2)
print(aov_table1)
print(mod1.summary())
sm.qqplot(mod1.resid, line = 's')
plt.title("Normal QQ of LR with variable log(Y+1)")
plt.show(block=False)


#sqrtY
data['sqrtY'] = np.sqrt(data['BAC'])
mod2 = ols('sqrtY~Type', data=data).fit()
aov_table2 = sm.stats.anova_lm(mod2, typ = 2)
print(aov_table2)
print(mod2.summary())
sm.qqplot(mod2.resid, line = 's')
plt.title("Normal QQ of LR with variable squared root of Y")
plt.show(block=False)


#1/(Y+1)
data['ModY'] = 1/(data['BAC'] + 1)
mod3 = ols('ModY ~ Type', data=data).fit()
aov_table3 = sm.stats.anova_lm(mod3, typ = 2)
print(aov_table3)
print(mod3.summary())
sm.qqplot(mod3.resid, line = 's')
plt.title("Normal QQ of LR with variable 1/(Y+1)")
plt.show()
