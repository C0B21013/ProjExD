from ast import Delete
from calendar import c
import tkinter as tk
import maze_maker as mm

#タイマー機能
def count_up():
    global tmr
    tmr = tmr+1
    label["text"]=tmr
    root.after(1000,count_up)


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global mx, my
    global cx, cy
    global tori

    if key =="Up":
        tori = tk.PhotoImage(file="fig/5.png")
        my -= 1
    if key =="Down":
        tori = tk.PhotoImage(file="fig/5.png")
        my += 1
    if key =="Left":
        tori = tk.PhotoImage(file="fig/0.png")
        mx -= 1
    if key =="Right":
        tori = tk.PhotoImage(file="fig/2.png")
        mx += 1
    if maze_list[my][mx]==0:
        cx, cy =mx*100 + 50, my*100 +50

    else:
        if key =="Up":
            my += 1
        if key =="Down":
            my -= 1
        if key =="Left":
            mx += 1
        if key =="Right":
            mx -= 1
            tori = tk.PhotoImage(file="fig/8.png")

    #こうかとんの移動、画像切り替え
    canv.delete("tori")
    canv.create_image(cx,cy,image=tori,tag="tori")
    root.after(150,main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    label = tk.Label(root,font=("",15))
    label.pack()
    tmr = 0
    root.after(1000, count_up)

    canv = tk.Canvas(root, width=1500,height=900,bg="black")
    canv.pack()

    maze_list= mm.make_maze(15,9)
    mm.show_maze(canv,maze_list)
    
    tori = tk.PhotoImage(file="fig/0.png")
    mx, my = 1, 1
    cx, cy = mx*100 + 50, my*100 +50
    canv.create_image(cx,cy,image=tori,tag="tori")

    key = "" 
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()

    root.mainloop()