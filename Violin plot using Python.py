#!/usr/bin/env python
# coding: utf-8

# # Violin plot using Python 

# In[6]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[7]:


data= sns.load_dataset("tips")
plt.figure(figsize=(10, 4))
sns.violinplot(x=data["total_bill"])
plt.show()


# In[ ]:




