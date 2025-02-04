import random
import copy

class Posmon: # 포스몬에 대한 클래스
    
    def __init__(self, health, max_health, attack, defence, move, name):
        self.health = health
        self.max_health = max_health
        
        self.first_attack = attack
        self.first_defence = defence
        
        self.attack = attack
        self.defence = defence
        self.moves = move
        self.name = name
    
    def get_name(self)->str: # 이름을 반환합니다
        return self.name
    
    def get_max_health(self)->int: # 최대 체력을 반환
        return self.max_health
    
    def get_health(self)->int: # 현재 체력 반환
        return self.health
    
    def get_type(self)->str: # 타입을 반환
        pass
        # 서브클래스에서 오버라이딩으로 구현
        
    def get_move(self)->str: # 사용할 수 있는 기술을 반환
        return self.moves
        
    def reset_status(self): # 초기 설정으로 되돌림?
        self.attack = self.first_attack
        self.defence = self.first_defence
            
class Ponix(Posmon): # Posmon -> Ponix class
    
    def __init__(self, health=86,max_health=86,attack=20,defence=23,move=["Tackle", "Growl", "SwordDance"],name="Ponix"):
        super().__init__(health, max_health, attack, defence, move, name)
    
    def get_type(self)->str:
        return "Paper"
    
class Normie(Posmon): # Posmon -> Normie class
    
    def __init__(self):
        super().__init__(health=80,max_health=80,attack=20,defence=20,move=["Tackle", "Swift", "TailWhip"],name="Normie")
    
    def get_type(self)->str:
        return "Nothing"
    
class Rocky(Posmon): # Rocky -> Normie class
    
    def __init__(self):
        super().__init__(health=80,max_health=80,attack=15,defence=25,move=["Tackle", "Growl"],name="Rocky")
    
    def get_type(self)->str:
        return "Rock"   
    
class Swania(Posmon): # Swania -> Normie class
    
    def __init__(self):
        super().__init__(health=80,max_health=80,attack=30,defence=10,move=["ScissorsCross", "SwordDance"],name="Swania")
    
    def get_type(self)->str:
        return "Scissors"   

class Move: # 기술에 대한 클래스
    def __init__(self, name):
        self.name = name
        
    def get_name(self)->str :
        return self.name
    
    def use(self, our_posmon:Posmon, opponent_posmon:Posmon):
        pass
    ## 밑에서 오버라이딩
    
class PhysicalMove(Move): # 데미지를 입히는 물리적인 기술
    
    def __init__(self, power, name):
        super().__init__(name)
        self.power = power
        
    def get_power(self)->int: # 기술의 데미지를 리턴
        return self.power
    
    def use(self, our_posmon:Posmon, opponent_posmon:Posmon): # 실제 데미지를 계산하는 함수 ## use ("공격한 포스몬", "공격 받은 포스몬")
        ss = ss_result(our_posmon.get_type(), opponent_posmon.get_type()) ## 상성을 계산하는 함수 -> 이겼으면 2, 아니면 1을 리턴
        
        damage = max(0, self.power + our_posmon.attack - opponent_posmon.defence) * ss # 데미지 계산식
        opponent_posmon.health -= damage # 체력 계산
        
        print("- %s 포스몬의 [체력] %d 감소 (%d->%d)" %(opponent_posmon.name, damage, opponent_posmon.health+damage, opponent_posmon.health) )
        pass
    
def ss_result(our_type, oppo_type): # 상성을 통해 공격 배율 계산
    if (our_type == "Scissors" and oppo_type == "Paper"):
        return 2
    elif (our_type == "Paper" and oppo_type == "Rock"):
        return 2
    elif (our_type == "Rock" and oppo_type == "Scissors"):
        return 2
    else : return 1
    
    # Scissors Paper Rock Nothing
    
class Tackle(PhysicalMove): # Tackle 공격
    def __init__(self):
        super().__init__(power = 25, name = "Tackle")
        
    def get_speed(self):
        return 0
    
class ScissorsCross(PhysicalMove): # ScissorsCross 공격
    def __init__(self):
        super().__init__(power = 30, name = "ScissorsCross")
        
    def get_speed(self):
        return 0
    
class Swift(PhysicalMove): # Swift 공격
    def __init__(self):
        super().__init__(power = 0, name = "Swift")
        
    def get_speed(self):
        return 3

class StatusMove(Move):
    pass
    ## 그냥 개념적인 변화기 클래스
    
class Growl(StatusMove): # Growl 변화기
    
    def __init__(self, name = "Growl"):
        super().__init__(name)
        self.amount = -5
        
    def get_speed(self) -> int:
        return 1
    
    def use(self, our_posmon:Posmon, opponent_posmon:Posmon):
        if (opponent_posmon.attack < 5):
            effect = opponent_posmon.attack
            opponent_posmon.attack = 0 # 0 이하로 내려가지 않습니다
        else : effect = self.amount ; opponent_posmon.attack += effect
        
        print("- %s 포스몬의 [공격력] %d 감소 (%d->%d)" % (opponent_posmon.name, -effect, opponent_posmon.attack - effect, opponent_posmon.attack) )
        
class SwordDance(StatusMove): # SwordDance 변화기
    
    def __init__(self, name = "SwordDance"):
        super().__init__(name)
        self.amount = 10
        
    def get_speed(self) -> int:
        return 0
    
    def use(self, our_posmon:Posmon, opponent_posmon:Posmon):
        effect = 10
        our_posmon.attack += effect
        
        print("- %s 포스몬의 [공격력] %d 증가 (%d->%d)" % (our_posmon.name, effect, our_posmon.attack - effect, our_posmon.attack) )
        
class TailWhip(StatusMove): # TailWhip 변화기
    
    def __init__(self, name = "TailWhip"):
        super().__init__(name)
        self.amount = -5
        
    def get_speed(self) -> int:
        return 1
    
    def use(self, our_posmon:Posmon, opponent_posmon:Posmon):
        if (opponent_posmon.defence < 5):
            effect = opponent_posmon.defence
            opponent_posmon.defence = 0 # 0 이하로 내려가지 않습니다
        else : effect = self.amount ; opponent_posmon.defence += effect
        
        print("- %s 포스몬의 [방어력] %d 감소 (%d->%d)" % (opponent_posmon.name, -effect, opponent_posmon.defence - effect, opponent_posmon.defence) )
        
class Change(): # 기술과 같이 클래스를 만들어서 밑의 계산식에 대응하게 함.
    def get_speed(self) -> int:
        return 100
    
    def get_name(self) -> int:
        return "Change"

def print_start(): # 시작 페이지 그림
    print(" ____    ___   ______ ___ ___   ___   ____ ")
    print("|    \\  /   \\ / ___ /|   T   | /   \\ |    \\")
    print("|  o  )Y     Y(   \\_ |  _    |Y     Y|  _  Y")
    print("|    _/|  O  | \\__  T|  \\_/  ||  O  ||  |  |")
    print("|    | |     | /  \\ ||   |   ||     ||  |  |")
    print("|    | l     ! \\    ||   |   |l     !|  |  |")
    print("l____j  \\____/  \\___jl___j___i \\___/ l__j__j")
    
def print_menu(): # 초기 선택 메뉴
    print("============================================")
    print("0. 포스몬 선택 ")
    print("1. 배틀하기")
    print("2. 종료하기")
    print("============================================")

def print_select(i): # 포스몬을 고르는 중에 출력
    print("============================================")
    print("당신이 사용할 포스몬을 선택하세요. 현재 %d 마리/최대 3 마리" %(i))
    print("0. Ponix")
    print("1. Normie")
    print("2. Swania")
    print("3. Rocky")
    if (i != 0): # 1개 이상을 골랐을 때, 종료할 수 있습니다.
        print("-1. 그만두기")
    print("============================================")

def start_mode(): # 프로그램에서 모드를 설정합니다.
    i = 0
    myposmon = []

    while(1):
        print_menu()
        command = int(input("입력: "))

        if (command == 0) : # 0 : 포스몬 선택
            i = pos_select(myposmon, i)
            print()
        elif (command == 1) : # 1 : 배틀
            if (len(myposmon) == 0): # 포스몬을 담는 변수에 포스몬 객체가 존재하지 않을 때
                print()
                print("싸울 포스몬이 없습니다! 먼저 포스몬을 선택해 주세요.")
                print()
                continue
            
            battle(myposmon)  
            break
        elif (command == 2) : print("프로그램을 종료합니다..") ; exit(0) # 2 : 프로그램 종료
        else : print("잘못된 입력입니다. 다시 입력하세요")

def pos_select(myposmon, i): # 포스몬을 최대 3개까지 선택할 수 있습니다.
    
    if (len(myposmon) == 3):
        print("이미 포스몬을 모두 선택했습니다!")
        return i
    
    while (1):
        
        if (i == 3) : # 모두 골랐다면 고른 항목을 모두 출력하고, 다시 메뉴로 돌아갑니다.
            print("============================================")
            print("당신의 포스몬 목록: ", end="")
            for posmon in myposmon:
                print(posmon.get_name(), end=" ")
            print()
            print("============================================")
            return i
            
        print_select(i)
        
        while (1): # 포스몬을 리스트에 deepcopy 해 집어 넣습니다. 앞으로 객체는 리스트에 인덱스로 접근하여 이용합니다.
            user_num = int(input("입력: "))
            print()
        
            if (user_num == 0) : # 0 : Ponix를 선택합니다.
                if (i >= 3):
                    continue
                posmon = Ponix()
                mypoix = copy.deepcopy(posmon)
                del(posmon)
                
                myposmon.append(mypoix)
                i += 1
                break
            elif (user_num == 1) : # 1 : Normie를 선택합니다.
                if (i >= 3):
                    continue
                posmon = Normie()
                mynormie = copy.deepcopy(posmon)
                del(posmon)
                
                myposmon.append(mynormie)
                i += 1
                break
            elif (user_num == 2) : # 2 : Swania를 선택합니다.
                if (i >= 3):
                    continue
                posmon = Swania()
                myswania = copy.deepcopy(posmon)
                del(posmon)
                
                myposmon.append(myswania)
                i += 1
                break
            elif (user_num == 3) : # 3 : Rocky를 선택합니다.
                if (i >= 3):
                    continue
                posmon = Rocky()
                myrocky = copy.deepcopy(posmon)
                del(posmon)
                
                myposmon.append(myrocky)
                i += 1
                break
            elif (user_num == -1 and i != 0): # 포스몬 선택을 중지할 때,
                print("============================================")
                print("당신의 포스몬 목록: ", end="")
                for posmon in myposmon:
                    print(posmon.get_name(), end=" ")
                print()
                print("============================================")
                return i
            else : 
                print("잘못된 입력입니다. 다시 입력하세요.")
                print()

def print_interface(myposmon, composmon): # 배틀을 시작할 때, 포스몬의 항목을 나타내는 함수
    is_my = []
    is_com = []

    print()
    print(("============================================")) # 플레이어는 포스몬을 1, 2, 3개를 갖고 게임을 진행할 수 있습니다.
    if (len(myposmon) == 1):
        print("당신의 포스몬 목록 %s" % (myposmon[0].get_name()) )
        is_my.append("O")
    elif (len(myposmon) == 2):
        print("당신의 포스몬 목록 %s %s" % (myposmon[0].get_name(), myposmon[1].get_name()) )
        is_my.append("O")
        is_my.append("O")
    elif (len(myposmon) == 3):
        print("당신의 포스몬 목록 %s %s %s" % (myposmon[0].get_name(), myposmon[1].get_name(), myposmon[2].get_name()) )
        is_my.append("O")
        is_my.append("O")
        is_my.append("O")
        
    print("컴퓨터 포스몬 목록 %s %s %s" % (composmon[0].get_name(), composmon[1].get_name(), composmon[2].get_name()) )
    is_com.append("O")
    is_com.append("O")
    is_com.append("O")
    
    print(("============================================"))
    print()

    return is_my, is_com

def battle(myposmon): # 전투를 진행하는 부분입니다.
    
    composmon = []
    
    posmon1 = Ponix() ; posmon2 = Normie() ; posmon3 = Swania() ; posmon4 = Rocky()
    all_posmon = [posmon1, posmon2, posmon3, posmon4]
    
    for i in range(3): # 중복되지 않게 컴퓨터의 포스몬을 랜덤으로 선택합니다.

        choiced_posmon = random.choice(all_posmon)
        myindex = all_posmon.index(choiced_posmon)
    
        composmon.append(choiced_posmon)
        
        all_posmon.remove(choiced_posmon)
        
    # 컴퓨터가 포켓몬을 선택하는 과정입니다.

    is_my, is_com = print_interface(myposmon, composmon)
    
    my_index = 0 # 현재 포스몬의 인덱스를 나타냄.
    com_index = 0
    # zero_base index
    
    print("배틀이 시작됩니다.")
    
    while (1):
        fight_command(myposmon, composmon, is_my, is_com, my_index, com_index)
    
    
def fight_command(myposmon, composmon, is_my, is_com, my_index, com_index): # 전투가 진행되는 메인 함수입니다.
    
    is_user_win = False
    is_com_win = False
    
    print_status(myposmon, composmon, is_my, is_com, my_index, com_index) # 게임식으로 화면을 출력합니다.
    
    while(1): # 유저의 공격 선택
        
        first_input = input("입력: ")
        user_commnad = first_input.split()
        
        if (user_commnad[0] == "e") :  # 내 포스몬의 숫자 이름, 체력 확인
            
            remain_posmon = 0
            
            for i in range(len(is_my)): # is_my에 "O"로 표현된, 즉 생존해 있는 포스몬의 정보를 표시합니다.
                if (is_my[i] == "O"):
                    remain_posmon += 1
            
            print("남은 포스몬의 숫자 : %d / %d" % (remain_posmon, len(is_my)) )
            for i in range(len(is_my)):
                if (is_my[i] == "O"):
                    print("(%d) %s    <|%s   %d / %d|" % (i, myposmon[i].get_name(),myposmon[i].get_type() ,myposmon[i].get_health(), myposmon[i].get_max_health() ) )
                    
            print()
                
        elif (user_commnad[0] == "o") : # 공격
            try :
                my_command = int(user_commnad[1]) # 입력을 정수로 바꾸길 시도합니다.
                if (len(myposmon[my_index].get_move()) == 2): # 만약 기술이 2개 존재하는 경우
                    my_range = [0,1]
                elif (len(myposmon[my_index].get_move()) == 3): # 만약 기술이 3개 존재하는 경우
                    my_range = [0,1,2]

                if ( (my_command not in my_range)): # 인덱스 범위를 넘어가는 경우
                    print("선택할 수 없는 기술입니다!") ; print() ;continue
            except : # 자료형 등에 오류가 있는 경우
                print("입력 형식이 잘못 되었습니다.") ; print() ;continue
            
            user_attack = myposmon[my_index].get_move()[my_command] # 유저가 선택한 공격의 종류
            
            com_attack, composmon, is_com, com_index = com_act(composmon, is_com, com_index) # 컴퓨터가 한 공격
            
            user_skill, user_speed = calc_skill(user_attack) # 유저가 선택한 공격의 객체와 스피드
            com_skill, com_speed = calc_skill(com_attack) # 컴퓨터가 선택한 공격의 객체와 스피드
            
            if (user_speed >= com_speed): # 유저의 스피드가 빠를 때,
                if (user_attack == "Change"): # 만약 포스몬을 교체하는 경우
                    
                    myposmon[my_index].reset_status() # 현재 있는 포켓몬을 집어 넣을 때, 능력치 초기화
                    
                    attack_oper(user_skill, myposmon, my_index, composmon, com_index) # 자신의 포스몬 -> 다른 사람의 포켓몬
                    print("당신의 포스몬 %s로 교대" % (myposmon[my_index].get_name()) )
                else : # 일반적은 기술의 경우
                    print("당신의 %s: %s 기술 사용" % (myposmon[my_index].get_name(), user_attack) )
                    attack_oper(user_skill, myposmon, my_index, composmon, com_index) # 자신의 포스몬 -> 다른 사람의 포켓몬
                
                if (composmon[com_index].get_health() <= 0): # 적 포스몬이 쓰러진 경우
                    is_com[com_index] = "X" # 쓰러짐을 기록
                    
                    print("컴퓨터 %s: 쓰러짐" % (composmon[com_index].get_name() ) )
                    
                    if ("O" not in is_com) : # 모든 포스몬이 쓰러졌을 때,
                        is_user_win = True
                        print()
                        print_status(myposmon, composmon, is_my, is_com, my_index, com_index)
                        print()
                        game_result(is_user_win, is_com_win)
                    com_index = com_replace(is_com, com_index) # 남은 포스몬으로 교체함
                    
                    print("컴퓨터 포스몬 %s로 교대" % (composmon[com_index].get_name() ))
                    
                    continue
                    
                if (com_attack == "Change"): # 컴퓨터가 교체를 선택했을 때
                    
                    composmon[com_index].reset_status()
                    
                    attack_oper(com_skill, composmon, com_index, myposmon, my_index) # 다른 사람의 포스몬 -> 자신의 포켓몬
                    print("컴퓨터의 포스몬 %s로 교대" % (composmon[com_index].get_name()) )
                else : # 일반적인 기술의 경우
                    print("컴퓨터의 %s: %s 기술 사용" % (composmon[com_index].get_name(), com_attack) )
                    attack_oper(com_skill, composmon, com_index, myposmon, my_index) # 다른 사람의 포스몬 -> 자신의 포켓몬
                
                if (myposmon[my_index].get_health() <= 0): # 유저의 포스몬이 쓰러졌을 경우
                    is_my[my_index] = "X" # 기록
                    remain_posmon = 0
                    
                    print("유저 %s: 쓰러짐" % (myposmon[my_index].get_name() ) )
            
                    for i in range(len(is_my)):
                        if (is_my[i] == "O"):
                            remain_posmon += 1
            
                    print("남은 포스몬의 숫자 : %d / %d" % (remain_posmon, len(is_my)) )
                    for i in range(len(is_my)):
                        if (is_my[i] == "O"):
                            print("(%d) %s    <|%s   %d / %d|" % (i, myposmon[i].get_name(),myposmon[i].get_type() ,myposmon[i].get_health(), myposmon[i].get_max_health() ) )
                    
                    if ("O" not in is_my) : # 모든 아군 포스몬이 쓰러졌을 때,
                        is_com_win = True
                        print()
                        print_status(myposmon, composmon, is_my, is_com, my_index, com_index)
                        print()
                        game_result(is_user_win, is_com_win)
                    
                    print()
                    my_index = user_replace(is_my, my_index) # 포스몬 교체 과정
                    
                    print("유저 포스몬 %s로 교대" % (myposmon[my_index].get_name() ))
                    
            else : # 컴퓨터의 공격이 빠를 때, *** 이부분의 코드와 밑의 s 를 통해 교체를 할 때의 코드도 동일하게 구성되어 있습니다. ***
                if (com_attack == "Change"): 
                    
                    composmon[com_index].reset_status()
                    
                    attack_oper(com_skill, composmon, com_index, myposmon, my_index) # 다른 사람의 포스몬 -> 자신의 포켓몬
                    print("컴퓨터의 포스몬 %s로 교대" % (composmon[com_index].get_name()) )
                else : 
                    print("컴퓨터의 %s: %s 기술 사용" % (composmon[com_index].get_name(), com_attack) )
                    attack_oper(com_skill, composmon, com_index, myposmon, my_index) # 다른 사람의 포스몬 -> 자신의 포켓몬
                
                if (myposmon[my_index].get_health() <= 0):
                    is_my[my_index] = "X"
                    remain_posmon = 0
                    
                    print("유저 %s: 쓰러짐" % (myposmon[my_index].get_name() ) )
            
                    for i in range(len(is_my)):
                        if (is_my[i] == "O"):
                            remain_posmon += 1
            
                    print("남은 포스몬의 숫자 : %d / %d" % (remain_posmon, len(is_my)) )
                    for i in range(len(is_my)):
                        if (is_my[i] == "O"):
                            print("(%d) %s    <|%s   %d / %d|" % (i, myposmon[i].get_name(),myposmon[i].get_type() ,myposmon[i].get_health(), myposmon[i].get_max_health() ) )
                    
                    if ("O" not in is_my) :
                        is_com_win = True
                        print()
                        print_status(myposmon, composmon, is_my, is_com, my_index, com_index)
                        print()
                        game_result(is_user_win, is_com_win)
                    
                    print()
                    
                    my_index = user_replace(is_my, my_index)
                    
                    print("유저 포스몬 %s로 교대" % (myposmon[my_index].get_name() ))
                    
                    continue
                
                if (user_attack == "Change"): 
                    
                    myposmon[my_index].reset_status()
                    
                    attack_oper(user_skill, myposmon, my_index, composmon, com_index) # 자신의 포스몬 -> 다른 사람의 포켓몬
                    print("당신의 포스몬 %s로 교대" % (myposmon[my_index].get_name()) )
                else : 
                    print("당신의 %s: %s 기술 사용" % (myposmon[my_index].get_name(), user_attack) )
                    attack_oper(user_skill, myposmon, my_index, composmon, com_index) # 자신의 포스몬 -> 다른 사람의 포켓몬
                
                if (composmon[com_index].get_health() <= 0):
                    is_com[com_index] = "X"
                    
                    print("컴퓨터 %s: 쓰러짐" % (composmon[com_index].get_name() ) )
                    
                    if ("O" not in is_com) :
                        is_user_win = True
                        print()
                        print_status(myposmon, composmon, is_my, is_com, my_index, com_index)
                        print()
                        game_result(is_user_win, is_com_win)
                    com_index = com_replace(is_com, com_index)
                    
                    print("컴퓨터 포스몬 %s로 교대" % (composmon[com_index].get_name() ))
                    
            print()

            # 유저, 컴퓨터로 데미지 계산
            
        elif (user_commnad[0] == "s") : # 교대하는 과정입니다.
            
            num_O = 0
            num_O_index = []
    
            for i in range (3): # 남은 포스몬과 그 위치를 판단하는 계산과정입니다.
                if is_com[i] == "O":
                    num_O += 1
                    num_O_index.append(i)
                    
            if (num_O == 1): # 나와있는 포스몬 혼자만 존재할 경우, 교체를 할 수 없습니다.
                print("교체할 포스몬이 없습니다!") ; print() ; continue
            
            try :
                my_command = int(user_commnad[1]) # 정수로 바꾸기
                if (len(is_my) == 2):
                    my_range = [0,1]
                elif (len(is_my) == 3):
                    my_range = [0,1,2]
                    
                if ( (my_command not in my_range) or (is_my[my_command] == "X") ):
                    print("포스몬을 교대할 수 없습니다!") ; print() ;continue
            except :
                print("입력 형식이 잘못 되었습니다.") ; print() ;continue
            
            if (my_command == my_index): # 자기자신으로 교체하려한 경우
                print("현재 나와있는 포켓몬으로 바꿀 수 없습니다!") ; print() ; continue
                
            print()
            
            my_index = my_command
            
            user_attack = "Change" # 교체의 명령
            
            com_attack, composmon, is_com, com_index = com_act(composmon, is_com, com_index)
            
            user_skill, user_speed = calc_skill(user_attack)
            com_skill, com_speed = calc_skill(com_attack)
            
            if (user_speed >= com_speed): # 위의 공격 과정과 동일합니다.
                if (user_attack == "Change"): 
                    
                    myposmon[my_index].reset_status()
                    
                    attack_oper(user_skill, myposmon, my_index, composmon, com_index) # 자신의 포스몬 -> 다른 사람의 포켓몬
                    print("당신의 포스몬 %s로 교대" % (myposmon[my_index].get_name()) )
                else : 
                    print("당신의 %s: %s 기술 사용" % (myposmon[my_index].get_name(), user_attack) )
                    attack_oper(user_skill, myposmon, my_index, composmon, com_index) # 자신의 포스몬 -> 다른 사람의 포켓몬
                
                if (composmon[com_index].get_health() <= 0):
                    is_com[com_index] = "X"
                    print("컴퓨터 %s: 쓰러짐" % (composmon[com_index].get_name() ) )
                    
                    if ("O" not in is_com) :
                        is_user_win = True
                        print()
                        print_status(myposmon, composmon, is_my, is_com, my_index, com_index)
                        print()
                        game_result(is_user_win, is_com_win)
                    com_index = com_replace(is_com, com_index)
                    
                    print("컴퓨터 포스몬 %s로 교대" % (composmon[com_index].get_name() ))
                    
                    continue
                    
                if (com_attack == "Change"): 
                    
                    composmon[com_index].reset_status()
                    
                    attack_oper(com_skill, composmon, com_index, myposmon, my_index) # 다른 사람의 포스몬 -> 자신의 포켓몬
                    print("컴퓨터의 포스몬 %s로 교대" % (composmon[com_index].get_name()) )
                else : 
                    print("컴퓨터의 %s: %s 기술 사용" % (composmon[com_index].get_name(), com_attack) )
                    attack_oper(com_skill, composmon, com_index, myposmon, my_index) # 다른 사람의 포스몬 -> 자신의 포켓몬
                
                if (myposmon[my_index].get_health() <= 0):
                    is_my[my_index] = "X"
                    remain_posmon = 0
                    
                    print("유저 %s: 쓰러짐" % (myposmon[my_index].get_name() ) )
            
                    for i in range(len(is_my)):
                        if (is_my[i] == "O"):
                            remain_posmon += 1
            
                    print("남은 포스몬의 숫자 : %d / %d" % (remain_posmon, len(is_my)) )
                    for i in range(len(is_my)):
                        if (is_my[i] == "O"):
                            print("(%d) %s    <|%s   %d / %d|" % (i, myposmon[i].get_name(),myposmon[i].get_type() ,myposmon[i].get_health(), myposmon[i].get_max_health() ) )
                    
                    if ("O" not in is_my) :
                        is_com_win = True
                        print()
                        print_status(myposmon, composmon, is_my, is_com, my_index, com_index)
                        print()
                        game_result(is_user_win, is_com_win)
                    
                    print()
                    
                    my_index = user_replace(is_my, my_index)
                    
                    print("유저 포스몬 %s로 교대" % (myposmon[my_index].get_name() ))
            
            else :
                if (com_attack == "Change"): 
                    
                    composmon[com_index].reset_status()
                    
                    attack_oper(com_skill, composmon, com_index, myposmon, my_index) # 다른 사람의 포스몬 -> 자신의 포켓몬
                    print("컴퓨터의 포스몬 %s로 교대" % (composmon[com_index].get_name()) )
                    
                else : 
                    print("컴퓨터의 %s: %s 기술 사용" % (composmon[com_index].get_name(), com_attack) )
                    attack_oper(com_skill, composmon, com_index, myposmon, my_index) # 다른 사람의 포스몬 -> 자신의 포켓몬
                
                if (myposmon[my_index].get_health() <= 0):
                    is_my[my_index] = "X"
                    remain_posmon = 0
                    
                    print("유저 %s: 쓰러짐" % (myposmon[my_index].get_name() ) )
            
                    for i in range(len(is_my)):
                        if (is_my[i] == "O"):
                            remain_posmon += 1
            
                    print("남은 포스몬의 숫자 : %d / %d" % (remain_posmon, len(is_my)) )
                    for i in range(len(is_my)):
                        if (is_my[i] == "O"):
                            print("(%d) %s    <|%s   %d / %d|" % (i, myposmon[i].get_name(),myposmon[i].get_type() ,myposmon[i].get_health(), myposmon[i].get_max_health() ) )
                    
                    if ("O" not in is_my) :
                        is_com_win = True
                        print()
                        print_status(myposmon, composmon, is_my, is_com, my_index, com_index)
                        print()
                        game_result(is_user_win, is_com_win)
                    
                    print()
                    
                    my_index = user_replace(is_my, my_index)
                    
                    print("유저 포스몬 %s로 교대" % (myposmon[my_index].get_name() ))
                    
                    continue
                
                if (user_attack == "Change"): 
                    
                    myposmon[my_index].reset_status()
                    
                    attack_oper(user_skill, myposmon, my_index, composmon, com_index) # 자신의 포스몬 -> 다른 사람의 포켓몬
                    print("당신의 포스몬 %s로 교대" % (myposmon[my_index].get_name()) )
                    
                else : 
                    print("당신의 %s: %s 기술 사용" % (myposmon[my_index].get_name(), user_attack) )
                    attack_oper(user_skill, myposmon, my_index, composmon, com_index) # 자신의 포스몬 -> 다른 사람의 포켓몬
                
                if (composmon[com_index].get_health() <= 0):
                    is_com[com_index] = "X"
                    print("컴퓨터 %s: 쓰러짐" % (composmon[com_index].get_name() ) )
                    
                    if ("O" not in is_com) :
                        is_user_win = True
                        print()
                        print_status(myposmon, composmon, is_my, is_com, my_index, com_index)
                        print()
                        game_result(is_user_win, is_com_win)
                    com_index = com_replace(is_com, com_index)
                    
                    print("컴퓨터 포스몬 %s로 교대" % (composmon[com_index].get_name() ))
                
            # 유저, 컴퓨터로 데미지 계산
            
        else : print("잘못된 명령어: ", first_input) ; continue
        
        print_status(myposmon, composmon, is_my, is_com, my_index, com_index)

def game_result(is_user_win, is_com_win): # 게임의 결과를 출력합니다.
    print()
    
    if (is_user_win == True):
        print("[배틀 결과] 당신이 이겼습니다!") ; print() ; print_start() ; start_mode()
    elif (is_com_win == True):
        print("[배틀 결과] 당신이 졌습니다!") ; print() ; print_start() ; start_mode()
        
def com_replace(is_com, com_index): # 컴퓨터의 포스몬이 쓰러졌을 때, 교체하는 과정입니다.
    num_O = 0
    num_O_index = []
    
    for i in range (3):
        if is_com[i] == "O":
            num_O += 1
            num_O_index.append(i)

    while(1):
        com_rand = random.randrange(0, num_O)
        if (num_O_index[com_rand] == com_index):
            continue
        else :
            com_index = num_O_index[com_rand]
            break
    
    return com_index

def user_replace(is_my, my_index): # 유저의 포스몬이 쓰러졌을 대, 교체하는 과정입니다.
    num_O = 0
    num_O_index = []
    
    for i in range(len(is_my)):
        if is_my[i] == "O":
            num_O += 1
            num_O_index.append(i)        
            
    while(1):
        try : 
            user_command = int(input("교체할 포스몬을 고르세요 : "))
        except : print("수행할 수 없는 명령입니다") ; print()
        
        if (user_command in num_O_index):
            print() ; break
        else : print("범위를 벗어났습니다!") ; print()
    
    my_index = user_command
    
    return my_index
        
