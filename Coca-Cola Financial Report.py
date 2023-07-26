#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import plotly.express as px  
import plotly.io as pio
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("cocacola_financial_report.csv")


# In[3]:


data.head()


# In[4]:


data.describe()


# In[5]:


data = {
    'Year': [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009],
    'Revenues': [37266, 34300, 36212, 41863, 44294, 45998, 46854, 48017, 46542, 35119, 30990],
    'Cost of Goods and Services Sold': [14619, 13067, 13721, 16465, 17482, 17889, 18421, 19053, 18215, 12693, 11088],
    'GROSS PROFIT': [22647, 21233, 22491, 25398, 26812, 28109, 28433, 28964, 28327, 22426, 19902],
    'Selling, General and Administrative Expense': [12103, 11002, 12834, 15262, 16427, 17218, 17310, 17738, 17422, 13158, 11358],
    'Other Cost and Expense, Operating': [458, 1079, 1902, 1510, 1657, 1183, 895, 447, 732, 819, 313],
    'OPERATING INCOME': [10086, 9152, 7755, 8626, 8728, 9708, 10228, 10779, 10173, 8449, 8231],
    'Interest income': [563, 689, 679, 642, 613, 594, 534, 471, 483, 317, 249],
    'Interest expense': [946, 950, 853, 733, 856, 483, 463, 397, 417, 733, 355],
    'Equity income (loss) - net': [1049, 1008, 1072, 835, 489, 769, 602, 819, 690, 1025, 781],
    'Other income (loss) - net': [34, -1674, -1763, -1234, 631, -1263, 576, 137, 529, 5185, 40],
    'INCOME BEFORE INCOME TAXES': [10786, 8225, 6890, 8136, 9605, 9325, 11477, 11809, 11458, 14243, 8946],
    'Income taxes': [1801, 1749, 5607, 1586, 2239, 2201, 2851, 2723, 2812, 2384, 2040],
    'CONSOLIDATED NET INCOME': [8985, 6476, 1283, 6550, 7366, 7124, 8626, 9086, 8646, 11859, 6906],
    'Net Income (Loss) Attributable to Noncontrolling Interest': [65, 42, 35, 23, 15, 26, 42, 67, 62, 50, 82],
    'NET INCOME ATTRIBUTABLE TO SHAREOWNERS OF THE COCA-COLA COMPANY': [8920, 6434, 1248, 6527, 7351, 7098, 8584, 9019, 8584, 11809, 6824],
    'BASIC NET INCOME PER SHARE (in dollars per share)': [2.09, 1.51, 0.29, 1.51, 1.69, 1.62, 1.94, 2, 1.88, 5.12, 2.95],
    'DILUTED NET INCOME PER SHARE (in dollars per share)': [2.07, 1.5, 0.29, 1.49, 1.67, 1.6, 1.9, 1.97, 1.85, 5.06, 2.93],
    'AVERAGE SHARES OUTSTANDING (in shares)': [4276, 4259, 4272, 4317, 4352, 4387, 4434, 4504, 4568, 2308, 2314],
    'Effect of dilutive securities (in shares)': [38, 40, 52, 50, 53, 63, 75, 80, 78, 25, 15],
    'AVERAGE SHARES OUTSTANDING ASSUMING DILUTION (in shares)': [4314, 4299, 4324, 4367, 4405, 4450, 4509, 4584, 4646, 2333, 2329]
}

data = pd.DataFrame(data)

data.columns = data.columns.str.strip()


# In[7]:


# Line plot showing the revenues over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Year', y='Revenues')
plt.title('Revenues Over the Years')
plt.xlabel('Year')
plt.ylabel('Revenues (in Millions USD)')
plt.xticks(rotation=45)
plt.show()


# In[8]:


# Bar plot showing gross profit and operating income over the years
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='Year', y='GROSS PROFIT', label='Gross Profit')
sns.barplot(data=data, x='Year', y='OPERATING INCOME', label='Operating Income')
plt.title('Gross Profit vs. Operating Income Over the Years')
plt.xlabel('Year')
plt.ylabel('Amount (in Millions USD)')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# In[9]:


# Bar plot showing cost of goods and services sold, selling, general and administrative expense, and other cost and expense, operating over the years
plt.figure(figsize=(12, 6))
sns.barplot(data=data, x='Year', y='Cost of Goods and Services Sold', label='Cost of Goods Sold')
sns.barplot(data=data, x='Year', y='Selling, General and Administrative Expense', label='SG&A Expense')
sns.barplot(data=data, x='Year', y='Other Cost and Expense, Operating', label='Other Cost and Expense')
plt.title('Costs and Expenses Over the Years')
plt.xlabel('Year')
plt.ylabel('Amount (in Millions USD)')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# In[11]:


# Line plot shpowing interest income, interest expense, equity income (loss) - net, and other income (loss) - net over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Year', y='Interest income', label='Interest Income')
sns.lineplot(data=data, x='Year', y='Interest expense', label='Interest Expense')
sns.lineplot(data=data, x='Year', y='Equity income (loss) - net', label='Equity Income (Loss)')
sns.lineplot(data=data, x='Year', y='Other income (loss) - net', label='Other Income (Loss)')
plt.title('Income and Expenses Over the Years')
plt.xlabel('Year')
plt.ylabel('Amount (in Millions USD)')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# In[12]:


# Line plot showing income before income taxes and consolidated net income over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Year', y='INCOME BEFORE INCOME TAXES', label='Income Before Income Taxes')
sns.lineplot(data=data, x='Year', y='CONSOLIDATED NET INCOME', label='Consolidated Net Income')
plt.title('Income Before Income Taxes vs. Consolidated Net Income Over the Years')
plt.xlabel('Year')
plt.ylabel('Amount (in Millions USD)')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# In[13]:


# Bar plot shpwing net income (Loss) attributable to noncontrolling interest and net income attributable to shareowners over the years
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='Year', y='Net Income (Loss) Attributable to Noncontrolling Interest', label='Noncontrolling Interest')
sns.barplot(data=data, x='Year', y='NET INCOME ATTRIBUTABLE TO SHAREOWNERS OF THE COCA-COLA COMPANY', label='Shareowners')
plt.title('Net Income Attributable to Noncontrolling Interest vs. Shareowners Over the Years')
plt.xlabel('Year')
plt.ylabel('Amount (in Millions USD)')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# In[14]:


# Line plot for Basic Net Income Per Share and Diluted Net Income Per Share over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='Year', y='BASIC NET INCOME PER SHARE (in dollars per share)', label='Basic EPS')
sns.lineplot(data=data, x='Year', y='DILUTED NET INCOME PER SHARE (in dollars per share)', label='Diluted EPS')
plt.title('Basic Net Income Per Share vs. Diluted Net Income Per Share Over the Years')
plt.xlabel('Year')
plt.ylabel('EPS (in dollars per share)')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# In[ ]:




