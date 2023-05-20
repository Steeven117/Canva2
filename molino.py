import random
from tkinter import*
from tkinter import messagebox, ttk

#Variables
BASE=460
ALTURA=220
RADIO=50
# funcion para modificar arco
def modificar_arco(angulo):
    c.itemconfig(aspa1,start=int(angulo)+45)  
    c.itemconfig(aspa2,start=int(angulo)+135) 
    c.itemconfig(aspa3,start=int(angulo)+225)
    c.itemconfig(aspa4,start=int(angulo)+315)
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

#arco
"""arco= c.create_arc(BASE/2 - RADIO, ALTURA/2 - RADIO, BASE/2 + RADIO, ALTURA/2 + RADIO, start=0, extent=0, fill="blue", )"""

# aspas
aspa1 = c.create_arc(BASE/2 -RADIO , ALTURA/2-RADIO , BASE/2 + RADIO , ALTURA/2 + RADIO , start=0 , extent=45 , fill="blue")
aspa2 = c.create_arc(BASE/2 -RADIO , ALTURA/2-RADIO , BASE/2 + RADIO , ALTURA/2 + RADIO , start=90 , extent=45 , fill="yellow")
aspa3 = c.create_arc(BASE/2 -RADIO , ALTURA/2-RADIO , BASE/2 + RADIO , ALTURA/2 + RADIO , start=180 , extent=45 , fill="red")
aspa4 = c.create_arc(BASE/2 -RADIO , ALTURA/2-RADIO , BASE/2 + RADIO , ALTURA/2 + RADIO , start=270 , extent=45 , fill="green")
                     
# frame de controles
frame_controles= Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

# barra de deslizamiento
barra_deslizamiento=Scale(frame_controles, label="angulo", from_=0, to=360, orient="horizontal", length=460, tickinterval=45,command=modificar_arco)
barra_deslizamiento.place(x=10, y=10)

# triangulo
triangulo = c.create_polygon(BASE*2/5,ALTURA, BASE/2, ALTURA/2, BASE*3/5, ALTURA, fill="purple")



#Desplegar ventana
ventana_principal.mainloop()