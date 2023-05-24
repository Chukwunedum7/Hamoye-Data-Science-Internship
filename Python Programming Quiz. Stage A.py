#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib 
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv("FoodBalanceSheets_E_Africa_NOFLAG (1).csv", encoding = "latin-1")


# In[8]:


#unique countries
df['Area'].unique()


# In[15]:


#to get the sum of processing in year 2017
df_element = df.groupby('Element')[['Y2017']].sum()
df_element


# In[29]:


df_area = df.groupby('Area')[['Y2017']].sum()
df_area


# In[28]:


df.describe() #to get the mean and standard deviation for year 2017


# In[32]:


#To get total sum of wine produced in 2015 and 2018
df_item = df.groupby('Item')[['Y2015', 'Y2018']].sum()
df_item


# In[33]:


#year with highest sum of stock variation
df_element = df.groupby('Element')[['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']].sum()
df_element


# In[ ]:




