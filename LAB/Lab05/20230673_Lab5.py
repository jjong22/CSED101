#!/usr/bin/env python
# coding: utf-8

# In[97]:


word = input("Enter a sentence: ")
d = {}

for i in word:
    if i in d:
        d[i] += 1
    else : 
        d[i] = 1

print(d)


# In[ ]:




