import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# Interfaz grafica
def crearWidget():
    etiquetaGuardar = Label(ventana, 
    text="Guardar como:", font=("", 10,"bold"))
    etiquetaGuardar.grid(row=1, column=0, padx=5, pady=5)
    
    ventana.textGuardar = Entry(ventana, width=30)
    ventana.textGuardar.grid(row=1, column=1, padx=5, pady=5)

    botonGuardar = Button(ventana, text="Guardar", width=10, command=navegarPantalla)
    botonGuardar.grid(row=1, column=2, padx=5, pady=5)

    botonCaptura = Button(ventana, text="Capturar", width=10, command=capturarPantalla)
    botonCaptura.grid(row=2, column=1, padx=5, pady=5)

# Funcion para navegar y guardar la pantalla
def navegarPantalla():
    ventana.archivoNombre = filedialog.asksaveasfilename(title="Guardar como:",
    initialdir="./",
    defaultextension=".png",filetypes=(("Archivos PNG", "*.png"), ("Todos los archivos", "*.*")))

    ventana.textGuardar.insert("1", ventana.archivoNombre)

# Funcion para capturar la pantalla
def capturarPantalla():
    # captura = pyautogui.screenshot()
    # captura.save(ventana.archivoNombre)
    pyautogui.screenshot(ventana.archivoNombre)
    messagebox.showinfo("Captura", "Captura guardada")

ventana = Tk()
ventana.title("Captura de pantalla")
crearWidget()
ventana.mainloop()