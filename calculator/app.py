import tkinter as tk

# Function to calculate the path
def summation():
    sum = int(number1.get()) + int(number2.get())
    return var.set(sum)

def clean():
    number1.delete(0, tk.END)
    number2.delete(0, tk.END)
    result.config(text="")
    var.set("")


# Configure the window
windows = tk.Tk()
windows.title("Calculator-Summation")
windows.geometry("300x300")
windows.resizable(0, 0)
windows.configure(background="white")
var = tk.StringVar() # Create a variable function

# Create a label and textbox
tag1 = tk.Label(windows, text="Enter the numbers first:", bg="white", fg="black")
tag1.pack(padx=10, pady=10, fill=tk.X)
number1 = tk.Entry(windows, width=10)
number1.pack(padx=10, pady=10, fill=tk.X)
number1.focus()

tag2 = tk.Label(windows, text="Enter the numbers second:", bg="white", fg="black")
tag2.pack(padx=10, pady=10, fill=tk.X)
number2 = tk.Entry(windows, width=10)
number2.pack(padx=10, pady=10, fill=tk.X)

# Create a button
botonSummation = tk.Button(windows, text="Summation", command=summation)
botonSummation.pack(padx=10, pady=10, fill=tk.X, side=tk.TOP)
botonClean = tk.Button(windows, text="Clean", command=clean)
botonClean.pack(padx=10, pady=10, fill=tk.X, side=tk.TOP)

# Show the result label
result = tk.Label(windows, textvariable=var, bg="white", fg="green", padx=10, pady=10, font=("Arial", 12), width=10)
result.pack(padx=10, pady=10, fill=tk.X)

# INITIALIZATION
windows.mainloop()