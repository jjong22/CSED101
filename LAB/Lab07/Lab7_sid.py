###############################################
# 학번: xxxxxxxx
###############################################

###############################################
#실습1 - zip() (함수 완성하기)
def problem1():
    L1 = ['one', 'two', 'three', 'four']
    L2 = [1, 2, 3, 4]

    
###############################################
#실습2 - 가변 매개변수 (함수 완성하기)
def vector_sum(vector, *vectors):
    pass

def problem2(): 
    v1=[0, 1]
    v2=[0.5, 0.5]
    v3=[1, 0]
    v4=[6, 4]
    v5=[3.13, 2.72]
    m1 = vector_sum(v1, v2, v3)
    m2 = vector_sum(v1, v2, v3, v4)
    m3 = vector_sum(v3, v5)
    print(m1,m2,m3)

    
###############################################
#실습3 - 디폴트  매개변수 (함수 완성하기)
def merge_list():
    pass

def problem3():
    l = [3, 5, 9, 1, 2]
    ml1 = merge_list(l,[2,1])
    ml2 = merge_list([6,9,4])
    ml3 = merge_list()
    print(ml1) # [1, 1, 2, 2, 3, 5, 9]
    print(ml2) # [0, 4, 6, 9] 
    print(ml3) # [0, 0]


###############################################
#실습4 - 집합1 (함수 완성하기)
def problem4():
    pass
    

###############################################
#실습5 - 집합2 (함수 완성하기)
def find_duplicates(L):
    pass

def problem5():
    l1 = [1, 2, 3, 2, 5, 5, 5, 6]
    l2 = [1, 3, 4]

    dl1 = find_duplicates(l1)
    dl2 = find_duplicates(l2)
    dl3 = find_duplicates(l1 + l2)

    print(dl1) # [2, 5]
    print(dl2) # []
    print(dl3) # [1, 2, 3, 5]


###############################################
if __name__ == "__main__":
    problem1() #실습1
    #problem2() #실습2
    #problem3() #실습3
    #problem4() #실습4
    #problem5() #실습5
