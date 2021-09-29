#!/usr/bin/env python
# coding: utf-8

# <img src="data:image/png;base64,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" alt="DSW LOGO" />

# # Import libraries

# In[1]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.svm import SVC
from sklearn.ensemble import StackingClassifier, VotingClassifier
from xgboost import XGBClassifier
import xgboost as xgb


from sklearn.metrics import f1_score, confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
# setting Jedha color palette as default
pio.templates["jedha"] = go.layout.Template(
    layout_colorway=["#4B9AC7", "#4BE8E0", "#9DD4F3", "#97FBF6", "#2A7FAF", "#23B1AB", "#0E3449", "#015955"]
)
pio.templates.default = "jedha"
pio.renderers.default = "svg" # to be replaced by "iframe" if working on JULIE
from IPython.display import display


# # Read file with labels

# In[2]:


data = pd.read_csv('conversion_data_train.csv')
print('Set with labels (our train+test) :', data.shape)


# In[3]:


data.head()


# # Explore dataset

# In[4]:


data.info()


# In[5]:


data.describe()


# # Machine learnin - Preprocessing

# In[6]:


#Separate X Y
Y = data.loc[:,"converted"]
X = data.loc[:, data.columns !="converted"]
print('Explanatory variables : ', X.columns)
print()
print("...Done.")
print(Y.head())
print()
print(X.head())
print()


# In[7]:


# Divide dataset Train set & Test set 
print("Dividing into train and test sets...")
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=0)
print("...Done.")
print()


# In[8]:


# Convert pandas DataFrames to numpy arrays before using scikit-learn
print("Convert pandas DataFrames to numpy arrays...")
X_train = X_train.values
X_test = X_test.values
Y_train = Y_train.values
Y_test = Y_test.values
print("...Done")

print(X_train[0:5,:])
print(X_test[0:2,:])
print()
print(Y_train[0:5])
print(Y_test[0:2])


# ### Pipeline

# In[9]:


# Create pipeline for numeric features
numeric_features = [4] # Positions of numeric columns in X_train/X_test
numeric_transformer = StandardScaler(with_mean=False)


# In[10]:


# Create pipeline for categorical features
categorical_features = [0,1,2,3]
categorical_transformer = OneHotEncoder(categories=[data.iloc[:, col].unique() for col in categorical_features])


# In[11]:


# Use ColumnTransformer to make a preprocessor object that describes all the treatments to be done
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])


# In[12]:


# Preprocessings on train set
print("Performing preprocessings on train set...")
print(X_train[0:5])
X_train = preprocessor.fit_transform(X_train)
print('...Done.')
print(X_train[0:5])
print()

# Preprocessings on test set
print("Performing preprocessings on test set...")
print(X_test[0:5])
X_test = preprocessor.transform(X_test) 
print('...Done.')
print(X_test[0:5])
print()


# # Machine learning - Model

# In[13]:


model_reg = LogisticRegression()

model_gridsearch_reg = GridSearchCV(estimator=LogisticRegression(), 
                                     param_grid= {"penalty":["l1","l2"],
                                                  "C":np.logspace(-4, 4, 20),
                                                  "solver" :['liblinear']},
                                     cv = 3, verbose=1)


model_gridsearch_dtc =  GridSearchCV(estimator=DecisionTreeClassifier(), 
                                     param_grid= {'max_depth' : np.arange(1,10,2),
                                                  'min_samples_split' : [2, 10, 20],
                                                  "criterion":["gini","entropy"]},
                                     cv = 3, verbose=1)

model_gridsearch_rfc = GridSearchCV(RandomForestClassifier(), 
                                    param_grid ={'max_depth': np.arange(1,10,2),
                                                 'min_samples_leaf': [1, 2, 5],
                                                 'min_samples_split': [2, 4, 8],
                                                 'n_estimators': [10, 20, 40]}, 
                                    cv = 3, verbose=1)

model_xgb = xgb.XGBClassifier(random_state=1,learning_rate=0.01)


# In[14]:


model_reg.fit(X_train,Y_train)


# In[15]:


model_gridsearch_reg.fit(X_train,Y_train)


# In[16]:


model_gridsearch_dtc.fit(X_train,Y_train)


# In[17]:


model_gridsearch_rfc.fit(X_train,Y_train)


# In[18]:


model_xgb.fit(X_train,Y_train)


# In[19]:


# Predictions on training set
Y_train_pred_reg = model_reg.predict(X_train)
Y_train_pred_cv_reg = model_gridsearch_reg.predict(X_train)
Y_train_pred_dtc = model_gridsearch_dtc.predict(X_train)
Y_train_pred_rfc = model_gridsearch_rfc.predict(X_train)
Y_train_pred_xgb = model_xgb.predict(X_train)
print("...Done.")
print(Y_train_pred_reg)
print(Y_train_pred_cv_reg)
print(Y_train_pred_dtc)
print(Y_train_pred_rfc)
print(Y_train_pred_xgb)
print()

# Predictions on test set
Y_test_pred_reg = model_reg.predict(X_test)
Y_test_pred_cv_reg = model_gridsearch_reg.predict(X_test)
Y_test_pred_dtc = model_gridsearch_dtc.predict(X_test)
Y_test_pred_rfc = model_gridsearch_rfc.predict(X_test)
Y_test_pred_xgb = model_xgb.predict(X_test)
print("...Done.")
print(Y_test_pred_reg)
print(Y_test_pred_cv_reg)
print(Y_test_pred_dtc)
print(Y_test_pred_rfc)
print(Y_test_pred_xgb)
print()


# In[20]:


# Print scores

f1score_training_reg =f1_score(Y_train, Y_train_pred_reg)
f1score_test_reg = f1_score(Y_test, Y_test_pred_reg)

f1score_training_cv_reg =f1_score(Y_train, Y_train_pred_cv_reg)
f1score_test_cv_reg = f1_score(Y_test, Y_test_pred_cv_reg)

f1score_training_dtc =f1_score(Y_train, Y_train_pred_dtc)
f1score_test_dtc = f1_score(Y_test, Y_test_pred_dtc)

f1score_training_rfc =f1_score(Y_train, Y_train_pred_rfc)
f1score_test_rfc= f1_score(Y_test, Y_test_pred_rfc)

f1score_training_xgb =f1_score(Y_train, Y_train_pred_xgb)
f1score_test_xgb = f1_score(Y_test, Y_test_pred_xgb)

score = {"Model":["Logistic Regression", "Logistic Regression GsCV", "Decision Tree", "Random Forest", "XGBoost"], 
        "F1-score on training set" : [f1score_training_reg, f1score_training_cv_reg, f1score_training_dtc, f1score_training_rfc, f1score_training_xgb],
         "F1-score on test set" : [f1score_test_reg, f1score_test_cv_reg, f1score_test_dtc, f1score_test_rfc, f1score_test_xgb]}

score = pd.DataFrame(score)
score


# - Confusion matrix

# In[21]:


#Confusion matrix Test

cm2 = confusion_matrix(Y_test, Y_test_pred_reg)
sns.heatmap(cm2, annot=True, fmt="d")

# labels, title and ticks
ax= plt.subplot(1,2,2)
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix'); 


# In[22]:


#Confusion matrix Train

cm1 = confusion_matrix(Y_train, Y_train_pred_cv_reg)
sns.heatmap(cm1, annot=True, fmt="d")

# labels, title and ticks
ax= plt.subplot()
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix Train Logistic Regression'); 


# In[23]:


#Confusion matrix Test

cm2 = confusion_matrix(Y_test, Y_test_pred_cv_reg)
sns.heatmap(cm2, annot=True, fmt="d")

# labels, title and ticks
ax= plt.subplot()
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix Test Logistic Regression'); 


# In[24]:


#Confusion matrix Train

cm1 = confusion_matrix(Y_train, Y_train_pred_dtc)
sns.heatmap(cm1, annot=True, fmt="d")

# labels, title and ticks
ax= plt.subplot()
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix Train Decision Tree'); 


# In[25]:


#Confusion matrix Test

cm2 = confusion_matrix(Y_test, Y_test_pred_dtc)
sns.heatmap(cm2, annot=True, fmt="d")

# labels, title and ticks
ax= plt.subplot()
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix Test Decision Tree'); 


# In[26]:


#Confusion matrix Train

cm1 = confusion_matrix(Y_train, Y_train_pred_xgb)
sns.heatmap(cm1, annot=True, fmt="d")

# labels, title and ticks
ax= plt.subplot()
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix Train XGBoost'); 


# In[27]:


#Confusion matrix Test

cm2 = confusion_matrix(Y_test, Y_test_pred_xgb)
sns.heatmap(cm2, annot=True, fmt="d")

# labels, title and ticks
ax= plt.subplot()
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix Test XGBoost'); 

