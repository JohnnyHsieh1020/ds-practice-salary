# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:20:45 2021

@author: Johnny Hsieh
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing

df = pd.read_csv('dataset/eda_data.csv')
df = df.drop(columns=['Unnamed: 0', 'Job Title', 'Salary Estimate', 'Job Description',
                      'Company Name', 'Location', 'Founded', 'min_salary', 'max_salary', 'Company'], axis = 1)
df.columns
df_adjust = df[['Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 
             'job_location', 'job_title_simp', 'seniority']]
# Prepare data
for i in df_adjust:
    encode = preprocessing.LabelEncoder()
    encode.fit(df[i])
    df[i]=encode.transform(df[i])

#Split data
from sklearn.model_selection import train_test_split

X = df.drop('avg_salary', axis = 1)
y = df.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)


from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

# LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)
np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error', cv = 3)) # NMAE = -29.379934015992262

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
    
err = tuple(zip(a,e))
df_err = pd.DataFrame(err, columns = ['alpha','error'])
df_err[df_err.error == max(df_err.error)] # alpha = 1.9, NMAE = -28.615896

# Random Forest 
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()
rf.fit(X_train,y_train)
np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3)) #NMAE = -31.17034598458396

# GridsearchCV 
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)

gs.best_score_ # -29.495615183246077
gs.best_estimator_
# RandomForestRegressor(bootstrap=True, criterion='mae', max_depth=None,
#                       max_features='log2', max_leaf_nodes=None,
#                       min_impurity_decrease=0.0, min_impurity_split=None,
#                       min_samples_leaf=1, min_samples_split=2,
#                       min_weight_fraction_leaf=0.0, n_estimators=20,
#                       n_jobs=None, oob_score=False, random_state=None,
#                       verbose=0, warm_start=False)

# Test
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = rf.predict(X_test)
tpred_rf_gs = gs.best_estimator_.predict(X_test)

# Check Performance
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_lm) # MAE = 27.02746042148
mean_absolute_error(y_test,tpred_lml) # MAE = 26.112709042868868
mean_absolute_error(y_test,tpred_rf) # MAE = 31.71193576388889
mean_absolute_error(y_test,tpred_rf_gs) # MAE = 31.477864583333332
