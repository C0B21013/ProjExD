import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("calc")
root.geometry("300x500")

def num_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END,txt)
    #tkm.showinfo(txt,f"[{txt}]のボタンをクリック")

def equal_click(event):
    eq=entry.get()
    res=eval(eq)
    entry.delete(0,tk.END)
    entry.insert(tk.END,res)

entry = tk.Entry(font=("Times New Roman",40),width=10,justify='right')
entry.grid(row=0,column=0,columnspan=3)

button = tk.Button(text="+",font=("Ricty Diminished",30),width=4,height=2)
button.bind("<1>",num_click)
button.grid(row = 4, column = 1)

button = tk.Button(text="=",font=("Ricty Diminished",30),width=4,height=2)
button.bind("<1>",equal_click)
button.grid(row = 4, column = 2)

r, c = 1, 0
for i, num in enumerate(range(9,-1,-1),1):
    button=tk.Button(root, text=f"{num}",font=("Ricty Diminished",30),width=4,height=2)
    button.grid(row = r, column = c)
    button.bind("<1>",num_click)
    c +=1 
    if i%3==0:
        r+=1
        c=0

root.mainloop()
