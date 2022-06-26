#!/usr/bin/env python
# coding: utf-8

# # Multiple Violin Plots in Python

# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[6]:


data= sns.load_dataset("tips")
plt.figure(figsize=(10, 4))
sns.violinplot(x="day", y="total_bill",data=data)
plt.show()


# In[ ]:




