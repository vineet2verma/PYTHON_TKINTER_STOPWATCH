import random
from tkinter import ttk
from tkinter import *
import datetime as dt

class App():
    def __init__(self,main):
        self.update_time = ''
        self.running = False
        self.hour = 0
        self.minute = 0
        self.sec = 0
        self.new = 0
        self.frame()


    def frame(self):
        self.bg_color = "#333333"
        self.f1 = Frame(bg=self.bg_color)
        self.font = ('Arial 15 bold')
        self.f1.place(x=0,y=0,width=700,height=199)
        self.lbl1 = Label(self.f1,text="STOP WATCH",bg=self.bg_color,fg="black",font=('Arial 30 bold'))
        self.lbl1.place(x=30,y=10,width=400)
        self.stop_watch = Label(self.f1, text="00:00:00", bg=self.bg_color,fg="black",font=('Arial 40 bold'))
        self.stop_watch.place(x=125, y=60)

        self.btn_start = Button(self.f1, text="START",command=self.start,font=self.font)
        self.btn_start.place(x=70, y=150, width=100, height=30)
        self.changeOnHover(self.btn_start, "Green", "White")

        self.btn_pause = Button(self.f1, text="PAUSE",command=self.pause,font=self.font,borderwidth=0,state=DISABLED)
        self.btn_pause.place(x=180, y=150, width=100, height=30)
        self.changeOnHover(self.btn_pause, "red", "White")

        self.btn_exit = Button(self.f1, text="EXIT", command=self.exit,font=self.font,borderwidth=0)
        self.btn_exit.place(x=290, y=150, width=100, height=30)
        self.changeOnHover(self.btn_exit, "red", "White")
    def start(self):
        if not self.running:
            self.stop_watch.after(1000)
            self.update()
            self.running = True
            self.btn_exit.config(text="RESET",command=self.reset)
            self.btn_pause.config(state="normal")
    def pause(self):
        if self.running:
            self.stop_watch.after_cancel(self.update_time)
            self.running = False
            self.btn_pause.config(state="disabled")
            # self.btn_exit.config(text="EXIT", command=self.exit)
    def reset(self):
        if self.running:
            self.stop_watch.after_cancel(self.update_time)
            self.running = False
        self.hour,self.minute,self.sec = 0,0,0
        self.stop_watch.config(text="00:00:00")
        self.btn_exit.config(text="EXIT", command=self.exit)
    def update(self):
        self.sec += 1
        if self.sec == 60:
            self.minute += 1
            self.sec = 0
        if self.sec == 60:
            self.hour += 1
            self.minute = 0
        hours_string = f'{self.hour}' if self.hour > 9 else f'0{self.hour}'
        minutes_string = f'{self.minute}' if self.minute > 9 else f'0{self.minute}'
        seconds_string = f'{self.sec}' if self.sec > 9 else f'0{self.sec}'
        self.stop_watch.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
        self.update_time = self.stop_watch .after(1000, self.update)

        if self.sec % 3==0:
            self.new += 3
            self.bgcolor()
    def changeOnHover(self,button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))
    def exit(self):
        main.quit()
    def bgcolor(self):
        list = ['yellow','green','brown','purple','indigo','white','orange','blue','cyan','mint']
        bg_val=random.choice(list)
        self.f1.config(bg=bg_val)
        self.stop_watch.config(bg=bg_val)
        self.lbl1.config(bg=bg_val)
        self.btn_start.config(bg=bg_val,borderwidth=0)
        self.btn_pause.config(bg=bg_val,borderwidth=0)
        self.btn_exit.config(bg=bg_val,borderwidth=0)
    


if __name__ == "__main__":
    print("Run",__name__)
    main = Tk()
    main.title("Stop Watch")
    main.geometry("450x200+600+50")
    App(main)
    main.mainloop()
