#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import plotly.express as px  
import plotly.io as pio


# In[2]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv("cholera.csv")


# In[4]:


data.head()


# In[5]:


data.describe()


# In[6]:


## checking for more information about the dataset
data.info()


# In[7]:


## checking for null values
data.isnull().sum()


# In[ ]:


## changing the names of some columns
## cause they are too long



# In[9]:


# Rename the columns
new_column_names = {
    'Number of reported cases of cholera': 'cases',
    'Number of reported deaths from cholera': 'deaths',
    'Cholera case fatality rate': 'fatality_rate',
    'WHO Region': 'region'
}
data = data.rename(columns=new_column_names)


# In[10]:


data.head()


# In[12]:


## checking for the latest and earliest year 
data['Year'].max()


# In[13]:


data['Year'].min()


# In[14]:


## converting cases and deaths to intergers
data['cases'].unique()


# In[15]:


## removing spaces inbetween numbers in the cases column
data['cases'] = data['cases'].str.replace(' ', '')


# In[18]:


## find the median of cases
median = data['cases'].median()
median


# In[19]:


## filling the nan values of cases with the median
data['cases'] = data['cases'].fillna(median)


# In[20]:


# Convert the column to integers
data['cases'] = data['cases'].astype(int)


# In[22]:


data['deaths'].unique()


# In[27]:


# make unknown show as nan value
# Replace 'unknown' with NaN
data['deaths'] = data['deaths'].replace('Unknown', np.nan)


# In[26]:


## removing spaces
data['deaths'] = data['deaths'].str.replace(' ', '')


# In[28]:


d_median = data['deaths'].median()
d_median


# In[29]:


## filling nan values with the median
data['deaths'] = data['deaths'].fillna(d_median)


# In[30]:


## converting to interger
data['deaths'] = data['deaths'].astype(int)


# In[31]:


data['fatality_rate'].unique()


# In[32]:


# Replace 'unknown' with NaN
data['fatality_rate'] = data['fatality_rate'].replace('Unknown', np.nan)


# In[33]:


data['fatality_rate'] = data['fatality_rate'].str.replace('0.0 0.0', '0')


# In[34]:


# median of fatality rate
f_median = data['fatality_rate'].median()
f_median


# In[35]:


## filling the nan values with nan
data['fatality_rate'] = data['fatality_rate'].fillna(f_median)


# In[36]:


## converting to float
data['fatality_rate'] = data['fatality_rate'].astype(float)


# In[37]:


data.info()


# In[38]:


## checking for unique regions
data['region'].unique()


# In[39]:


# number cases over the years
fig = px.histogram(data, x="Year", title='Cases over the Years', y="cases")
fig.show()


# In[40]:


# number of deaths over the years
fig = px.histogram(data, x="Year", title='Deaths over the Years', color_discrete_sequence=['red'], y="deaths")
fig.show()


# In[41]:


## region with highest cases
fig = px.histogram(data, x="region", title = "Region with the highest Cases", y="cases")
fig.show()


# In[42]:


## region with the highest deaths
fig = px.histogram(data, x="region", title = "Region with the highest Deaths", color_discrete_sequence=['red'], y="deaths")
fig.show()


# In[43]:


## Region with the highest fatality rate
fig = px.histogram(data, x="region", title = "Region with the highest Fatality Rate", y="fatality_rate")
fig.show()


# In[ ]:




