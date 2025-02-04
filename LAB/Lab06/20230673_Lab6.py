#!/usr/bin/env python
# coding: utf-8

# In[151]:


f = open("score.txt" ,"r")
new = open("report.txt" ,"w")

mylist = f.readline()
score = ""

while (mylist):
    num, a, b = mylist.split()
    a = int(a)
    b= int(b)

    print(equ)
    if (equ >= 90 ):  
        score = "A"
    elif ( equ >= 80 ):
        score = "B"
    elif ( equ >= 70 ):
        score = "C"
    elif ( equ >= 60 ):
        score = "D"
    else :
        score = "F"
    new.write(num + " %.2f" % equ + " (%s)" % score +"\n")
    
    mylist = f.readline()

new.close()


# In[ ]:




