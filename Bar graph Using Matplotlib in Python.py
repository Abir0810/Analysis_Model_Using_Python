#!/usr/bin/env python
# coding: utf-8

# # Bar graph Using Matplotlib in Python

# In[9]:


import matplotlib.pyplot as plt
labels=('python','Java','Scala','C#','PHP')
index=(1,2,3,4,5)
sizes=[45,10,15,30,22]
plt.bar(index,sizes, tick_label=labels)
plt.ylabel('Usage')
plt.xlabel('Programming Language')
plt.show()


# In[ ]:




