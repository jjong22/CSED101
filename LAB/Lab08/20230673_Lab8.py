#!/usr/bin/env python
# coding: utf-8

# In[13]:


class BankAccount:
    def __init__(self, name = "none", balance = 0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if (self.balance < amount):
            print("잔액 부족!")
        else : self.balance -= amount
            
    def get_info(self):
        print("이름:", self.name, "잔고:", self.balance)
        
    def __str__(self):
        return "이름: %s, 잔고: %d" % (self.name, self.balance)
    
    def transfer(self, other, amount):
        if(self.balance < amount):
            print("잔액 부족!")
        else : 
            self.balance -= amount
            other.balance += amount


# In[ ]:




