#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import plotly.express as px  
import plotly.io as pio


# In[4]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


data_1 = pd.read_csv("Africa Food Production (2004 - 2013).csv")


# In[6]:


data_2 = pd.read_csv("Africa Food Supply (2004 - 2013).csv")


# In[7]:


data_1.head()


# In[8]:


data_2.head()


# In[9]:


data_1.describe()


# In[10]:


data_2.describe()


# In[9]:


data_1['Item'].unique()


# In[11]:


#merge datasets from food production and food supply
merged_df = pd.merge(data_1, data_2, on=['Country', 'Year'])


# In[12]:


data_1 = data_1.rename(columns={'Value': 'Production Value'})
data_2 = data_2.rename(columns={'Value': 'Supply Value'})


# In[13]:


data_1['Country'].unique()


# In[14]:


data_2['Country'].unique()


# In[15]:


#adding kilotons unit to the heading of the values columns
data_1 = data_1.rename(columns={'Production Value':'Production Value (Kt)' })
data_2 = data_2.rename(columns={'Supply Value':'Supply Value (Kt)'})


# In[16]:


# Merge datasets from food production and food supply
merged_df = pd.merge(data_1, data_2, on=['Country', 'Year'])


# In[22]:


# Group the data by country and calculate the total production value
country_production = data_1.groupby('Country')['Production Value (Kt)'].sum().reset_index()
top_10_countries = country_production.nlargest(10, 'Production Value (Kt)')


# In[23]:


# Create a bar plot to visualize the top 10 countries with the highest production over the years
fig = px.bar(top_10_countries, x='Country', y='Production Value (Kt)', title='Top 10 Countries with Highest Production')
fig.show()


# In[41]:


# Calculate the difference between production and supply values
merged_df['Shortage'] = merged_df['Production Value (Kt)'] - merged_df['Supply Value (Kt)']


# In[43]:


# Calculate the total production value by year
yearly_production = data_1.groupby('Year')['Production Value (Kt)'].sum().reset_index()



# In[28]:


# line plot to visualize the production trend over the years
fig = px.line(yearly_production, x='Year', y='Production Value (Kt)', title='Food Production by Year')
fig.show()


# In[34]:


# Calculate he total production value for each item
item_production = data_1.groupby('Item')['Production Value (Kt)'].sum().reset_index()


# In[35]:


# items by production value in descending order
top_10_production = item_production.nlargest(10, 'Production Value (Kt)')


# In[37]:


# bar plot for the top 10 items produced
fig = px.bar(top_10_production, x='Production Value (Kt)', y='Item', orientation='h', title='Top 10 Items Produced')
fig.show()


# In[40]:


country_supply = data_2.groupby('Country')['Supply Value (Kt)'].sum().reset_index()
top_10_countries = country_supply.nlargest(10, 'Supply Value (Kt)')


# In[109]:


# Calculate the total supply value by year
yearly_supply = data_2.groupby('Year')['Supply Value (Kt)'].sum().reset_index()

# line plot to visualize the supply trend over the years
fig = px.line(yearly_supply, x='Year', y='Supply Value (Kt)', title='Food Supply by Year')
fig.show()


# In[81]:


# total production by country
production_by_country = data_1.groupby('Country')['Production Value (Kt)'].sum().reset_index()

# Visualization of the production by country
fig = px.bar(production_by_country, x='Country', y='Production Value (Kt)', title='Food Production by Country')
fig.show()


# In[80]:


# total supply by country
supply_by_country = data_2.groupby('Country')['Supply Value (Kt)'].sum().reset_index()

# visualisation of the supply by country
fig = px.bar(supply_by_country, x='Country', y='Supply Value (Kt)', title='Food Supply by Country')
fig.show()


# In[86]:


nigeria_production = data_1[data_1['Country'] == 'Nigeria']

# total production per year in Nigeria
production_trends = nigeria_production.groupby('Year')['Production Value (Kt)'].sum().reset_index()

# Visualization of the production trends in Nigeria
fig = px.line(production_trends, x='Year', y='Production Value (Kt)', title='Food Production Trends in Nigeria')
fig.show()


# In[88]:


nigeria_supply = data_2[data_2['Country'] == 'Nigeria']

# total supply per year in Nigeria
supply_trends = nigeria_supply.groupby('Year')['Supply Value (Kt)'].sum().reset_index()

# Visualization of the supply trends in Nigeria
fig = px.line(supply_trends, x='Year', y='Supply Value (Kt)', title='Food Supply Trends in Nigeria')
fig.show()


# In[102]:


production_by_item_nigeria = nigeria_production.groupby('Item')['Production Value 9'].sum().reset_index()

# Sorting the items by production value
production_by_item_nigeria = production_by_item_nigeria.sort_values('Production Value (Kt)', ascending=False)

# Visualization of the production by item in Nigeria
fig = px.bar(production_by_item_nigeria, x='Item', y='Production Value (Kt)', title='Food Production by Item in Nigeria')
fig.show()

