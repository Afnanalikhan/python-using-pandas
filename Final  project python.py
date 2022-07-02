#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np


# In[9]:


df = pd.read_csv("ds_salaries.csv")


# In[10]:


df


# In[11]:


df.head(8)


# In[12]:


df.tail(8)


# In[15]:


df.shape


# In[16]:


#viewing the data

print(df.info())


# In[17]:


df.info


# In[18]:


df.describe()


# In[19]:


df.nunique()


# In[20]:


df.corr()


# In[23]:


df.columns


# # Data cleaning

# In[29]:


#Finding number of nan or missing values in all columns

print(df.isna().sum(axis = 0))

#nan value in every column


# In[31]:


print(df.isna().sum(axis = 1))

# this function will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame
# In[33]:


df.dropna(inplace = True)
print(df.to_string())


# # Replace Empty value

# In[34]:


df.fillna(2, inplace = True)


# In[36]:


df


# In[37]:


df.notnull()


# In[38]:


df.isnull()


# In[39]:


# if cells is duplicated they will say yes

print(df.duplicated())


# In[42]:


# Removing duplicate

df.drop_duplicates(inplace = True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




