# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:20:45 2021

@author: Johnny Hsieh
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('eda_data.csv')

df_model = df[['avg_salary', 'Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'hourly', 'job_location', 'age', 'req_python', 'req_excel', 'req_git',
       'req_tableau', 'req_sql', 'req_tensorflow', 'req_powerbi', 'job_title_simp', 'seniority', 'desc_len']]

df_dum = pd.get_dummies(df_model)

#Split data
from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary', axis = 1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

# multiple linear regression 
import statsmodels.api as sm

X_sm = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

# LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)
np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error', cv = 3)) # NMAE = -38.378241609164945

# Lasso
lm_l = Lasso(alpha=1.9)
lm_l.fit(X_train,y_train)
np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error', cv = 3))
a = []
e = []
# 找出使 NMAE 最大的 alpha
for i in range(1, 20):
    a.append(i/10)    
    lm_l = Lasso(alpha = (i/10))
    e.append(np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error', cv = 3)))
    
plt.plot(a, e)
err = tuple(zip(a,e))
df_err = pd.DataFrame(err, columns = ['alpha','error'])
df_err[df_err.error == max(df_err.error)] # alpha = 1.9, NMAE = -28.587566

# Random Forest 
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()
rf.fit(X_train,y_train)
np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3)) #NMAE = -30.254782942806752

# Test
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = rf.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_lml)
mean_absolute_error(y_test,tpred_rf)