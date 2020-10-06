#!/usr/bin/env python
# coding: utf-8

# In[173]:


import pandas as pd
import numpy as np


# In[262]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',  
'londON_StockhOlm', 
'Budapest_PaRis', 'Brussels_londOn'], 
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
'12. Air France', '"Swiss Air"']}) 


# In[263]:


df


# In[264]:


#ANSWER 1

df['FlightNumber'].fillna({1:100055,3:10075},inplace=True)


# In[265]:


df


# In[266]:


df.dtypes


# In[287]:


df=df.astype({'FlightNumber':int})
df.dtypes


# In[268]:


#Answer2

expand=df['From_To'].str.split("_",expand=True)


# In[269]:


expand.columns=['From','To']


# In[270]:


expand


# In[271]:


#Answer 3

expand['From']=expand['From'].str.capitalize()
expand['To']=expand['To'].str.capitalize()


# In[272]:


expand


# In[273]:


#Answer4

df.drop("From_To",axis=1,inplace=True)


# In[274]:


df


# In[275]:


df[['From','TO']]=expand


# In[276]:


df


# In[277]:


#ANSWER 5

delays=df['RecentDelays'].apply(pd.Series)
delays


# In[280]:


df[['delays1','delays2','delays3']]=delays


# In[281]:


df


# In[283]:


df.drop('RecentDelays',axis=1,inplace=True)


# In[284]:


df


# In[ ]:




