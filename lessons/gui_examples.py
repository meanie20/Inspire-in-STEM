#!/usr/bin/python

#GUI EXAMPLES
################################################################################
#   Name: Evelyn Wangui
#   Date: 07-06-2022
###############################################################################
from cProfile import label
from tkinter import *
from tkinter import font

window=Tk()
window.title("Welcome to my app")
window.configure(bg='black')
window.geometry("400x400")

f_name = Label(window, text = "First Name:",font=("Arial",20))
s_name = Label(window, text = "Second Name:",font=("Arial",20))
f_name.grid(column=60, row=100)
s_name.grid(column=60, row=120)

f_name_box=Entry(window,width=30)
s_name_box=Entry(window,width=30)
f_name_box.grid(column=130,row=100)
s_name_box.grid(column=130,row=120)

def open_popup():
    top=Toplevel(window)
    top.geometry("300x300")
    top.title("Pop up window")
    top.configure(bg="brown")
    msg=Label(top,text="Welcome to the pop up").place(x=150,y=150)

submit=Button(window,text="Submit",bg="white",width=30,command=open_popup().pack())
submit.grid(column=100,row=300)
#reversal of a number
#built an analog clock and digital clock display time and date
#create a form which prompt user input first,name,password and it has a link to another page that display photo,first,second name,favorite movie


window.mainloop()

