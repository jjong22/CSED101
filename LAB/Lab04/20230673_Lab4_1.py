#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 함수
def cal_average(mid, fin):
    aver = round((mid + fin) / 2, 1)
    return aver

def calc_grade(aver):
    if (aver >= 90):
        str = "A"
        return str
    elif (aver < 90 and aver >= 80):
        str = "B"
        return str
    elif (aver < 80 and aver >= 70):
        str = "C"
        return str
    elif (aver < 70 and aver >= 60):
        str = "D"
        return str
    elif (aver < 60):
        str = "F"
        return str
    
# 시작 코드       
def main():
    mid = int(input("중간고사 점수 입력: "))
    fin = int(input("기말고사 점수 입력: "))
    
    aver = cal_average(mid, fin)
    print("평균: ", aver)
    
    str = calc_grade(aver)
    print("학점: ",str)
    
main()


# In[ ]:




