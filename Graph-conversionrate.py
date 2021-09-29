#!/usr/bin/env python
# coding: utf-8

# # Graph analysis

# In[1]:


import pandas as pd
import plotly.express as px
import seaborn as sns


# In[2]:


# The dataset is quite big : you must create a sample of the dataset before making any visualizations !
data = pd.read_csv('conversion_data_train.csv')
data_sample = data.sample(10000)


# In[3]:


data_sample


# ### Repartition of the dataset

# In[5]:


fig = px.pie(data_frame=data_sample, color="country")
fig.show("iframe")


# In[6]:


repart_age = data_sample.groupby("age")["new_user"].count().reset_index()
repart_age = repart_age.rename(columns={'new_user': 'count'})
display(repart_age.head())
print()

fig = px.bar(data_frame=repart_age, x="age", y="count", color="age")
fig.show()


# In[7]:


repart_converted = data_sample.groupby("converted")["new_user"].count().reset_index()
repart_converted = repart_converted.rename(columns={'new_user': 'count'})
display(repart_converted.head())
print()

fig = px.bar(data_frame=repart_converted, x="converted", y="count", color="converted")
fig.show()


# In[8]:


fig = px.pie(data_frame=data_sample, values="country")
fig.show("iframe")


# In[9]:


fig = px.pie(data_frame=data_sample, values="source")
fig.show("iframe")


# In[10]:


total_pages_visited_per_converted = data_sample.groupby("converted")["total_pages_visited"].mean().reset_index()
display(total_pages_visited_per_converted.head())
print()

fig = px.bar(data_frame=total_pages_visited_per_converted, x="converted", y="total_pages_visited", color="total_pages_visited")
fig.show()


# In[11]:


age_per_converted = data_sample.groupby("converted")["age"].mean().reset_index()
display(age_per_converted.head())
print()

fig = px.bar(data_frame=age_per_converted, x="converted", y="age", color="age")
fig.show()


# In[12]:


new_user_converted = data_sample.groupby("converted")["new_user"].mean().reset_index()
display(new_user_converted.head())
print()

fig = px.bar(data_frame=new_user_converted, x="converted", y="new_user", color="new_user")
fig.show()


# In[16]:


data_converted_by_country = data_converted.groupby("country")["converted"].count().reset_index()
data_converted_by_country = data_converted_by_country.rename(columns={'converted': 'count'})
display(data_converted_by_country.head())
print()

fig = px.bar(data_frame=data_converted_by_country, x="country", y="count", color="country")
fig.show()


# In[18]:


data_no_converted_by_country = data_no_converted.groupby("country")["converted"].count().reset_index()
data_no_converted_by_country = data_no_converted_by_country.rename(columns={'converted': 'count'})
display(data_no_converted_by_country.head())
print()

fig = px.bar(data_frame=data_no_converted_by_country, x="country", y="count", color="country")
fig.show()


# In[ ]:




