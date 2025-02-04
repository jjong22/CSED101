import tkinter as tk
import model

class App(tk.Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        
        self.master.title(model.TITLE)
    
        self.header_frame = tk.Frame(master)
        self.header_frame.pack()
        
        self.body_frame = tk.Frame(master)
        self.body_frame.pack()
        
        self.img1 = tk.PhotoImage(file="imgs/smile.png") # 이미지 로드
        self.img2 = tk.PhotoImage(file="imgs/sunglasses.png")
        self.skull_image = tk.PhotoImage(file="imgs/skull.png")
    
        self.reset_button = tk.Button(self.header_frame, image=self.img1)
        self.reset_button.pack(pady = 10) 
    
        self.reset_button.bind('<Button-1>', reset_button_left)
        
        master.title(model.TITLE)
        self.board = model.Board(self.body_frame, self.reset_button) # button에 대한 함수처리를 위해 body_frame과 reset_button을 매개변수로 넣어 만듭니다.
    

def reset_button_left(event): # reset_button을 좌클릭했을 때, 리셋합니다. 
    app.board.reset(model.NUM_MINE, model.BTN_HEIGHT, model.BTN_WIDTH)

def easy_mode(): # 이지모드로 설정 후, 리셋합니다.
    model.BTN_WIDTH = 10
    model.BTN_HEIGHT = 10
    model.NUM_MINE = 10
    app.board.reset(model.NUM_MINE, model.BTN_HEIGHT, model.BTN_WIDTH)
    
def normal_mode(): # 노말모드로 설정 후, 리셋합니다.
    model.BTN_WIDTH = 15
    model.BTN_HEIGHT = 15
    model.NUM_MINE = 30
    app.board.reset(model.NUM_MINE, model.BTN_HEIGHT, model.BTN_WIDTH)
    
def hard_mode(): # 하드모드로 설정 후, 리셋합니다.
    model.BTN_WIDTH = 20
    model.BTN_HEIGHT = 20
    model.NUM_MINE = 50
    app.board.reset(model.NUM_MINE, model.BTN_HEIGHT, model.BTN_WIDTH)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    
    app.board.reset(model.NUM_MINE, model.BTN_HEIGHT, model.BTN_WIDTH)
    
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    level_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="난이도", menu=level_menu)

    level_menu.add_command(label="초급", command=lambda: easy_mode())
    level_menu.add_command(label="중급", command=lambda: normal_mode())
    level_menu.add_command(label="고급", command=lambda: hard_mode())

    app.mainloop()
        