def attack_oper(skill, myposmon, my_index, toposmon, to_index): # 기술을 사용하는 함수입니다.
    
    if (skill.get_name() == "Change"): # 이미 처리를 했으므로, 그냥 출력만 함.
        pass
    else :
        skill.use(myposmon[my_index], toposmon[to_index])

def calc_skill(attack_name): # 공격 유형을 통해 공격의 클래스와 속도를 리턴
    
    if(attack_name == "Change"):
        skill = Change()
        return skill, skill.get_speed()
    elif(attack_name == "Tackle"):
        skill = Tackle()
        return skill, skill.get_speed()
    elif(attack_name == "ScissorsCross"):
        skill = ScissorsCross()
        return skill, skill.get_speed()
    elif(attack_name == "Swift"):
        skill = Swift()
        return skill, skill.get_speed()
    elif(attack_name == "Growl"):
        skill = Growl()
        return skill, skill.get_speed()
    elif(attack_name == "SwordDance"):
        skill = SwordDance()
        return skill, skill.get_speed()
    elif(attack_name == "TailWhip"):
        skill = TailWhip()
        return skill, skill.get_speed()    

def com_act(composmon, is_com, com_index): # 컴퓨터의 행동과정입니다.
    num_O = 0
    num_O_index = []
    
    for i in range (3):
        if is_com[i] == "O":
            num_O += 1
            num_O_index.append(i)
            
    com_to_select = len(composmon[com_index].get_move()) + 1 # 교체를 고려함.
    
    com_rand = random.randrange(0, com_to_select)

    if (num_O == 1):
        com_rand = random.randrange(1, com_to_select) # 하나 남았을 땐, 교체할 수 없음.

    
    if (com_rand == 0) : # 0알 때를 교체하는 상황으로 봅니다.
        while(1):
            my_rand = random.randrange(0, num_O)
            if (num_O_index[my_rand] == com_index):
                continue
            else :
                com_index = num_O_index[my_rand] # 자기 자신을 제외한 다른 남은 포스몬으로 교체를 진행합니다.
                break
        com_attack = "Change"

        return com_attack, composmon, is_com, com_index
    else : # 공격하는 상황
        com_to_select -= 1
        select_num = random.randrange(0, len(composmon[com_index].get_move()) ) # 사용할 수 있는 기술을 랜덤으로 사용합니다.
        
        com_attack = composmon[com_index].get_move()[select_num]

        return com_attack, composmon, is_com, com_index
        
    
