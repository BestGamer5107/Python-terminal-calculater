from tkinter import *

def button_pressed(num):
    global numbers
    str(num).lower()

    if num == "equal":
        try:
            total = eval(numbers)
            label.config(text=total)
        except ZeroDivisionError:
            label.config(text="Error: Division by zero")
            numbers = ""
        except SyntaxError:
            label.config(text="Error: bracket not closed or only symbols are written")
            numbers = ""
    elif num == "delete":
        numbers = numbers[:-1]
        label.config(text=numbers)
    elif num == "clear":
        numbers = ""
        label.config(text=numbers)
    else:
            numbers += num
            label.config(text=numbers)


numbers = ""

window = Tk()
window.title("Password generator")
window.geometry("300x435")
window.config(bg="Black")
window.resizable(False, False)

label = Label(window, font=5, width=26, height=2)
label.pack(pady=10, side=TOP)

buttonframe = Frame(window)
buttonframe.pack(pady=5, side=BOTTOM)

button1 = Button(buttonframe, text="1", width=9, height=4, command= lambda : button_pressed("1"))
button1.grid(row=0, column=0)

button2 = Button(buttonframe, text="2", width=9, height=4, command=lambda:button_pressed("2"))
button2.grid(row=0, column=1)

button3 = Button(buttonframe, text="3", width=9, height=4, command=lambda:button_pressed("3"))
button3.grid(row=0, column=2)

button4 = Button(buttonframe, text="4", width=9, height=4, command=lambda:button_pressed("4"))
button4.grid(row=1, column=0)

button5 = Button(buttonframe, text="5", width=9, height=4, command=lambda:button_pressed("5"))
button5.grid(row=1, column=1)

button6 = Button(buttonframe, text="6", width=9, height=4, command=lambda:button_pressed("6"))
button6.grid(row=1, column=2)

button7 = Button(buttonframe, text="7", width=9, height=4, command=lambda:button_pressed("7"))
button7.grid(row=2, column=0)

button8 = Button(buttonframe, text="8", width=9, height=4, command=lambda:button_pressed("8"))
button8.grid(row=2, column=1)

button9 = Button(buttonframe, text="9", width=9, height=4, command=lambda:button_pressed("9"))
button9.grid(row=2, column=2)

button0 = Button(buttonframe, text="0", width=9, height=4, command=lambda:button_pressed("0"))
button0.grid(row=3, column=1)

divide = Button(buttonframe, text="/", width=9, height=4, command=lambda:button_pressed("/"))
divide.grid(row=0, column=3)

multiply = Button(buttonframe, text="*", width=9, height=4, command=lambda:button_pressed("*"))
multiply.grid(row=1, column=3)

minus = Button(buttonframe, text="-", width=9, height=4, command=lambda:button_pressed("-"))
minus.grid(row=2, column=3)

plus = Button(buttonframe, text="+", width=9, height=4, command=lambda:button_pressed("+"))
plus.grid(row=3, column=3)

leftbracket = Button(buttonframe, text="(", width=9, height=4, command=lambda:button_pressed("("))
leftbracket.grid(row=3, column=0)

rightbracket = Button(buttonframe, text=")", width=9, height=4, command=lambda:button_pressed(")"))
rightbracket.grid(row=3, column=2)

clear = Button(buttonframe, text="Clear", width=9, height=4, command=lambda:button_pressed("clear"))
clear.grid(row=4, column=0)

decimal = Button(buttonframe, text=".", width=9, height=4, command=lambda:button_pressed("."))
decimal.grid(row=4, column=1)

delete = Button(buttonframe, text="Delete", width=9, height=4, command=lambda:button_pressed("delete"))
delete.grid(row=4, column=2)

equal = Button(buttonframe, text="=", width=9, height=4, command=lambda:button_pressed("equal"))
equal.grid(row=4, column=3)

window.mainloop()