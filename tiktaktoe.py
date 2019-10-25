from tkinter import *
import itertools
import tkinter.messagebox
root=Tk()
root.configure(background="yellow")
root.title("TIK TAK TOE")

def Active():
    global l1
    l1=Label(root,text="Player 1",bg="red",width=18,font=("arial",10,"bold"))
    l1.grid(row=3,column=0)
    for b in l:
        b["state"]='active'
        
def Player1(t):
    global pl1
    global l1
    global l2
    global count
    global l
    global turn
    turn=False
    root.configure(background="red")
    l1.destroy()
    l2=Label(root,text="Player 2",bg="blue",width=18,font=("arial",10,"bold"))
    l2.grid(row=3,column=2)
    count=count+1
    pl1.append(t[0]*3+t[1]+1)
    l[t[0]*3+t[1]]['bg']='red'
    if count>=5:
        f=Result(pl1)
        if f:
            tkinter.messagebox.showinfo("Result","Player 1 win")
            Clear()
            return
    if count==9:
        tkinter.messagebox.showinfo("Result","Draw")
        Clear()

def Player2(t):
    global pl2
    global l1
    global l2
    global count
    global l
    global turn
    turn=True
    root.configure(background="Blue")
    l2.destroy()
    l1=Label(root,text="Player 2",bg="blue",width=18,font=("arial",10,"bold"))
    l1.grid(row=3,column=2)
    count=count+1
    pl1.append(t[0]*3+t[1]+1)
    l[t[0]*3+t[1]]['bg']='blue'
    if count>=5:
        f=Result(pl2)
        if f:
            tkinter.messagebox.showinfo("Result","Player 2 win")
            Clear()
            return
    if count==9:
        tkinter.messagebox.showinfo("Result","Draw")
        Clear()
def Result(p1):
    win=[(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7),(1,4,7),(2,5,8),(3,6,9)]
    for i in itertools.permutations(p1,3):
        if j in win:
            return True
        else:
            return False
def Clear():
    global pl2
    global pl1
    global l1
    global l2
    global count
    global l
    global turn
    turn=True
    count=0
    root.configure(background="yellow")
    l1.destroy()
    l2.destroy()
    pl1.clear()
    pl2.clear()
    l.clear()
    for i in range(3):
        for j in range(3):
            l.append(Button(root,state="disable",width=18,height=6,command= lambda t=(i,j):Player1(t) if turn==True else Player2(t)))
            l[-1].grid(row=i,column=j)
l=[]
count=0
pl1=[]
pl2=[]
turn=True
for i in range(3):
        for j in range(3):
            l.append(Button(root,state="disable",width=18,height=6,command= lambda t=(i,j):Player1(t) if turn==True else Player2(t)))
            l[-1].grid(row=i,column=j)

start=Button(root,text="start",bg="powder blue",command=Active,font=("arial",20,"bold"),width=5,height=2).grid(row=3,column=1)
root.mainloop()
