#Se importa la libreria tkinter con todas sus funciones
from tkinter import *

#---------------------------------
#Funciones de la app
#---------------------------------

import random

#Variables
BASE=460
ALTURA=220





#---------------------------------
#ventana principal
#---------------------------------

#se declara una variable llamada "ventana_principal" que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk( )

#Titulo de la ventana
ventana_principal.title("Sistema UIS Socorro")

#Tamaño de la ventana
ventana_principal.geometry("500x500")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fonde de la ventana
ventana_principal.config(bg="black")

#frame de graficacion
Frame_graficacion = Frame(ventana_principal)
Frame_graficacion.config(bg="white", width=480, height=240)
Frame_graficacion.place(x=10 , y=10)

#Creacion canvas
c = Canvas(Frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

#graficacion
x=10
y=10
"""for i in range(100):
    circulo= c.create_oval(x,y, x+20, y+20, fill="red")
    x= x + 30
    y= y + 30"""

#graficacion2 (para que no se salga del canva)
x=10
y=10
"""for i in range(100):
    circulo= c.create_oval(x,y, x+20, y+20, fill="red")
    x= random.randint(0, BASE-20)
    y= random.randint(0,ALTURA-20)"""

#graficacion3 (para que no se salga del canva y que cada color sea diferente)
x=10
y=10
for i in range(100):
    x= random.randint(0, BASE-20)
    y= random.randint(0,ALTURA-20)
    color="#"
    for caracter in range(6):
        color = color+random.choice("0123456789ABCDEF")
    circulo= c.create_oval(x,y, x+20, y+20, fill=color)
    



#Desplegar ventana
ventana_principal.mainloop()