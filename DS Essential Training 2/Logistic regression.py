#!/usr/bin/env python
# coding: utf-8

# # Chapter 3 - Regression Models
# ## Segment 3- Logistic regression

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn

from pandas import Series, DataFrame
from pylab import rcParams
from sklearn import preprocessing


# In[60]:


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict

from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')


# ## Logistic regression on titanic dataset

# In[7]:


address = 'C:/Users/imran/OneDrive/Documents/GitHub/pythonLinkedIn/pythonWithLinkedIn/DS Essential Training 2/Data/titanic-training-data.csv'

titanic_training = pd.read_csv(address)
titanic_training.columns = ['PassengerId','Survived','Pclass','Name',
                                            'Sex','Age','SibSp','Parch','Ticket',
                                            'Fare','Cabin','Embarked']

titanic_training.head()


# In[8]:


# Print info about the variables

print(titanic_training.info())
# Cabin and Age has some missing values.


# ## Check that your target variable is binary

# In[9]:


sb.countplot(x='Survived', data=titanic_training, palette='hls')


# ## Checking for missing values

# In[10]:


titanic_training.isnull().sum()


# In[11]:


# Check count of rows in the dataset
titanic_training.describe()

'''Age is good for predicting survival, but has 177 missing values. How do we fill that info in?'''


# In[12]:


#Dropping columns of data that are not relevant to survival 
titanic_data = titanic_training.drop(['Name', 'Ticket', 'Cabin'], axis=1)
titanic_data.head()


# ## Imputing missing values

# In[13]:


sb.boxplot(x='Parch', y='Age', data=titanic_data, palette='hls')


# In[14]:


parch_groups = titanic_data.groupby(titanic_data['Parch'])
parch_groups.mean()


# In[22]:


def age_approx(cols):
    Age = cols[0]
    Parch=cols[1]
    
    if pd.isnull(Age):
        if Parch==0:
            return 32
        elif Parch==1:
            return 24
        elif Parch==2:
            return 17
        elif Parch==3:
            return 33
        elif Parch==4:
            return 45
        else:
            return 30
    else:
        return Age


# In[24]:


titanic_data['Age'] = titanic_data[['Age', 'Parch']].apply(age_approx, axis=1)
titanic_data.isnull().sum()


# In[26]:


#Only 2 values missing in Embarked, dropping won't affect results

titanic_data.dropna(inplace=True)
titanic_data.reset_index(inplace=True, drop=True)

print(titanic_data.info())


# ## Converting categorical variables to a dummy indicators

# In[28]:


from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
gender_cat = titanic_data['Sex']
gender_encoded = label_encoder.fit_transform(gender_cat)
gender_encoded


# In[29]:


titanic_data.head()


# In[33]:


# 1 = male, 0 = female
gender_DF= pd.DataFrame(gender_encoded, columns=['male_gender'])
gender_DF.head()


# In[37]:


embarked_cat = titanic_data['Embarked']
embarked_encoded = label_encoder.fit_transform(embarked_cat)
embarked_encoded[:100]


# In[39]:


from sklearn.preprocessing import OneHotEncoder
binary_encoder = OneHotEncoder(categories='auto')
embarked_1hot = binary_encoder.fit_transform(embarked_encoded.reshape(-1,1))
embarked_1hot_mat = embarked_1hot.toarray()
embarked_DF = pd.DataFrame(embarked_1hot_mat, columns=['C', 'Q', 'S'])
embarked_DF.head()


# In[40]:


#Dropping the categorical data and replacing it with our new binary data
titanic_data.drop(['Sex', 'Embarked'], axis=1, inplace=True)
titanic_data.head()


# In[41]:


titanic_dmy = pd.concat([titanic_data, gender_DF, embarked_DF], axis=1, verify_integrity=True).astype(float)
titanic_dmy.head()


# ## Checking for independence between features

# In[42]:


sb.heatmap(titanic_dmy.corr())


# In[43]:


titanic_dmy.drop(['Fare','Pclass'], axis=1, inplace=True)
titanic_dmy.head()


# ## Checking that dataset size is sufficient

# In[44]:


#We have 6 predictive features, 50 per feature, we will need 300 records in the dataset

titanic_dmy.info()
#We have 889 data records, enough to do logistic regression.


# In[45]:


X_train, X_test, y_train, y_test = train_test_split(titanic_dmy.drop('Survived', axis=1), 
                                                    titanic_dmy['Survived'], test_size=0.2, random_state=200)


# In[47]:


print(X_train.shape)
print(y_train.shape)


# In[48]:


X_train[:5]


# ## Deploying and evaluating the model

# In[55]:


LogReg = LogisticRegression(solver='liblinear')
LogReg.fit(X_train,y_train)


# In[56]:


y_pred=LogReg.predict(X_test)


# ## Model Evaluation
# ### Classification report without cross-validation

# In[64]:


print(sklearn.metrics.classification_report(y_test,y_pred))


# ### K-fold cross-validation & confusion matrices

# In[65]:


y_train_pred = cross_val_predict(LogReg, X_train, y_train, cv=5)
confusion_matrix(y_train, y_train_pred)


# In[66]:


precision_score(y_train, y_train_pred)


# ### Make a test prediction

# In[68]:


titanic_dmy[863:864]


# In[69]:


test_passenger = np.array(['866', '40', '0', '0', '0', '0', '0','1']).reshape(1,-1)
print(LogReg.predict(test_passenger))
print(LogReg.predict_proba(test_passenger))


# In[ ]:




