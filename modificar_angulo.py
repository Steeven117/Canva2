#Se importa la libreria tkinter con todas sus funciones
from tkinter import *


import random

#Variables
BASE=460
ALTURA=220
RADIO=50


#---------------------------------
#Funciones de la app
#---------------------------------

def modificar_arco(angulo):
    c.itemconfig(arco, extent=angulo)

#---------------------------------
#ventana principal
#---------------------------------

#se declara una variable llamada "ventana_principal" que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk( )

#Titulo de la ventana
ventana_principal.title("Sistema UIS Socorro")

#Tamaño de la ventana
ventana_principal.geometry("600x500")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fonde de la ventana
ventana_principal.config(bg="black")

#frame de graficacion
Frame_graficacion = Frame(ventana_principal)
Frame_graficacion.config(bg="white", width=580, height=240)
Frame_graficacion.place(x=10 , y=10)

#Creacion canvas
c = Canvas(Frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=60, y=10)

#ARCO
arco= c.create_arc(BASE/2 - RADIO, ALTURA/2 - RADIO, BASE/2 + RADIO, ALTURA/2 + RADIO, start=0, extent=0, fill="blue", )

#Frame de controles
frame_controles=Frame(ventana_principal)
frame_controles.config(bg="green", width=580, height=240)
frame_controles.place(x=10, y=260)

#barra de deslizamiento
barra_deslizamiento=Scale(frame_controles, label="Angulo", from_=0, to=360, orient="horizontal", length=550, tickinterval=45, command=modificar_arco)
barra_deslizamiento.place(x=10, y=10)






#Desplegar ventana
ventana_principal.mainloop()