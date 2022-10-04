import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("calc")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]のボタンをクリック")

r, c = 0, 0
for i, num in enumerate(range(9,-1,-1),1):
    button=tk.Button(root, text=f"{num}",font=("Ricty Diminished",30),width=4,height=2)
    button.grid(row = r, column = c)
    button.bind("<1>",button_click)
    c +=1 
    if i%3==0:
        r+=1
        c=0

root.mainloop()
