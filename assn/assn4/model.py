import random
import tkinter as tk
import app as myapp

TITLE = "Minesweeper" 
BTN_WIDTH = 10
BTN_HEIGHT = 10
NUM_MINE = 10
# 타이틀, 게임의 크기, 지뢰의 숫자를 나타내는 전역 변수.

button_list = [] # 버튼을 담는 리스트.
mylist = [] # 지뢰의 위치를 나타내는 전역 변수.

class Panel(): # 지뢰찾기의 각 칸에 해당하는 클래스
    def __init__(self, body_frame):
        self.isRevealed = False # panel이 밝혀진 상태인지 나타냄.
        self.hasFlag = False # panel이 flag를 보유하고 있는지 나타냄.
        
        self.body_frame = body_frame # 버튼의 구현을 위해 받아옴.

    def toggleFlag(self): # 해당 panel의 hasFlag를 toggle함.
        if self.hasFlag == False:
            self.hasFlag = True
        elif self.hasFlag == True:
            self.hasFlag = False

    def unveil(self): # 해당 panel을 밝혀진 상태로 변경.
        self.isRevealed = True

class EmptyPanel(Panel): # 지뢰가 존재하지 않는 칸을 의미.
    def __init__(self, body_frame):
        super().__init__(body_frame)
        self.hasMine = False # panel이 지뢰를 갖고 있는지 나타냄.
        self.numOfNearMines = 0

    def addNumOfNearMines(self): # 해당 panel의 numOfNearMines 값을 1 증가 시킵니다.
        self.numOfNearMines += 1
        
    def unveil(self): # 부모 class의 unveil을 실행하고, numOfNearMines를 리턴합니다.
        super().unveil()
        return self.numOfNearMines
    
class MinePanel(Panel):
    def __init__(self, body_frame):
        super().__init__(body_frame)
        self.hasMine = True
        self.numOfNearMines = 0

    def addNumOfNearMines(self): # 여기서는 쓰지 않지만, 구현은 해둠.
        pass

    def unveil(self):
        super().unveil()
        return -1 # -1일때 터짐
    
class Board(): # 게임의 틀을 나타내는 합수입니다.
    def __init__(self, body_frame, reset_button):
        self.panels = []

        self.body_frame = body_frame
        self.reset_button = reset_button
        
        self.img1 = tk.PhotoImage(file="imgs/smile.png") # 이미지 로드
        self.img2 = tk.PhotoImage(file="imgs/sunglasses.png")
        self.skull_image = tk.PhotoImage(file="imgs/skull.png")
    
    def reset(self, numMine, height, width): # 보드판을 초기화하는 함수입니다.
        
        self.face_reset() # 리셋 버튼의 이미지 초기화
        
        for widget in self.body_frame.winfo_children(): # 기존에 있던 버튼들 삭제
            widget.destroy()
    
        for r in range(height):
            for c in range(width):
                button=tk.Button(self.body_frame, width=2, height=1)
                button.grid(row=r, column=c)
                
        # 버튼을 생성
                
        mylist.clear()
        self.panels.clear()
        button_list.clear()
        # 지뢰찾기의 진행 상황 등을 나타내는 변수들 초기화

        for i in range(height):
            mylist.append([])
            for j in range(width):
                mylist[i].append(0)
        # 지뢰의 위치를 나타내는 mylisy를 모두 0으로 초기화

        for i in range(numMine):
            while (1):
                my_height = random.randint(0, height -1)
                my_width = random.randint(0, width -1)   

                if (mylist[my_height][my_width] == 1): # 이미 지뢰인 경우 넘어감.
                    continue

                mylist[my_height][my_width] = 1
                break
        # 지뢰의 수만큼 랜덤한 위치에 1 추가

        for i in range(height):
            self.panels.append([])
            for j in range(width):
                if (mylist[i][j] == 1):
                    self.panels[i].append(MinePanel(self.body_frame))
                else : self.panels[i].append(EmptyPanel(self.body_frame))
        # 지뢰의 위치에는 MinePanel을, 아닌 경우 EmptyPanel을 넣어줌.
                
        for r in range(height):
            button_list.append([])
            for c in range(width):
                button=tk.Button(self.body_frame, width=2, height=1)
                button.grid(row=r, column=c)
                button.bind("<Button-1>", lambda event, row=r, col=c : self.unveil(row, col) )
                button.bind("<Button-3>", lambda event, row=r, col=c : self.on_right_click(row, col) )
                
                button_list[r].append(button)
                
        # 버튼을 넣어줌.

        for i in range(height):
            for j in range(width):

                for k in range(3): # 0, 1, 2
                    for l in range(3): # 0, 1, 2
                        try:
                            if (k == 1 and l == 1): # 자신의 경우 넘어감. EmptyPanel만 기록하니 사실상 없어도 됨.
                                continue

                            if (0 <= i+k-1 < BTN_WIDTH and 0 <= j+l-1 < BTN_HEIGHT):
                                if (mylist[i + k - 1][j + l - 1] == 1):
                                    self.panels[i][j].addNumOfNearMines()
                        except: # 인덱스 범위를 넘어가는 경우는 무시합니다.
                            pass
        # numOfNearMines를 기록하는 과정. 주변 8개의 패널을 탐색해 지뢰의 개수를 기록한다.
            
    def getNumOfRevealedPanels(self): # 현재 밝혀져 있는 panel의 개수 반환.
        sum = 0
        
        for r in range(BTN_HEIGHT):
            for c in range(BTN_WIDTH):
                if  self.panels[r][c].isRevealed == True:
                    sum += 1
                    
        return sum

    def unveil(self, y, x): # y행, x열의 Panel을 드러냅니다.
        result = self.panels[y][x].unveil()
        
        if (result == -1):
            self.on_left_click(y, x)
            return -1
        
        # 재귀적으로 반복
        if (self.panels[y][x].numOfNearMines == 0):
            # 밝히기
            for k in range(3): # 0, 1, 2
                    for l in range(3): # 0, 1, 2
                        try:
                            if ( (0 <= y+k-1 < BTN_WIDTH) and (0 <= x+l-1 < BTN_HEIGHT) ): # 인덱스 범위 안에 존재하고,
                                if (self.panels[y+k-1][x+l-1].numOfNearMines == 0 and self.panels[y+k-1][x+l-1].isRevealed == False): # numOfNearMines개수가 0이며, 패널이 드러나지 않았을 때,
                                    if (k == 1 and l == 1): # 자기 자신은 넘어감.
                                        pass
                                    else:
                                        self.panels[y+k-1][x+l-1].isRevealed = True
                                        self.unveil(y+k-1, x+l-1) # 재귀함수로 드러내는 과정을 반복함.
                        except IndexError: # 인덱스를 벗어나는 경우는 실행하지 않음.
                            pass
                        
                        try:
                            if ( (0 <= y+k-1 < BTN_WIDTH) and (0 <= x+l-1 < BTN_HEIGHT) ):
                                self.on_left_click(y+k-1, x+l-1)
                        except IndexError: # 인덱스를 벗어나는 경우는 실행하지 않음.
                            pass        
                        
        else : self.on_left_click(y, x) # 0이 아닌 경우, 그냥 그 위치의 패널을 드러냄.
        
        if (self.getNumOfRevealedPanels() == BTN_WIDTH * BTN_HEIGHT - NUM_MINE): # 모든 지뢰 이외의 패널을 드러냈을 때, 승리.
            self.win()
            
    def toggleFlag(self, y, x): # 해당 위치의 flag를 토글합니다.
        self.panels[y][x].toggleFlag()

    def checkReveal(self, y, x): # 해당 위치의 isRevealed를 리턴합니다.
        return self.panels[y][x].isRevealed

    def checkFlag(self, y, x): # 해당 위치의 hasFlag를 리턴합니다.
        return self.panels[y][x].hasFlag
    
    def checkMine(self, y, x): # 해당 위치의 hasMine를 리턴합니다.
        return self.panels[y][x].hasMine
    
    def getNumOfNearMines(self, y, x): # 해당 위치의 numOfNearMines을 리턴합니다.
        return self.panels[y][x].numOfNearMines
    
        
    def on_left_click(self, row, col): # 버튼을 좌클릭 했을 때, 실행하는 함수
        button = button_list[row][col]
       
        if (mylist[row][col] == 1): # 지뢰일 경우, 게임 종료
            button.config(text = '💣', state=tk.DISABLED, relief=tk.SUNKEN)
            self.game_end()
        else: # 아닌 경우 패널을 드러냄.
            if (self.panels[row][col].numOfNearMines == 0):
                button.config(text = '', state=tk.DISABLED, relief=tk.SUNKEN)
            else: 
                button.config(text = self.panels[row][col].numOfNearMines, state=tk.DISABLED, relief=tk.SUNKEN)
    
        self.panels[row][col].isRevealed = True
      
    def on_right_click(self,row, col): # 버튼을 우클릭 했을 때, 실행하는 함수
        button = button_list[row][col]
        if (self.checkReveal(row, col) == False):
            if (self.checkFlag(row, col) == True): # 토글 되어있을 때, (이미 플래그가 새워져있음..)
                self.panels[row][col].hasFlag = False
                button.config(text = "")
            else : # 플래그가 없을 때
                self.panels[row][col].hasFlag = True
                button.config(text = "🚩")
            
    def game_end(self): # 졌을때.
    
        self.lose()
    
        for r in range(BTN_HEIGHT):
            for c in range(BTN_WIDTH):
            
                button = button_list[r][c] # 모든 패널을 드러내는 과정
            
                if (self.checkMine(r,c)): # mine
                    button.config(text = '💣', state=tk.DISABLED, relief=tk.SUNKEN)
                else:
                    if (self.getNumOfNearMines(r,c) == 0):
                        button.config(text = '', state=tk.DISABLED, relief=tk.SUNKEN)
                    else: 
                        button.config(text = self.getNumOfNearMines(r,c), state=tk.DISABLED, relief=tk.SUNKEN)

    def face_reset(self):
        self.reset_button.config(image=self.img1) # 기본 이미지로 설정

    def win(self):
        self.reset_button.config(image=self.img2) # 이겼을 때, 선글라스의 이미지로 설정
    
    def lose(self):
        self.reset_button.config(image=self.skull_image) # 패배했을 때, 해골의 이미지로 설정