#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from scipy.spatial import distance
from sklearn import preprocessing
import time


# In[13]:


sr = pd.read_excel('SingaRaja.xlsx')


# In[14]:


sr.head()


# In[15]:


sr.tail()


# In[16]:


sr['Month'] = sr['Date'].dt.month
sr['Year'] = sr['Date'].dt.year
sr['Day'] = sr['Date'].dt.day_name()


# In[17]:


sr.columns


# In[18]:


var = ['beras']
sry1 = sr.groupby(['Year']).mean()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('rata-rata harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[37]:


var = ['beras']
sry1 = sr.groupby(['Year']).min()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('minimal harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[20]:


var = ['beras']
sry1 = sr.groupby(['Year']).max()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('maksimal harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[21]:


var = ['cabai merah']
sry1 = sr.groupby(['Year']).mean()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('rata-rata harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[29]:


var = ['cabai merah']
sry1 = sr.groupby(['Year']).min()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('minimal harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[23]:


var = ['cabai merah']
sry1 = sr.groupby(['Year']).max()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('maksimal harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[27]:


var = ['telur ayam']
sry1 = sr.groupby(['Year']).mean()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('rata-rata harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[26]:


var = ['telur ayam']
sry1 = sr.groupby(['Year']).min()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('minimal harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[30]:


var = ['telur ayam']
sry1 = sr.groupby(['Year']).max()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('maksimal harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[31]:


var = ['minyak goreng']
sry1 = sr.groupby(['Year']).mean()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('rata-rata harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[32]:


var = ['minyak goreng']
sry1 = sr.groupby(['Year']).min()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('minimal harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[33]:


var = ['minyak goreng']
sry1 = sr.groupby(['Year']).max()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('maksimal harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[34]:


var = ['gula pasir']
sry1 = sr.groupby(['Year']).mean()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('rata-rata harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[35]:


var = ['gula pasir']
sry1 = sr.groupby(['Year']).min()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('minimal harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)


# In[36]:


var = ['gula pasir']
sry1 = sr.groupby(['Year']).max()[var]
sry1.plot(marker = 's')
plt.ylabel('harga')
plt.title('maksimal harga pangan')
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.35), ncol=3)

