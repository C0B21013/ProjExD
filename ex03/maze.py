import tkinter as tk

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canv = tk.Canvas(root, width=1500,height=900,bg="black")
    canv.pack()

    tori = tk.PhotoImage(file="C:/Users/C0B21013/Documents/ProjExD2022/fig/3.png")
    cx,cy = 300, 400 #効果トンの座標
    canv.create_image(cx,cy,image=tori,tag="tori")

    key = "" #現在押されているキー
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    root.mainloop()