from tkinter import *
window = Tk()
window.title("SILAS CALCULATOR")
window.geometry("312x324")
window.resizable(0,0)


operational_value = ""
def update_screen(value):
    global operational_value
    operational_value += value
    But.insert(END, value)
    print(operational_value)

def clear_button():
    global operational_value
    operational_value = ""
    Sample_entry_text.set(operational_value)

Sample_entry_text = StringVar()

def equal_button():
    global operational_value
    result = str(eval(operational_value))
    But.insert(END,result)
    Sample_entry_text.set(result)

Sample_entry_text = StringVar()

#Frame for result
Button_frame = Frame(window,width=312,height=50)
Button_frame.pack(side=TOP)

But = Entry(Button_frame,textvariable=Sample_entry_text,justify=RIGHT,width=50)
But.grid(row=0,column=0,ipady=10)

#frame for rows 
But_frame = Frame(window,width=312,height=50,)
But_frame.pack()

#button for 1st row
Cancel_button = Button(But_frame,text="CANCEL",width=33,height=3,command = lambda:clear_button())
Cancel_button.grid(row=0,column=0,columnspan=3,pady=1,padx=1,sticky="w")


Division = Button(But_frame,text="/",width=10,height=3,command=lambda:update_screen("/"))
Division.grid(row=0,column=3,padx=1,pady=1)

#Button for 2nd row
seven = Button(But_frame,text="7",width=10,height=3,command=lambda:update_screen('7'))
seven.grid(row=1,column=0,padx=1,pady=1)

eight = Button(But_frame,text="8",width=10,height=3,command=lambda:update_screen('8'))
eight.grid(row=1,column=1,padx=1,pady=1)

nine = Button(But_frame,text="9",width=10,height=3,command=lambda:update_screen('9'))
nine.grid(row=1,column=2,padx=1,pady=1)

multiply = Button(But_frame,text="*",width=10,height=3,command=lambda:update_screen("*"))
multiply.grid(row=1,column=3,padx=1,pady=1)

#button for 3rd row
four = Button(But_frame,text="4",width=10,height=3,command=lambda:update_screen('4'))
four.grid(row=2,column=0,padx=1,pady=1)

five = Button(But_frame,text="5",width=10,height=3,command=lambda:update_screen('5'))
five.grid(row=2,column=1,padx=1,pady=1)

six = Button(But_frame,text="6",width=10,height=3,command=lambda:update_screen('6'))
six.grid(row=2,column=2,padx=1,pady=1)

subtract = Button(But_frame,text="-",width=10,height=3,command=lambda:update_screen("-"))
subtract.grid(row=2,column=3,padx=1,pady=1)

#button for 4th row
one = Button(But_frame,text="1",width=10,height=3,command=lambda:update_screen('1'))
one.grid(row=3,column=0,padx=1,pady=1)

two = Button(But_frame,text="2",width=10,height=3,command=lambda:update_screen('2'))
two.grid(row=3,column=1,padx=1,pady=1)

three = Button(But_frame,text="3",width=10,height=3,command=lambda:update_screen('3'))
three.grid(row=3,column=2,padx=1,pady=1)

addition = Button(But_frame,text="+",width=10,height=3,command=lambda:update_screen("+"))
addition.grid(row=3,column=3,padx=1,pady=1)

#button for 4th row
zero = Button(But_frame,text="0",width=20,height=3,command=lambda:update_screen('0'))
zero.grid(row=4,column=0,columnspan=2,padx=1,pady=1)

dot = Button(But_frame,text=".",width=10,height=3,command=lambda:update_screen("."))
dot.grid(row=4,column=2,padx=1,pady=1)

equal = Button(But_frame,text="=",width=10,height=3,command=lambda:equal_button())
equal.grid(row=4,column=3,padx=1,pady=1)


window.mainloop()
