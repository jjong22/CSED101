#!/usr/bin/env python
# coding: utf-8

# In[6]:


money = int(input("투입한 돈: "))
value = int(input("물건값: "))


print("거스름돈: ", money - value)
print("500원짜리: ", (money - value) // 500)

remain = (money - value) - ((money - value) // 500) * 500

print("100원짜리: ", remain // 100)
