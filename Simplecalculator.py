#import tkinter, just the module we're using for the gui
#time is for the mainloop
from Tkinter import *
import time 


tk = Tk()
canvas = Canvas(tk, width=400, height=360)
canvas.pack()
tk.title("Calculator")
canvas.configure(bg='#253f4b') 
tk.resizable(False, False)
#tkinter code to set the canvas and display it on the screen


number_inp = StringVar()



#adds textbox
expression_field = Entry(tk, width=37, textvariable=number_inp)
expression_field.place(x=30, y=40)

calc_value = ""

def press(x):
   global calc_value 
   calc_value = calc_value + str(x)
   number_inp.set(calc_value)
   

def calculate():
   global calc_value 
   total = str(eval(calc_value))
   number_inp.set(total)
   
def clear_input():
  global calc_value  
  calc_value = ""
  number_inp.set("")



   



#NOTE:each of these buttons are exactly 70 left and 70 right in terms of distance from
#their neighbors. Why? the number of 70 feels juuust far enough 
#without making the buttons feel too spaced apart

#creates button on canvas (this button will map to the number 1 later) 
btn1 = Button(tk, text='1', width=3, height=2, bg='GREY', bd='0', command=lambda: press(1))
btn1.place(x=30, y=90)

#creates button on canvas (this button will map to the number 2 later)
btn2 = Button(tk, text='2', width=3, height=2, bg='GREY', bd='0', command=lambda: press(2))
btn2.place(x=100, y=90)
 
#creates a button that will map to 3 later
btn3 = Button(tk, text='3', width=3, height=2, bg='GREY', bd='0', command=lambda: press(3))
btn3.place(x=170, y=90)

#this button will map to 4 later
btn4 = Button(tk, text='4', width=3, height=2, bg='GREY', bd='0', command=lambda: press(4))
btn4.place(x=30, y=160)

#this button will map to 5
btn5 = Button(tk, text='5', width=3, height=2, bg='GREY', bd='0', command=lambda: press(5))
btn5.place(x=100, y=160)

#this button will map to 6
btn6 = Button(tk, text='6', width=3, height=2, bg='GREY', bd='0', command=lambda: press(6))
btn6.place(x=170, y=160)

#this button will map to 7
btn7 = Button(tk, text='7', width=3, height=2, bg='GREY', bd='0', command=lambda: press(7))
btn7.place(x=30, y=230)

#this button will map to 8
btn8 = Button(tk, text='8', width=3, height=2, bg='GREY', bd='0', command=lambda: press(8))
btn8.place(x=100, y=230)

#this button will map to 9
btn9 = Button(tk, text='9', width=3, height=2, bg='GREY', bd='0', command=lambda: press(9))
btn9.place(x=170, y=230)

#this button will map to 0
btn0 = Button(tk, text='0', width=3, height=2, bg='GREY', bd='0', command=lambda: press(0))
btn0.place(x=100, y=300)

#plus button
btn_plus = Button(tk, text='+', width=3, height=2, bg='GREY', bd='0', command=lambda: press("+"))
btn_plus.place(x=240, y=90)

#subtraction buttonclear_input
btn_subt = Button(tk, text='-', width=3, height=2, bg='GREY', bd='0', command=lambda: press("-"))
btn_subt.place(x=310, y=90)

#division button
btn_div = Button(tk, text='/', width=3, height=2, bg='GREY', bd='0', command=lambda: press("/"))
btn_div.place(x=310, y=160)

#multiplication button
btn_mult = Button(tk, text='x', width=3, height=2, bg='GREY', bd='0', command=lambda: press("*"))
btn_mult.place(x=240, y=160)

#equal button, finishes equation
btn_equal = Button(tk, text='=', width=3, height=2, bg='GREY', bd='0', command=calculate)
btn_equal.place(x=240, y=230)

#clears equation button
btn_clear = Button(tk, text='C', width=3, height=2, bg='GREY', bd='0', command=clear_input)
btn_clear.place(x=310, y=230)






while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    
