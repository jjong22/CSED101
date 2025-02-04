import random
import os 
from IPython.display import clear_output
import sys

def clear_screen(): # 화면을 clear합니다. 윈도우 환경에서 실행했습니다.
	os.system('cls') # Windows 콘솔 창에서 실행 시 주석 해제
	# os.system('clear') # Linux 콘솔 창에서 실행 시 주석 해제 
	# clear_output() # jupyter notebook 외 실행 시 주석 처리할 것
	return 0
# 딱히 사용하진 않았습니다..

def random_dice(): # 컴퓨터나 유저의 랜덤한 다이스를 리턴
    dice = []
    for i in range(5):
        dice.append(random.randrange(1,7)) # 1~6 사이의 정수를 선택합니다. 이를 5번 반복해 리스트로 리턴합니다.
    return dice

def pause(upper_game_index, upper_game_index_score, lower_game_index, lower_game_index_score): # 동작을 정지하는 함수입니다.
    print()
    print("Game paused. Enter the filename to save:")
    name_to_save = input()
    
    save_list = [] # 저장할 값이 들어갑니다.
    
    for i in range(6): # 1 ~ 6의 경우입니다.
        if (upper_game_index[1][i] == 0 and upper_game_index[2][i] == 0): # 유저와 컴퓨터 모두 기록하지 않았을 때
            save_list.append("%s: x x\n" % (upper_game_index[0][i]))
        elif (upper_game_index[1][i] == 1 and upper_game_index[2][i] == 0): # 유저만 기록했을 때
            save_list.append("%s: %d x\n" % (upper_game_index[0][i], upper_game_index_score[0][i]))
        elif (upper_game_index[1][i] == 0 and upper_game_index[2][i] == 1): # 컴퓨터만 기록했을 때
            save_list.append("%s: x %d\n" % (upper_game_index[0][i], upper_game_index_score[1][i]))
        elif (upper_game_index[1][i] == 1 and upper_game_index[2][i] == 1): # 유저와 컴퓨터 모두 기록했을 때
            save_list.append("%s: %d %d\n" % (upper_game_index[0][i], upper_game_index_score[0][i], upper_game_index_score[1][i]))
    
    for i in range(6): # C 부터 Yacht 까지의 경우입니다.
        
        if (i == 5): # Yacht 인 경우에는 파일에 "Y"의 형태로 씁니다.
            if (lower_game_index[1][i] == 0 and lower_game_index[2][i] == 0): # 유저와 컴퓨터 모두 기록하지 않았을 때
                save_list.append("%s: x x\n" % ("Y"))
            elif (lower_game_index[1][i] == 1 and lower_game_index[2][i] == 0): # 유저만 기록했을 때
                save_list.append("%s: %d x\n" % ("Y", lower_game_index_score[0][i]))
            elif (lower_game_index[1][i] == 0 and lower_game_index[2][i] == 1): # 컴퓨터만 기록했을 때
                save_list.append("%s: x %d\n" % ("Y", lower_game_index_score[1][i]))
            elif (lower_game_index[1][i] == 1 and lower_game_index[2][i] == 1): # 유저와 컴퓨터 모두 기록했을 때
                save_list.append("%s: %d %d\n" % ("Y", lower_game_index_score[0][i], lower_game_index_score[1][i]))
            
        else : 
            if (lower_game_index[1][i] == 0 and lower_game_index[2][i] == 0): # 유저와 컴퓨터 모두 기록하지 않았을 때
                save_list.append("%s: x x\n" % (lower_game_index[0][i]))
            elif (lower_game_index[1][i] == 1 and lower_game_index[2][i] == 0): # 유저만 기록했을 때
                save_list.append("%s: %d x\n" % (lower_game_index[0][i], lower_game_index_score[0][i]))
            elif (lower_game_index[1][i] == 0 and lower_game_index[2][i] == 1): # 컴퓨터만 기록했을 때
                save_list.append("%s: x %d\n" % (lower_game_index[0][i], lower_game_index_score[1][i]))
            elif (lower_game_index[1][i] == 1 and lower_game_index[2][i] == 1): # 유저와 컴퓨터 모두 기록했을 때
                save_list.append("%s: %d %d\n" % (lower_game_index[0][i], lower_game_index_score[0][i], lower_game_index_score[1][i]))
        
    
    f = open(name_to_save, "w") # 파일을 씁니다.
    for line in save_list:
        f.write(line)
        
    f.close()
    
    print("file saved.")
    print()
    
    start()
    

def check_error(file_list): # 파일을 열 때, 가능한지 판단하고, 그 파일을 카테고리에 따라 분류해주는 함수입니다.
    
    if (len(file_list) != 12) : return False # 12줄이 아니면 불가능합니다.
        
    upper_list = [[],[],[],[],[],[]] # 숫자가 가능한 지 판단하기 위해 담는 리스트입니다.
    lower_list = [[],[],[],[],[],[]]
    
    for index in range(0, 12, 1):
        in_word = []
        in_word = file_list[index].split()
        
        try : 
            try_num1 = float(in_word[1])
            if ( try_num1.is_integer() == False) : return False # 즉, 소수 일 때 불가능
        except: pass
        
        try : 
            try_num2 = float(in_word[2])
            if ( try_num2.is_integer() == False) : return False # 즉, 소수 일 때 불가능
        except: pass
        
        if (in_word[0] == "1:"):
            if (in_word[1] != "x"): upper_list[0].append(int(in_word[1])) # 유저
            else : upper_list[0].append("x")
            if (in_word[2] != "x"): upper_list[0].append(int(in_word[2])) # 컴퓨터
            else : upper_list[0].append("x")
            
        elif (in_word[0] == "2:"):
            if (in_word[1] != "x"): upper_list[1].append(int(in_word[1])) # 유저
            else : upper_list[1].append("x")
            if (in_word[2] != "x"): upper_list[1].append(int(in_word[2])) # 컴퓨터
            else : upper_list[1].append("x")
            
        elif (in_word[0] == "3:"):
            if (in_word[1] != "x"): upper_list[2].append(int(in_word[1])) # 유저
            else : upper_list[2].append("x")
            if (in_word[2] != "x"): upper_list[2].append(int(in_word[2])) # 컴퓨터
            else : upper_list[2].append("x")
            
        elif (in_word[0] == "4:"):
            if (in_word[1] != "x"): upper_list[3].append(int(in_word[1])) # 유저
            else : upper_list[3].append("x")
            if (in_word[2] != "x"): upper_list[3].append(int(in_word[2])) # 컴퓨터
            else : upper_list[3].append("x")
            
        elif (in_word[0] == "5:"):
            if (in_word[1] != "x"): upper_list[4].append(int(in_word[1])) # 유저
            else : upper_list[4].append("x")
            if (in_word[2] != "x"): upper_list[4].append(int(in_word[2])) # 컴퓨터
            else : upper_list[4].append("x")
            
        elif (in_word[0] == "6:"):
            if (in_word[1] != "x"): upper_list[5].append(int(in_word[1])) # 유저
            else : upper_list[5].append("x")
            if (in_word[2] != "x"): upper_list[5].append(int(in_word[2])) # 컴퓨터
            else : upper_list[5].append("x")
            
        elif (in_word[0] == "C:"):
            if (in_word[1] != "x"): lower_list[0].append(int(in_word[1])) # 유저
            else : lower_list[0].append("x")
            if (in_word[2] != "x"): lower_list[0].append(int(in_word[2])) # 컴퓨터
            else : lower_list[0].append("x")
            
        elif (in_word[0] == "4K:" ):
            if (in_word[1] != "x"): lower_list[1].append(int(in_word[1])) # 유저
            else : lower_list[1].append("x")
            if (in_word[2] != "x"): lower_list[1].append(int(in_word[2])) # 컴퓨터
            else : lower_list[1].append("x")
            
        elif (in_word[0] == "FH:"):
            if (in_word[1] != "x"): lower_list[2].append(int(in_word[1])) # 유저
            else : lower_list[2].append("x")
            if (in_word[2] != "x"): lower_list[2].append(int(in_word[2])) # 컴퓨터
            else : lower_list[2].append("x")
            
        elif (in_word[0] == "SS:"):
            if (in_word[1] != "x"): lower_list[3].append(int(in_word[1])) # 유저
            else : lower_list[3].append("x")
            if (in_word[2] != "x"): lower_list[3].append(int(in_word[2])) # 컴퓨터
            else : lower_list[3].append("x")
            
        elif (in_word[0] == "LS:"):
            if (in_word[1] != "x"): lower_list[4].append(int(in_word[1])) # 유저
            else : lower_list[4].append("x")
            if (in_word[2] != "x"): lower_list[4].append(int(in_word[2])) # 컴퓨터
            else : lower_list[4].append("x")
        
        elif (in_word[0] == "Y:"):
            if (in_word[1] != "x"): lower_list[5].append(int(in_word[1])) # 유저
            else : lower_list[5].append("x")
            if (in_word[2] != "x"): lower_list[5].append(int(in_word[2])) # 컴퓨터
            else : lower_list[5].append("x")
        
        else : return False
            
    for i in range (6): # 1, 2, 3, 4, 5, 6 의 경우의 수 입니다.
        for num in upper_list[i]:
            
            if (num == "x") : continue
        
            if ( (0 <= num <= 5 * (i+1)) ): # 0, 1 * i, ... , 5 * i만 가질수 있습니다.
                if ( (num % (i+1) == 0) ): # i의 배수여야 합니다.
                    pass
                else : return False
            else : return False
        
    # C 일 경우, 5이상, 30 이하의 수를 가집니다.
    # 4K 일 경우, 4 * i + j (i,j 는 1~6) 이므로 5이상, 30 이하의 수를 가집니다.
    # FH 의 경우, 2 * i + 3 * j (i,j는 1~6) 이므로, 5이상, 30 이하의 수를 가지는데, 6과 29는 불가능합니다.
    
    for i in range(0, 3, 1):
        for num in lower_list[i]:
            
            if (num == "x") : continue
            
            if ( (5 <= num <= 30) ):
                if (i == 2) :
                    if (num != 6 and num != 29):
                        pass
                    else : return False

            else : return False
        
    # SS : 15, LS : 30, Y : 50의 값을 가져야 합니다.
    
    for i in range(3, 6, 1):
        for num in lower_list[i] :
            
            if (num == "x") : continue
            
            if (i == 3):
                if (num != 15):
                    return  False
            if (i == 4):
                if (num != 30):
                    return False
            if (i == 5):
                if (num != 50):
                    return False
                
    is_loaded = True
                
    return is_loaded, upper_list, lower_list
    

def load_file2list(upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total):
    # 파일을 열어서 값을 가져오는 함수입니다.
    while (1) :
        file_name = input("Enter filename to load: ") # 파일 이름을 입력 받습니다.
        print()
        
        try:
            f = open(file_name, "r") # 정상적인 파일이 존재할 때까지 받습니다.
        except : 
            print("File does not exist.") 
            print()
            continue
    
        user_cnt = 1
        com_cnt = 1
        is_loaded = False

        file_list = []

        for line in f:
            if (line.isspace()) : continue # 모두 공백인지 판단해 무시합니다.
            else : file_list.append(line)
            
        if (check_error(file_list) == False): # 불가능한 경우 
            pass
        else : is_loaded, upper_list, lower_list = check_error(file_list) # 가능한 경우, 위쪽의 점수 기록과 아래쪽의 점수 기록을 리턴 받습니다.
        
        if (is_loaded == True) : break # 가능한 파일이라면 파일 입력을 탈출합니다.
        else : print("Invalid file content.") ; print() # 그렇지 않을 경우 다시 입력을 받습니다.
        
    
    for index in range(0, 6, 1): # 파일로 받은 local 리스트를 게임에 기록해서 리턴하는 과정입니다.
        in_word = []
        in_word = upper_list[index]
    
        if (in_word[0] != "x"): # 유저
            upper_game_index[1][index] = 1
            upper_game_index_score[0][index] = int(in_word[0])
            player_upper_sum += int(in_word[0])
            user_total += int(in_word[0])
            user_cnt += 1
        
        if (in_word[1] != "x"): # 컴퓨터
            upper_game_index[2][index] = 1
            upper_game_index_score[1][index] = int(in_word[1])
            computer_upper_sum += int(in_word[1])
            com_total += int(in_word[1])
            com_cnt += 1
            
    if (player_upper_sum >= 63):
        user_bonus = 35
        
    if (computer_upper_sum >= 63):
        computer_bonus = 35
            
    for index in range(0, 6, 1):
        in_word = []
        in_word = lower_list[index]
        
        if (in_word[0] != "x"): # 유저
            lower_game_index[1][index] = 1
            lower_game_index_score[0][index] = int(in_word[0])
            user_total += int(in_word[0])
            user_cnt += 1
        
        if (in_word[1] != "x"): # 컴퓨터
            lower_game_index[2][index] = 1
            lower_game_index_score[1][index] = int(in_word[1])
            com_total += int(in_word[1])
            com_cnt += 1

    f.close()
    
    return player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, user_total, com_total, user_cnt, com_cnt


def is_bonus_user(player_upper_sum): # 유저의 윗 부분의 합이 63 이상이라면 보너스 점수 35를 리턴합니다.
    if (player_upper_sum >= 63): return 35
    else : return 0

def is_bonus_computer(computer_upper_sum): # 컴퓨터의 윗 부분의 합이 63 이상이라면 보너스 점수 35를 리턴합니다.
    if (computer_upper_sum >= 63): return 35
    else : return 0

def computer_pattern(computer_dice, upper_game_index, lower_game_index): # 컴퓨터가 주사위를 다시 돌리는 과정입니다.
    
    max_score, newindex = computer_case_search(computer_dice, upper_game_index, lower_game_index) # 족보를 선택합니다.

    for j in range (2): # 주사위를 2번더 굴려서 수정할 수 있습니다.
        if (newindex == 0 or newindex == 1 or newindex == 2 or newindex == 3 or newindex == 4 or newindex == 5 ): # 선택된것이 1, 2, 3, 4, 5, 6
            index_to_reroll = []
            for i in range(5):
                if (computer_dice[i] != newindex + 1): # 선택된 수 이외의 수를 돌립니다.
                    index_to_reroll.append(i)
        elif (newindex == 6) : # 선택된 것이 C 일때
            index_to_reroll = []
            for i in range(5):
                if (computer_dice[i] <= 3): # 3이하의 수를 돌립니다.
                    index_to_reroll.append(i)
        else : 
            if (max_score != 0) : break
            else : index_to_reroll = [0,1,2,3,4] # 족보가 완성되었으면 그대로 하고, 아니면 전부 다시 돌립니다.
            
        print("which dice to reroll (1~5)?", end=" ")
        for i in index_to_reroll: print(i, end=" ")
        print()
        
        for index in index_to_reroll:
            computer_dice[index] = random.randrange(1,7)
            
        print("Roll: ",computer_dice)
        print()
                
    computer_dice = sorted(computer_dice) 
    print("Sorted Roll: ", computer_dice)
    
    print("Choose a category: ", end= "")
            
    if (newindex == 0) : str_index = "1"
    elif (newindex == 1) : str_index = "2"
    elif (newindex == 2) : str_index = "3"
    elif (newindex == 3) : str_index = "4"
    elif (newindex == 4) : str_index = "5"
    elif (newindex == 5) : str_index = "6"
    elif (newindex == 6) : str_index = "C"
    elif (newindex == 7) : str_index = "4K"
    elif (newindex == 8) : str_index = "FH"
    elif (newindex == 9) : str_index = "SS"
    elif (newindex == 10) : str_index = "LS"
    elif (newindex == 11) : str_index = "Y"
    
    print(str_index)
    print()
    
    return str_index     
    

def computer_case_search(computer_dice, upper_game_index, lower_game_index): # 컴퓨터가 어떠한 족보를 고를지 선택하는 과정입니다.
    
    all_case = []
    mycase = ["1","2","3","4","5","6", "C","4K","FH","SS","LS","Y"]
    
    for i in mycase:
        index, score = calc_score(i, computer_dice)
        all_case.append(score) # 각 케이스의 점수를 리턴받습니다.
    
    for i in range(12): # 이미 사용한 족보의 케이스를 제외하는 과정입니다.
        if (i < 6):
            if (upper_game_index[2][i] == 1): all_case[i] = -1
        else : 
            if (lower_game_index[2][i - 6] == 1): all_case[i] = -1
            
    if (all_case[6] < 20): # "C" 가 20 이하일 땐 선택하지 않습니다.
        if ( (upper_game_index[2].count(0) == 0) and (lower_game_index[2].count(0) == 1) and (lower_game_index[2][0] == 0) ) : 
            pass  # 오직 C만 남았을 때는 그대로 선택합니다.
        else : all_case[6] = -1
            
    max_score = -1
    newindex = -1
    
    for i in range(12):
        if (max_score < all_case[i]) : # 최댓값을 선택합니다.
            max_score = all_case[i]
            newindex = i
    
    if (newindex < 6): # 고른 족보를 기록해 둡니다.
        upper_game_index[2][newindex] = 1
    else : 
        lower_game_index[2][newindex - 6] = 1
                 
    return max_score, newindex
            
    
def reroll(user_dice, upper_game_index, upper_game_index_score , lower_game_index, lower_game_index_score): # 유저가 주사위를 다시 선택하는 과정입니다.
    for i in range(2):
        mylist = []
        newlist = []
        cnt = 0
        
        while (1) :
            newlist = list(input("Which dice to reroll (1~5)?").split())
            
            if (len(newlist) == 1): # "Q" or "q" 하나만 입력되었을 경우, 게임을 기록합니다.
                if (newlist[0] == "Q" or newlist[0] == "q") : pause(upper_game_index, upper_game_index_score, lower_game_index, lower_game_index_score) 
            
            try :
                for i in newlist:
                    mylist.append(int(i))
                mylist = list(set(mylist)) # 중복 제거하는 예외 처리
                
                break
            except:
                print("Wrong input!")
                    

        for index in mylist:
            if (index > 5 or index < 1) : continue # 범위 밖의 입력은 무시합니다.
            else : 
                user_dice[index - 1] = random.randrange(1,7)
                cnt += 1
                
        if (cnt == 0) : break # 그냥 엔터만 입력시 break
            
        print("Roll: ", user_dice)
        
    print()
    
    user_dice = sorted(user_dice) 
    print("Sorted Roll: ", user_dice)
    
    while(1):
        
        while(1):
            chosen = input("Choose a category: ") # 족보를 고르는 과정입니다.
            
            if (chosen== "Q" or chosen == "q") : pause(upper_game_index, upper_game_index_score, lower_game_index, lower_game_index_score) # 여기서도 저장 가능
            
            if (chosen == "1") : chosen_index = 0 ; break
            elif (chosen == "2") : chosen_index = 1 ; break
            elif (chosen == "3") : chosen_index = 2 ; break
            elif (chosen == "4") : chosen_index = 3 ; break
            elif (chosen == "5") : chosen_index = 4 ; break
            elif (chosen == "6") : chosen_index = 5 ; break
            elif (chosen == "C" or chosen == "c") : chosen_index = 6 ; break
            elif (chosen == "4K" or chosen == "4k") : chosen_index = 7 ; break
            elif (chosen == "FH" or chosen == "fh") : chosen_index = 8 ; break
            elif (chosen == "SS" or chosen == "ss") : chosen_index = 9 ; break
            elif (chosen == "LS" or chosen == "ls") : chosen_index = 10 ; break
            elif (chosen == "Y" or chosen == "y") : chosen_index = 11 ; break
            else : print("command false.")
            
        if (chosen_index < 6):
            if (upper_game_index[1][chosen_index] == 1): # 이미 사용한 족보는 선택할 수 없습니다.
                print("Wrong input!!")
            else : return chosen
            
        else:
            chosen_index = chosen_index - 6
            if (lower_game_index[1][chosen_index] == 1):
                print("Wrong input!!")
            else : return chosen
            
            # user_dice의 값은 이미 변경되었으므로 리턴할 필요는 없음.
        
def score_input(player, index, score, upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total):
    # 점수를 기록하는 함수입니다. 
    
    if (index < 6): # 만약 upper에 위치한 족보일 경우
        if (player == "user"):
            upper_game_index[1][index] = 1
            upper_game_index_score[0][index] = score
            player_upper_sum += score
            user_total += score
            return player_upper_sum , user_total
        elif (player == "computer"):
            upper_game_index[2][index] = 1
            upper_game_index_score[1][index] = score
            computer_upper_sum += score
            com_total += score
            return computer_upper_sum , com_total
            
    else : # 만약 lower에 위치한 족보일 경우
        index = index - 6
        if (player == "user"):
            lower_game_index[1][index] = 1
            lower_game_index_score[0][index] = score
            user_total += score
            return player_upper_sum , user_total
        elif (player == "computer"):
            lower_game_index[2][index] = 1
            lower_game_index_score[1][index] = score
            com_total += score
            return computer_upper_sum , com_total
    
        
