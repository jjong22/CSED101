#!/usr/bin/env python
# coding: utf-8

# In[17]:


def bubble_sort(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist) -1 - i):
            if (mylist[j] > mylist[j+1]):
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
        print("[step %s] " % (i+1), end="")
        for num in mylist:
            print(num, end = " ")
        print()


# In[18]:


def seq_search(mylist, to_search):

    for i in range(len(mylist)):
        if (to_search == mylist[i]):
            return i
        
    return -1


# In[19]:


def sigma(a,b):
    sum = 0
    
    for i in range(a, b+1):
        sum += i
    
    print(sum)
    
def sigma_rec(a, n):
    if(n - a + 1 < 2): return a
    else: return n + sigma_rec(a, n-1)


# In[ ]:




