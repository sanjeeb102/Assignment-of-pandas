#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing the necessary libraries
import numpy as np
import pandas as pd


# In[3]:


#importing the dataset
users = pd.read_table(r"C:\Users\sanje_crlv28m\Downloads\u.user.txt")
users = pd.read_csv(r"https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user",sep = "|", index_col = 0)
print(users)


# In[4]:


#First 10 entries
users.head(10)   


# In[6]:


#last 10 entries
users.tail(10)  


# In[7]:


#What is the number of observations in the dataset?
users.shape


# In[8]:


#Print the name of all the columns.
users.columns


# In[9]:


ncols = users.shape[1]
ncols


# In[10]:


#What is the data type of each column?
users.dtypes 


# In[11]:


#DataFrame Info?
users.info


# In[12]:


#Describe all the columns
users.describe(include='all')  


# In[ ]:




