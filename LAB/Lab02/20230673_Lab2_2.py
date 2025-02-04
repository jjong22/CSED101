#!/usr/bin/env python
# coding: utf-8

# In[2]:


time = input("날짜(연/월/일) 입력:")
year, month, day = time.split("/")
year = int(year)
month = int(month)
day = int(day)

print("입력한 날짜의 10년 후는",year+10,"년",month, "월",day, "일")


# In[ ]:




