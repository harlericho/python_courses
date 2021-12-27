from tkinter import *
from tkinter import font

# Configure the window
windows = Tk()
windows.title("Calculator")
# windows.geometry("300x300")
windows.resizable(0, 0)
windows.configure(background="black")


# Create the entry box
eText = Entry(windows, font=("Arial", 20))
eText.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create the buttons
button1 = Button(windows, text="1", width=5, height=2, padx=15, pady=5, command=lambda: button_click(1))
button1.grid(row=1, column=0)
button2 = Button(windows, text="2",width=5, height=2, padx=15, pady=5, command=lambda: button_click(2))
button2.grid(row=1, column=1)
button3 = Button(windows, text="3",width=5, height=2, padx=15, pady=5, command=lambda: button_click(3))
button3.grid(row=1, column=2)
button4 = Button(windows, text="4",width=5, height=2, padx=15, pady=5, command=lambda: button_click(4))
button4.grid(row=2, column=0)
button5 = Button(windows, text="5",width=5, height=2, padx=15, pady=5, command=lambda: button_click(5))
button5.grid(row=2, column=1)
button6 = Button(windows, text="6",width=5, height=2, padx=15, pady=5, command=lambda: button_click(6))
button6.grid(row=2, column=2)
button7 = Button(windows, text="7",width=5, height=2, padx=15, pady=5, command=lambda: button_click(7))
button7.grid(row=3, column=0)
button8 = Button(windows, text="8",width=5, height=2, padx=15, pady=5, command=lambda: button_click(8))
button8.grid(row=3, column=1)
button9 = Button(windows, text="9",width=5, height=2, padx=15, pady=5, command=lambda: button_click(9))
button9.grid(row=3, column=2)
button0 = Button(windows, text="0", width=15, height=2, padx=15, pady=5, bg="yellow", fg="black", command=lambda: button_click(0))
button0.grid(row=4, column=0, columnspan=2)

buttonAdd = Button(windows, text="+",width=5, height=2, padx=15, pady=5, bg="green", fg="black", command=lambda: button_click("+"))
buttonAdd.grid(row=5, column=0)
buttonSub = Button(windows, text="-",width=5, height=2, padx=15, pady=5, bg="green", fg="black", command=lambda: button_click("-"))
buttonSub.grid(row=5, column=1)
buttonMul = Button(windows, text="*",width=5, height=2, padx=15, pady=5, bg="green", fg="black", command=lambda: button_click("*"))
buttonMul.grid(row=5, column=2)
buttonDiv = Button(windows, text="/",width=5, height=2, padx=15, pady=5, bg="green", fg="black", command=lambda: button_click("/"))
buttonDiv.grid(row=5, column=3)

buttonEqual = Button(windows, text="=", width=5, height=2, padx=15, pady=5, bg="black", fg="white", command=lambda: operation())
buttonEqual.grid(row=4, column=2)
buttonClear = Button(windows, text="AC", width=5, height=2, padx=15, pady=5, bg="red", fg="white", command=lambda: button_clear())
buttonClear.grid(row=1, column=3)
buttonParenthesis1 = Button(windows, text="(", width=5, height=2, padx=15, pady=5, bg="blue", fg="white", command=lambda: button_click('('))
buttonParenthesis1.grid(row=2, column=3)
buttonParenthesis2 = Button(windows, text=")", width=5, height=2, padx=15, pady=5, bg="blue", fg="white", command=lambda: button_click(')'))
buttonParenthesis2.grid(row=3, column=3)
buttonPoint = Button(windows, text=".", width=5, height=2, padx=15, pady=5, bg="blue", fg="white", command=lambda: button_click('.'))
buttonPoint.grid(row=4, column=3)

value = 0

# function for the buttons
def button_click(number):
    global value
    eText.insert(value, number)
    value += 1
def button_clear():
    eText.delete(0, END)
    value = 0
def operation():
    value = 0
    equation = eText.get()
    result = eval(equation)
    eText.delete(0, END)
    eText.insert(0, result)

# Run the window
windows.mainloop()