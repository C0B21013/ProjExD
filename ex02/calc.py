import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("calc")
root.geometry("375x440")
root.resizable(width=False, height=False)

def num_click(event): #数字をクリックした際の反応
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END,txt)

def equal_click(event):
    eq=entry.get()
    res=eval(eq)
    entry.delete(0,tk.END)
    entry.insert(tk.END,res)

def clear_click(event):
    entry.delete(0,tk.END)

def sq_click(event):
    sq=int(entry.get())
    res=sq*sq
    entry.delete(0,tk.END)
    entry.insert(tk.END,res)

def per_click(event):
    per=int(entry.get())
    res=per/100
    entry.delete(0,tk.END)
    entry.insert(tk.END,res)

entry = tk.Entry(font=("Times New Roman",50),width=10,justify='right')
entry.grid(row=0,column=0,columnspan=4)

button = tk.Button(text="％",font=("Ricty Diminished",30),width=4,height=1)
button.bind("<1>",per_click)
button.grid(row = 1, column = 1)

button = tk.Button(text="x²",font=("Ricty Diminished",30),width=4,height=1)
button.bind("<1>",sq_click)
button.grid(row = 1, column = 2)

button = tk.Button(text="C",font=("Ricty Diminished",30),width=4,height=1)
button.bind("<1>",clear_click)
button.grid(row = 1, column = 3)

button = tk.Button(text="/",font=("Ricty Diminished",30),width=4,height=1)
button.bind("<1>",num_click)
button.grid(row = 2, column = 3)

button = tk.Button(text="*",font=("Ricty Diminished",30),width=4,height=1)
button.bind("<1>",num_click)
button.grid(row = 3, column = 3)

button = tk.Button(text="-",font=("Ricty Diminished",30),width=4,height=1)
button.bind("<1>",num_click)
button.grid(row = 4, column = 3)

button = tk.Button(text="+",font=("Ricty Diminished",30),width=4,height=1)
button.bind("<1>",num_click)
button.grid(row = 5, column = 3)

button = tk.Button(text="=",font=("Ricty Diminished",30),width=4,height=1)
button.bind("<1>",equal_click)
button.grid(row = 5, column = 2)

button = tk.Button(text=".",font=("Ricty Diminished",30),width=4,height=1)
button.bind("<1>",num_click)
button.grid(row = 5, column = 1)

    

r, c = 2, 0
for i, num in enumerate(range(9,-1,-1),1):
    button=tk.Button(root, text=f"{num}",font=("Ricty Diminished",30),width=4,height=1)
    button.grid(row = r, column = c)
    button.bind("<1>",num_click)
    c +=1 
    if i%3==0:
        r+=1
        c=0

root.mainloop()
