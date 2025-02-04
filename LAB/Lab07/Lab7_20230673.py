###############################################
# 학번: 20230673
###############################################

###############################################
#실습1 - zip() (함수 완성하기)
def problem1():
    L1 = ['one', 'two', 'three', 'four']
    L2 = [1, 2, 3, 4]
    res = {k:v for k, v in zip (L1, L2)}
    print(res)

    
###############################################
#실습2 - 가변 매개변수 (함수 완성하기)
def vector_sum(vector, *vectors):
    sum1 ,sum2 = 0, 0
    for i in vectors:
        sum1 += i[0]
    sum1 += vector[0]
    
    for i in vectors:
        sum2 += i[1]
    sum2 += vector[1]
    
    mylist = [sum1, sum2]
    return mylist

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
def merge_list(*arg):
    if arg == []:
        sum = [0]
        return sum
    else :
        sum = []
        for i in arg:
            sum += i
        sum = sorted(sum)
        return sum

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
    cnt = 0
    current = 1
    zib = set()
    while (current <= 100):
        if (current % 3 == 0 and current % 5 == 0):
            zib.add(current)
            cnt += 1
        current += 1
    print("3와 5의 공배수: %d개" % (cnt))
    print(zib)
    

###############################################
#실습5 - 집합2 (함수 완성하기)
def find_duplicates(L):
    cnt = 0
    sum = []
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] == L[j]:
                cnt += 1
        if (cnt != 1):
            sum.append(L[i])
        cnt = 0
        
    return list(set(sum))

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
    problem2() #실습2
    problem3() #실습3
    problem4() #실습4
    problem5() #실습5