def print_status(myposmon, composmon, is_my, is_com, my_index, com_index): # 포스몬의 정보를 게임 화면과 같이 출력합니다.
    num_my = is_my.count("O")
    num_com = is_com.count("O")
    
    print("############################################")
    print("컴퓨터 포스몬: [%s%s%s] %d / %d" %(is_com[0], is_com[1], is_com[2], num_com, len(is_com)) )
    print("%s    <|%s %d / %d:" % (composmon[com_index].get_name(), composmon[com_index].get_type(), composmon[com_index].get_health(), composmon[com_index].get_max_health() ) )
    print("    vs    ")
    print("%s    <|%s %d / %d:" % (myposmon[my_index].get_name(), myposmon[my_index].get_type(), myposmon[my_index].get_health(), myposmon[my_index].get_max_health() ) )
    print("당신의 포스몬: [", end="")

    for exist in is_my:
        print("%s" %(exist), end="")
        
    print("] %d / %d" %(num_my, len(is_my)))
    print("++++++++++++++++++++++++++++++++++++++++++++")
    if (len(myposmon[my_index].get_move()) == 2):
        print("기술 (0) %s (1) %s" % (myposmon[my_index].get_move()[0], myposmon[my_index].get_move()[1]))
    elif (len(myposmon[my_index].get_move()) == 3):
        print("기술 (0) %s (1) %s (2) %s" % (myposmon[my_index].get_move()[0], myposmon[my_index].get_move()[1], myposmon[my_index].get_move()[2]))
    print("############################################")
    print()

def main():
    print_start()

    start_mode()

main()