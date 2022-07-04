#importing the required libraries
from tkinter import *
import datetime as dt 
import time
import math
import tkinter as Tkinter


#window interface 
clock= Tk()
clock.title("Clock app")
clock.configure(bg="black")
clock.geometry("400x400")

#creating a date picker
date=dt.datetime.now()
#create label to display date
date= Label(clock,text=f"{date: %A, %B %d, %Y}", font=("Arial bold",20), bg="black", fg="white")
date.pack()

#creating digital clock
    #function that display the present time
def dig_time():
    #display time in the 12 hour format
    display_time=time.strftime("%I:%M:%S %p ")
    dig_clock.config(text= display_time)
    dig_clock.after(200,dig_time)

dig_clock=Label(clock,font=("Arial",50),bg="black", fg="white")
dig_clock.pack()
dig_time()





clock.mainloop()