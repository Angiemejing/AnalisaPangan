#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn import datasets
import matplotlib.pyplot as plt
import scipy
from scipy.spatial import distance
import seaborn as sns
from sklearn.cluster import KMeans
import time


# In[8]:


df=pd.read_excel('SingaRajaa.xlsx')


# In[9]:


c = df.corr()
c


# In[30]:


plt.scatter(df['beras'], df['telur ayam'], color = 'yellow')
plt.xlabel('beras')
plt.ylabel('telur ayam')


# In[11]:


plt.scatter(df['beras'], df['cabai merah'], color = 'blue')
plt.xlabel('beras')
plt.ylabel('cabai merah')


# In[32]:


plt.scatter(df['beras'], df['minyak goreng'], color = 'green')
plt.xlabel('beras')
plt.ylabel('minyak goreng')


# In[33]:


plt.scatter(df['beras'], df['gula pasir'], color = 'purple')
plt.xlabel('beras')
plt.ylabel('gula pasir')


# In[16]:


plt.scatter(df['telur ayam'], df['cabai merah'], color = 'pink')
plt.xlabel('telur ayam')
plt.ylabel('cabai merah')


# In[35]:


plt.scatter(df['telur ayam'], df['minyak goreng'], color = 'black')
plt.xlabel('telur ayam')
plt.ylabel('minyak goreng')


# In[36]:


plt.scatter(df['telur ayam'], df['gula pasir'], color = 'grey')
plt.xlabel('telur ayam')
plt.ylabel('gula pasir')


# In[24]:


plt.scatter(df['cabai merah'], df['minyak goreng'], color = 'green')
plt.xlabel('cabai merah')
plt.ylabel('minyak goreng')


# In[37]:


plt.scatter(df['cabai merah'], df['gula pasir'], color = 'orange')
plt.xlabel('cabai merah')
plt.ylabel('gula pasir')


# In[38]:


plt.scatter(df['minyak goreng'], df['gula pasir'], color = 'yellow')
plt.xlabel('cabai merah')
plt.ylabel('minyak goreng')


# In[ ]:




