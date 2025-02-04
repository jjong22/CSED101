import random
import os 
from IPython.display import clear_output

def stair_setting(): # 계단의 개수를 설정합니다.
    num_stair = 0
    while (num_stair < 10 or num_stair > 30): # 10 ~ 30개를 벗어나는 입력을 받거나 형식에 맞지 않는 입력을 받으면 다시 입력을 받습니다.
        num_stair = int(input("게임을 위한 계단의 개수를 입력해주세요. <10 ~ 30> >> "))
    return num_stair
    
def stair(num_stair, user_place, com_place): 
    # 계단의 수, 유저의 위치, 컴퓨터의 위치를 입력받아 계단을 출력하는 함수입니다.
    # 계단의 수가 짝수일 때와 홀수일 때가 동작이 다릅니다.
    
    # 짝수일 때
    # 2중 리스트의 형태로 계단을 만들고, 유저와 컴퓨터의 위치에 그림을 삽입해 현재 상황을 출력합니다.
    if (num_stair % 2 == 0):
        stair_ui = [] # 계단을 출력할 때마다 리스트를 새로 만듭니다. 유저와 컴퓨터의 위치가 변하기 때문에, 계단을 만드는 과정부터 반복합니다.
        for i in range (0, num_stair//2 + 1, 1):
            stair_ui.append([])
            roop_count = 2 * i
            stair_count = i
            for j in range(stair_count):
                stair_ui[i].append("▨")
            for j in range(num_stair - roop_count + 1):
                stair_ui[i].append(" ")
            for j in range(stair_count):
                stair_ui[i].append("▨")
                
        user_r, user_c = where_is_user(user_place, num_stair) # 유저의 좌표를 받아옵니다.
        com_r, com_c = where_is_com(com_place, num_stair) # 컴퓨터의 좌표를 받아옵니다.
        
        stair_ui[user_r][user_c] = '○' # 유저의 좌표에 ○를 넣습니다.
        if(user_c == com_c and user_r == com_r):
            stair_ui[user_r][user_c] = '◑' # 유저와 컴퓨터의 좌표가 같을 경우, ◑를 좌표에 넣습니다.
        else:
            stair_ui[com_r][com_c] = '●' # 좌표가 다른 경우, 컴퓨터의 좌표에 ●를 넣습니다.
              
        for i in range (0, num_stair//2 + 1, 1):
            for j in range (num_stair+1):
                print(stair_ui[i][j], end='')
            print()           
            
    # 홀수일 때
    if (num_stair % 2 == 1):
        stair_ui = []
        for i in range (0, num_stair//2 + 2, 1):
            stair_ui.append([])
            roop_count = 2 * i
            stair_count = i
            for j in range(stair_count):
                stair_ui[i].append("▨")
            for j in range(num_stair - roop_count + 1):
                stair_ui[i].append(" ")
            for j in range(stair_count):
                stair_ui[i].append("▨")
            
        user_r, user_c = where_is_user(user_place, num_stair) # 유저의 좌표를 받아옵니다.
        com_r, com_c = where_is_com(com_place, num_stair) # 컴퓨터의 좌표를 받아옵니다.
        
        stair_ui[user_r][user_c] = '○' # 유저의 좌표에 ○를 넣습니다.
        if(user_c == com_c and user_r == com_r):
            stair_ui[user_r][user_c] = '◑' # 유저와 컴퓨터의 좌표가 같을 경우, ◑를 좌표에 넣습니다.
        else:
            stair_ui[com_r][com_c] = '●' # 좌표가 다른 경우, 컴퓨터의 좌표에 ●를 넣습니다.
               
        for i in range (0, num_stair//2 + 2, 1): # 2중 for문을 이용하여 리스트의 모든 요소를 출력합니다.
            for j in range (num_stair + 1):
                print(stair_ui[i][j], end='')
            print()
    print()
            
def where_is_user(user_place, num_stair): # 유저의 위치를 좌표로 리턴해 주는 함수입니다.
    if (user_place < (num_stair // 2)): # 중앙 전에 있을 때
        user_r = user_place
        user_c = user_place
        return user_r, user_c
    else:
        user_r = num_stair - user_place # 중앙 이후에 있을 때
        user_c = user_place
        return user_r, user_c
    
def where_is_com(com_place, num_stair): # 컴퓨터의 위치를 좌표로 리턴해 주는 함수입니다.
    if (com_place < (num_stair // 2)): # 중앙 전에 있을 때
        com_r = com_place
        com_c = com_place
        return com_r, com_c
    else:
        user_r = num_stair - com_place # 중앙 이후에 있을 때
        user_c = com_place
        return user_r, user_c
    
    # 보여주는 디스플레이에서만 com의 경우 오른쪽을 0로 시작하지만, 내부 처리 상에는 좌표로 사용함.
    
def print_rock(): # 바위를 출력합니다.
    print("┌──────────────────────┐")
    print("|                      |")
    print("|                      |")
    print("│    ▩▩▩▩▩             │")
    print("│   ▩▩▩▩▩▩▩▩▩          │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩         │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩         │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩        │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩        │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩        │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩         │")
    print("│  ▩▩▩▩▩▩▩▩▩▩          │")
    print("│   ▩▩▩▩▩▩▩            │")
    print("|                      |")
    print("└──────────────────────┘")
    
def print_paper(): # 보를 출력합니다.
    print("┌──────────────────────┐")
    print("|                      |")
    print("|                      |")
    print("│    ▩▩▩▩▩             │")
    print("│   ▩▩▩                │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩          │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩    │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩          │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩          │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│   ▩▩▩▩▩              │")
    print("|                      |")
    print("└──────────────────────┘")
    
def print_scissors(): # 가위를 출력합니다.
    print("┌──────────────────────┐")
    print("|                 ▩▩   |")
    print("│       ▩▩      ▩▩▩▩▩  │")
    print("│      ▩▩▩▩▩   ▩▩▩▩▩▩▩ │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩  │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩        │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩          │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩        │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│ ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩    │")
    print("│  ▩▩▩▩▩▩▩ ▩▩▩▩▩▩▩     │")
    print("│   ▩▩▩▩▩▩   ▩▩▩▩▩     │")
    print("│     ▩▩▩      ▩▩      │")
    print("└──────────────────────┘")

def com_choice(): # 컴퓨터의 가위, 바위, 보를 랜덤으로 선택해주는 함수입니다.
    com_rsp = random.randint(1,3)
    
    return com_rsp # 1일 경우 가위, 2일 경우 바위, 3일 경우 보로 지정합니다.         
        
def get_user_rsp(): # 유저의 '가위', '바위', '보' 입력을 받는 함수입니다.
    while(1):
        user_input = input("가위, 바위, 보 중 하나 선택: ")
        print()
        
        if (user_input == "가위"):
            user_rsp = 1
            return user_rsp
        elif (user_input == "바위"):
            user_rsp = 2
            return user_rsp
        elif (user_input == "보"):
            user_rsp = 3
            return user_rsp
        # '가위', '바위', '보' 이외의 입력을 받을 경우 무시하고 다시 입력을 받습니다.

def RSP(): # 컴퓨터의 선택과 유저의 선택을 받아 누가 이겼는지를 반환하는 함수입니다.
    com_rsp = com_choice()
    user_rsp = get_user_rsp()
    
    print_rsp(com_rsp ,user_rsp)
    
    if (com_rsp == user_rsp): # 비겼을 때
        status = -1 
        return status
    elif ( (com_rsp == 1 and user_rsp == 2) or # 유저가 이겼을 때
           (com_rsp == 2 and user_rsp == 3) or 
           (com_rsp == 3 and user_rsp == 1) ) :
        status = 0
        return status
    elif  ((com_rsp == 3 and user_rsp == 2) or # 유저가 졌을 때
           (com_rsp == 1 and user_rsp == 3) or 
           (com_rsp == 2 and user_rsp == 1) ) :
        status = 1
        return status
        
def muk_chi_ppa(): # 가위바위보를 통해 공격권을 얻는 것부터, 묵찌빠를 진행하여 점수를 처리하는 함수입니다.
    status = 0
    score = 0
    user_win = None
    
    # 처음의 가위바위보를 통해 공격권을 결정합니다.
    while (user_win != -1):
        print("[공격권 결정 가위바위보]")
        status = RSP()
        if(status == -1):
            print("[결과] 무승부입니다.")
            print()
            enter_to_conti()
            clear_screen()
        elif(status == 0):
            print("[결과] 이겼습니다.")
            print()
            user_win = True
            enter_to_conti()
            clear_screen()
            break
        elif(status == 1):
            print("[결과] 졌습니다.")
            print()
            user_win = False
            enter_to_conti()
            clear_screen()
            break
        
    # 승부가 날 때가지 묵찌바를 반복하는 부분입니다.
    while(status != -1):
        score += 1 # 초기값을 0으로 설정해서 반복문에 맞게 설정했습니다. 묵찌빠를 반복 할 때마다 1씩 늘어납니다.
        
        print("[묵찌빠]")
        print("승리 시 이동 칸 수: ",score)
        if(status == -1):
            break
        elif(status == 0):
            user_win = True
            print("플레이어 공격, 컴퓨터 수비입니다.")
        elif(status == 1):
            user_win = False
            print("컴퓨터 공격, 플레이어 수비입니다.")
            
        status = RSP() # 가위바위보를 진행해 누가 이겼는지를 저장합니다.
        
        if(status == -1):
            break
        elif(status == 0):
            user_win = True
            print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
        elif(status == 1):
            user_win = False
            print("[결과] 컴퓨터 공격, 플레이어 수비입니다.")
        enter_to_conti()
        clear_screen()
        
    # 만약 같은 것을 내서 묵찌빠가 종료된 경우 빠져나와서 점수를 처리합니다.
    if(user_win == True): # 유저가 공격권을 가진 상태로 묵찌빠를 이긴(가위바위보가 무승부) 경우, 유저가 누적된 score 값 만큼 이동합니다.
        print("[결과] 묵찌빠 종료")
        print()
        print("플레이어 승, ",score,("칸 이동합니다."))
        print()
        status = 0
        enter_to_conti()
        clear_screen()
        return status, score
    elif(user_win == False): # 컴퓨터가 공격권을 가진 상태로 묵찌빠를 이긴(가위바위보가 무승부) 경우, 컴퓨터가 누적된 score 값 만큼 이동합니다.
        print("[결과] 묵찌빠 종료")
        print()
        print("컴퓨터 승, ",score,("칸 이동합니다."))
        print()
        status = 1
        enter_to_conti()
        clear_screen()
        return status, score
    
def print_rsp(com_rsp ,user_rsp): # 컴퓨터와 유저의 가위바위보를 출력합니다.
    print("[컴퓨터 선택]")
    if (com_rsp == 1):
        print_scissors()
    elif (com_rsp == 2):
        print_rock()
    elif (com_rsp == 3):
        print_paper()
           
    print("[플레이어 선택]")
    if (user_rsp == 1):
        print_scissors()
    elif (user_rsp == 2):
        print_rock()
    elif (user_rsp == 3):
        print_paper()      
        
    # ***********************************************************************************
    # 위의 stair 함수에서 알 수 있듯이 user_place와 com_place는 리스트에서 좌표를 나타냅니다.
    # 하지만 게임에서 처음의 위치를 0으로 설정하였기 때문에
    # 컴퓨터의 경우 총 계단 수에서 좌표값을 빼는 방식으로 계산합니다. 
    # ***********************************************************************************
    
def display_place(num_stair, user_place, com_place): # 현재 게임의 정보를 출력하는 역할을 합니다.
    print("총 계단 수: ", num_stair)
    print("PLAYER:   ○ <", user_place, ">")
    print("COMPUTER: ● <", num_stair - com_place, ">")
    print()
    

def clear_screen(): # 화면을 clear합니다. 윈도우 환경에서 실행했습니다.
	os.system('cls') # Windows 콘솔 창에서 실행 시 주석 해제
	# os.system('clear') # Linux 콘솔 창에서 실행 시 주석 해제 
	# clear_output() # jupyter notebook 외 실행 시 주석 처리할 것
	return 0

def enter_to_conti(): # 단순히 엔터를 입력하면 넘어가는 함수입니다.
    user_input = None
    while(user_input != ""):
        user_input = input("계속하려면 엔터를 눌러주세요...")

def main(): # 게임의 흐름이 진행되는 메인 함수입니다.
    num_stair = 10
    user_place = 0
    com_place = num_stair
    
    print("======================")
    print("[묵찌빠 계단 오르기]")
    print("======================")
    stair(num_stair, user_place, com_place) # 초기의 값을 10으로 설정해 계단의 에시를 보여줍니다.
    
    num_stair = stair_setting()
    com_place = num_stair
    clear_screen()
    display_place(num_stair, user_place, com_place)
    stair(num_stair, user_place, com_place)
    enter_to_conti()
    clear_screen() # 입력받은 계단의 수를 바탕으로 계단을 설정합니다.
    
    while(1): # 게임이 끝날 때까지 묵찌빠를 반복합니다.
        status, score = muk_chi_ppa()
        if(status == 0):
            user_place += score
            if (user_place >= num_stair): # 플레이어가 이겼을 때
                user_place = num_stair # 리스트의 인덱스를 벗어나지 않도록 좌표를 num_stair(원래 컴퓨터의 위치)로 설정합니다.
                display_place(num_stair, user_place, com_place)
                stair(num_stair, user_place, com_place)
                print("▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨")
                print("플레이어 최종 승리!!!")
                print("▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨")
                print()
                print("게임을 종료합니다...")
                break
            display_place(num_stair, user_place, com_place)
        elif(status == 1):
            com_place -= score
            if (com_place <= 0): # 컴퓨터가 이겼을 때
                com_place = 0 # 리스트의 인덱스를 벗어나지 않도록 좌표를 0(원래 유저의 위치)로 설정합니다.
                display_place(num_stair, user_place, com_place)
                stair(num_stair, user_place, com_place)
                print("▨▨▨▨▨▨▨▨▨▨▨▨▨")
                print("컴퓨터 최종 승리!!!")
                print("▨▨▨▨▨▨▨▨▨▨▨▨▨")
                print()
                print("게임을 종료합니다...")
                break
            display_place(num_stair, user_place, com_place)
            
        stair(num_stair, user_place, com_place) # 묵찌빠 한 라운드가 끝났을 때, 업데이트 된 계단의 상태를 보여주고 다시 묵찌빠의 초기부터 시작합니다.
        enter_to_conti()
        clear_screen()
    
    return 0

main()