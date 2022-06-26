#!/usr/bin/env python
# coding: utf-8

# # Tree Map Using Python

# In[2]:


pip install plotly


# In[3]:





# In[13]:


import plotly.graph_objects as go
fig=go.Figure(go.Treemap(
   labels=["A","B","C","D","E","F","G","H","I"],
   parents=["","A","A","C","C","A","A","G","A"]
))
fig.show()


# In[ ]:




