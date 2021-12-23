import tkinter as tkinter
from typing import Text
windows = tkinter.Tk() # Creacion de la ventana
windows.title("Tkinter") # Titulo de la ventana
windows.geometry("432x325") # Tamaño de la ventana

# label = tkinter.Label(windows, text="Hola mundo", bg="green") # Creacion de un label
# # label.pack(side=tkinter.BOTTOM) # Colocacion del label
# # label.pack(fill=tkinter.X) # Colocacion del label
# label.pack(fill=tkinter.BOTH, expand=True) # Colocacion del label
# def saludos():
#     print("Hola mundo")

# boton = tkinter.Button(windows, text="Hola mundo", command=saludos) # Creacion de un boton
# boton.pack() # Colocacion del boton
# label = tkinter.Label(windows, bg="green") # Creacion de un label
# label.pack() # Colocacion del label

# caja = tkinter.Entry(windows, font="Helvetica 50") # Creacion de una caja de texto
# caja.pack() # Colocacion de la caja de texto

# def textoCaja():
#     label['text'] = caja.get() # Obtencion del texto de la caja de texto

# # boton = tkinter.Button(windows, text="Hola mundo", command=lambda: print(caja.get())) # Creacion de un boton
# boton = tkinter.Button(windows, text="Hola mundo", command=textoCaja) # Creacion de un boton
# boton.pack() # Colocacion del boton

grid = tkinter.Button(windows, text="GRID", width=10, height=3, bg="yellow", fg="white") # Creacion de un boton
column0 = tkinter.Button(windows, text="Column 0", width=10, height=3, bg="yellow", fg="white") # Creacion de un boton
column1 = tkinter.Button(windows, text="Column 1", width=10, height=3, bg="yellow", fg="white") # Creacion de un boton
column2 = tkinter.Button(windows, text="Column 2", width=10, height=3, bg="yellow", fg="white") # Creacion de un boton
grid.grid(row=0, column=0) # Colocacion del boton
column0.grid(row=0, column=1) # Colocacion del boton
column1.grid(row=0, column=2) # Colocacion del boton
column2.grid(row=0, column=3) # Colocacion del boton


row0 = tkinter.Button(windows, text="row 0", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column0row0 = tkinter.Button(windows, text="Column 0 Row 0", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column1row0 = tkinter.Button(windows, text="Column 1 Row 0", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column2row0 = tkinter.Button(windows, text="Column 2 Row 0", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
row0.grid(row=1, column=0) # Colocacion del boton
column0row0.grid(row=1, column=1) # Colocacion del boton
column1row0.grid(row=1, column=2) # Colocacion del boton
column2row0.grid(row=1, column=3) # Colocacion del boton

row1 = tkinter.Button(windows, text="row 1", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column0row1 = tkinter.Button(windows, text="Column 0 Row 1", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column1row1 = tkinter.Button(windows, text="Column 1 Row 1", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column2row1 = tkinter.Button(windows, text="Column 2 Row 1", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
row1.grid(row=2, column=0) # Colocacion del boton
column0row1.grid(row=2, column=1) # Colocacion del boton
column1row1.grid(row=2, column=2) # Colocacion del boton
column2row1.grid(row=2, column=3) # Colocacion del boton

row2 = tkinter.Button(windows, text="row2", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column0row2 = tkinter.Button(windows, text="Column 0 Row 2", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column1row2 = tkinter.Button(windows, text="Column 1 Row 2", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column2row2 = tkinter.Button(windows, text="Column 2 Row 2", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
row2.grid(row=3, column=0) # Colocacion del boton
column0row2.grid(row=3, column=1) # Colocacion del boton
column1row2.grid(row=3, column=2) # Colocacion del boton
column2row2.grid(row=3, column=3) # Colocacion del boton

row3 = tkinter.Button(windows, text="row 3", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column0row3 = tkinter.Button(windows, text="Column 0 Row 3", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column1row3 = tkinter.Button(windows, text="Column 1 Row 3", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
column2row3 = tkinter.Button(windows, text="Column 2 Row 3", width=10, height=3, bg="gray", fg="white") # Creacion de un boton
row3.grid(row=4, column=0) # Colocacion del boton
column0row3.grid(row=4, column=1) # Colocacion del boton
column1row3.grid(row=4, column=2) # Colocacion del boton
column2row3.grid(row=4, column=3) # Colocacion del boton


windows.mainloop() # registro de eventos de la ventana