def calc_score(jokbo_index, dice_result) : # 주사위를 굴린 결과를 그 족보의 인덱스와 점수로 리턴하는 함수입니다.
    score = 0
    
    if (jokbo_index == "1"): # 1일 경우
        cnt = 0
        for num in dice_result:
            if (num == 1):
                cnt += 1
        index = 0
        score = cnt * 1 # 1의 합을 리턴합니다.
        return index, score

    elif (jokbo_index == "2"): # 2일 경우
        cnt = 0
        for num in dice_result:
            if (num == 2):
                cnt += 1
        index = 1
        score = cnt * 2 # 2의 합을 리턴합니다.
        return index, score
    
    elif (jokbo_index == "3"): # 3일 경우
        cnt = 0
        for num in dice_result:
            if (num == 3):
                cnt += 1
        index = 2
        score = cnt * 3 # 3의 합을 리턴합니다.
        return index, score
    
    elif (jokbo_index == "4"): # 4일 경우
        cnt = 0
        for num in dice_result:
            if (num == 4):
                cnt += 1
        index = 3
        score = cnt * 4 # 4의 합을 리턴합니다.
        return index, score

    elif (jokbo_index == "5"): # 5일 경우
        cnt = 0
        for num in dice_result:
            if (num == 5):
                cnt += 1
        index = 4
        score = cnt * 5 # 5의 합을 리턴합니다.
        return index, score
             
    elif (jokbo_index == "6"): # 6일 경우
        cnt = 0
        for num in dice_result:
            if (num == 6):
                cnt += 1
        index = 5
        score = cnt * 6 # 6의 합을 리턴합니다.
        return index, score
    
    #### 여기부터 lower 족보 계산 ####
    
    elif (jokbo_index == "C" or jokbo_index == "c") : # C 일 경우
        sum = 0
        for num in dice_result: # 모든 주사위의 합을 리턴합니다.
            sum += num
        index = 6
        score = sum
        return index, score
        
    
    elif (jokbo_index == "4K" or jokbo_index == "4k"): # 4K일 경우
        max_count = 0
        for num in dice_result:
            if (dice_result.count(num) > max_count):
                max_count = dice_result.count(num)

        index = 7
        score = 0

        if (max_count >= 4): # 족보를 만족하는 경우 모든 주사위의 합을 리턴합니다.
            sum = 0
            for num in dice_result:
                sum += num
            score = sum
            return index, score
        else : return index, score # 그렇지 않은 경우 0을 리턴합니다.
        
    
    elif (jokbo_index == "FH" or jokbo_index == "fh"): # FH의 경우
        index = 8
        score = 0
        
        for num in dice_result: # 모든 주사위가 같은 경우도 만족하는 경우로 봅니다.
            if (dice_result.count(num) == 5):
                return index, num * 5
        
        for num in dice_result: # 2개 또는 3개만 있는 경우만 칩니다.
            if (dice_result.count(num) != 2 and dice_result.count(num) != 3):
                return index, score
            
        sum = 0
        for num in dice_result: # 모든 주사위의 합을 리턴합니다.
            sum += num
            
        return index, sum
    
    
    elif (jokbo_index == "SS" or jokbo_index == "ss"): # SS의 경우
        index = 9
        score = 0
        
        is_1, is_2, is_3, is_4, is_5, is_6 = 0,0,0,0,0,0
       
        for num in dice_result:
            if (num == 1): is_1 = 1
            elif (num == 2): is_2 = 1
            elif (num == 3): is_3 = 1
            elif (num == 4): is_4 = 1
            elif (num == 5): is_5 = 1
            elif (num == 6): is_6 = 1
            
        if ( (is_1 == is_2 == is_3 == is_4) or (is_2 == is_3 == is_4 == is_5) or (is_3 == is_4 == is_5 == is_6) ):
            
            return index, 15 # 맞으면 15를,
        else : return index, score # 아니면 0을 리턴합니다.
    
    
    elif (jokbo_index == "LS" or  jokbo_index == "ls"): # LS의 경우
        index = 10
        score = 0
        
        is_1, is_2, is_3, is_4, is_5, is_6 = 0,0,0,0,0,0
       
        for num in dice_result:
            if (num == 1): is_1 = 1
            elif (num == 2): is_2 = 1
            elif (num == 3): is_3 = 1
            elif (num == 4): is_4 = 1
            elif (num == 5): is_5 = 1
            elif (num == 6): is_6 = 1
            
        if ( (is_1 == is_2 == is_3 == is_4 == is_5) or (is_2 == is_3 == is_4 == is_5 == is_6) ):
            
            return index, 30 # 맞으면 30을,
        else : return index, score # 아니면 0을 리턴합니다.
        
        
    elif (jokbo_index == "Y" or jokbo_index == "y"): # Y의 경우
        index = 11
        score = 0
        
        is_Yacht = False
        
        if (dice_result.count(dice_result[0]) == 5):
            is_Yacht == True
            
        if (is_Yacht == True):
            
            return index, 50 # 맞으면 50을
        
        else : return index, score # 아니면 0을 리턴합니다.

def start(): # 시작해서 명령을 받는 합수입니다.
    print_start_screen()
    
    while(1):
        command = int(input("Select a menu:"))
        if(command == 1): # 새로운 게임을 시작했을 때
            print()
            print("Starting a game...")
            start_game(command) 
            break
        elif(command == 2): # 게임을 불러올 때
            print()
            start_game(command)
            break
        elif(command == 3) : print("Program ended. Bye!") ; sys.exit() # 프로그램을 종료했을 때
        else : print("Wrong Input!"); print()

def print_score_board(upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total):
    print("┌─────────────────────────────────────┐")
    print("│      Player      │      Computer    │")
    print("├──────────────────┴──────────────────┤")
    for i in range(6):
        if (upper_game_index[1][i] == 0 and upper_game_index[2][i] == 0): # 둘다 족보를 사용하지 않았을 때
            print("| {:<2s}: {:^13s}│ {:<2s}: {:^13s}│".format(upper_game_index[0][i],"", upper_game_index[0][i], ""))
        elif (upper_game_index[1][i] == 1 and upper_game_index[2][i] == 0): # 유저만 족보를 사용했을 때,
            print("| {:<2s}: {:^13d}│ {:<2s}: {:^13s}│".format(upper_game_index[0][i],upper_game_index_score[0][i], upper_game_index[0][i], "   "))
        elif (upper_game_index[1][i] == 0 and upper_game_index[2][i] == 1): # 컴퓨터만 족보를 사용했을 때,
            print("| {:<2s}: {:^13s}│ {:<2s}: {:^13d}│".format(upper_game_index[0][i], "   ", upper_game_index[0][i], upper_game_index_score[1][i]))
        elif (upper_game_index[1][i] == 1 and upper_game_index[2][i] == 1): # 둘다 족보를 사용했을 때,
            print("| {:<2s}: {:^13d}│ {:<2s}: {:^13d}│".format(upper_game_index[0][i],upper_game_index_score[0][i], upper_game_index[0][i], upper_game_index_score[1][i])) 
    print("├─────────────────────────────────────┤")
    print("| Sub total: %2d/63 | Sub total: %2d/63 |" % (player_upper_sum ,computer_upper_sum))
    print("|  +35 bonus: +%2d  |  +35 bonus: +%2d  |" % (user_bonus, computer_bonus))
    print("├─────────────────────────────────────┤") 
    for i in range(6):
        if (lower_game_index[1][i] == 0 and lower_game_index[2][i] == 0): # 둘다 족보를 사용하지 않았을 때,
            print("| {:<5s}: {:^10s}│ {:<5s}: {:^10s}│".format(lower_game_index[0][i],"   ", lower_game_index[0][i], "   "))
        elif (lower_game_index[1][i] == 1 and lower_game_index[2][i] == 0): # 유저만 족보를 사용했을 때,
            print("| {:<5s}: {:^10d}│ {:<5s}: {:^10s}│".format(lower_game_index[0][i],lower_game_index_score[0][i], lower_game_index[0][i], "   ")) 
        elif (lower_game_index[1][i] == 0 and lower_game_index[2][i] == 1): # 컴퓨터만 족보를 사용했을 때,
            print("| {:<5s}: {:^10s}│ {:<5s}: {:^10d}│".format(lower_game_index[0][i], "   ", lower_game_index[0][i], lower_game_index_score[1][i])) 
        elif (lower_game_index[1][i] == 1 and lower_game_index[2][i] == 1): # 둘다 족보를 사용했을 때,
            print("| {:<5s}: {:^10d}│ {:<5s}: {:^10d}│".format(lower_game_index[0][i],lower_game_index_score[0][i], lower_game_index[0][i], lower_game_index_score[1][i]))
            
        if (i == 0):
            print("├─────────────────────────────────────┤") 
    
    print("├─────────────────────────────────────┤")
    print("| Total:    %3d    | Total:    %3d    |" % (user_total, com_total))
    print("└─────────────────────────────────────┘")
    print()
         
def print_start_screen(): # 단순히 시작화면을 출력합니다.
    print("[Yacht Dice]")
    print("----------------------------------")
    print("1. New Game 2. Load Game 3. Exit")
    print("----------------------------------")
    
def start_game(command): # 게임의 초기 설정을 하고, 유저와 컴퓨터의 턴을 반복하는 함수입니다.
    
    upper_game_index = [["1","2","3","4","5","6"], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]] # 이 족보를 채웠는지 아닌지를 나타냄.
    # 1 인덱스는 플레이어, 2 인덱스는 컴퓨터를 나타냄.
    upper_game_index_score = [[0,0,0,0,0,0], [0,0,0,0,0,0]] # 각 족보에서 얻은 점수를 나타냄.
    # 0 인덱스는 플레이어, 1 인덱스는 컴퓨터를 나타냄.  
    player_upper_sum = 0
    computer_upper_sum = 0
    # 1, 2, 3, 4, 5, 6의 결과 합산한 변수
    user_bonus = 0
    computer_bonus = 0
    # 보너스 점수
    lower_game_index = [["C","4K","FH","SS","LS","Yacht"], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]] # 이 족보를 채웠는지 아닌지를 나타냄.
    lower_game_index_score = [[0,0,0,0,0,0], [0,0,0,0,0,0]] # 각 족보에서 얻은 점수를 나타냄.
    user_total = 0
    com_total = 0
    # 총 점수를 나타내는 변수
    user_cnt, com_cnt = 1, 1
    # 턴 기록을 위한 변수

    if (command == 2) : ## 파일을 불러오는 경우
        
        player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, user_total, com_total, user_cnt, com_cnt = load_file2list(upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total)
        print("Loading a game...")
        print()
    
    print_score_board(upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total)
    
    while(1):
        if (user_cnt == com_cnt): # 유저의 턴
            player_upper_sum , user_total = user_turn(user_cnt, upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total)
            user_bonus = is_bonus_user(player_upper_sum)
            print_score_board(upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total)
            user_cnt += 1
        
        if (user_cnt > com_cnt): # 컴퓨터의 턴
            computer_upper_sum, com_total = computer_turn(com_cnt, upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total)
            computer_bonus = is_bonus_computer(computer_upper_sum)
            
            if(user_cnt == 13) : print("<Final Score Board>")
            
            print_score_board(upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total)
            com_cnt += 1
        
        if (com_cnt == 13): break
        
        ## 여기서 종료할건지 인풋을 받음
        
    if (user_total > com_total): print("You win!")
    elif (user_total == com_total): print("Draw")
    else : print("You lose!")
    
    is_enter = input("Press Enter to continue...")
    print()
    
    start()
            
        
def user_turn(user_cnt, upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total):
    # 유저의 턴을 진행하는 상황입니다.
    
    print("[Player's Turn (%d/12)]" % (user_cnt))
    user_dice = random_dice()
    print("user's dice: ", user_dice)
    
    user_result = reroll(user_dice, upper_game_index, upper_game_index_score, lower_game_index, lower_game_index_score)
    index, score = calc_score(user_result, user_dice)
    player_upper_sum , user_total = score_input("user", index, score, upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total)
    
    print()
    
    return player_upper_sum , user_total

def computer_turn(com_cnt, upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total):
    # 컴퓨터의 턴을 진행하는 상황입니다.
    
    print("[Computer's Turn (%d/12)]" % (com_cnt))
    print()
    
    computer_dice = random_dice()
    print("computer's dice: ", computer_dice)
    print()
    
    str_index = computer_pattern(computer_dice, upper_game_index, lower_game_index)
    
    index, score = calc_score(str_index, computer_dice)
    computer_upper_sum, com_total = score_input("computer", index, score, upper_game_index, upper_game_index_score, player_upper_sum, computer_upper_sum, user_bonus, computer_bonus, lower_game_index, lower_game_index_score, user_total, com_total)
    
    return computer_upper_sum, com_total
    
def main():
    start()


## 시작 ##

    
main()