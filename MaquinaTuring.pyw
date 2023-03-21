from tkinter import *
from tkinter.scrolledtext import ScrolledText
import turing as MT
import workString as work

class Interfaz:
    def __init__(self, ventana):
        #Inicializar la ventana con un título
        self.ventana = ventana
        self.ventana.title("Maquina de Turing")
        self.ventana.resizable(False,False)
        self.ventana.iconbitmap("logo.ico")
        self.ventana.geometry("650x310")
        self.ventana.config(bg="light blue")

        #Textos en pantalla
        texto1 = Label(self.ventana, text=" Estado Inicial: ", bg="light blue").place(x = 4, y = 4)
        texto2 = Label(self.ventana, text=" Estado Final: ", bg="light blue").place(x = 4, y = 34)
        texto3 = Label(self.ventana, text=" Transciciones: ", bg="light blue").place(x = 4, y = 64)
        texto4 = Label(self.ventana, text=" Palabra: ", bg="light blue").place(x = 360, y = 4)
        texto6 = Label(self.ventana, text=" NOTA: Los blancos están denotados por el símbolo '#'", bg="light blue", fg="blue").place(x = 0, y = 207)
        texto7 = Label(self.ventana, text=" Los estados son escritos como números enteros positivos, incluyendo el 0", bg="light blue", fg="blue").place(x = 0, y = 227)
        texto8 = Label(self.ventana, text=" Cada función de transicion debe ser separada por un salto de linea", bg="light blue",fg="blue").place(x = 0, y = 247)
        texto9 = Label(self.ventana, text=" Cada función de transicion tiene la forma: estado_actual,simbolo_actual,nuevo_estado,nuevo_simbolo,dirección", bg="light blue",fg="blue").place(x = 0, y = 267)
        texto10 = Label(self.ventana, text=" \tEJEMPLO: 0,a,1,X,D", bg="light blue",fg="green").place(x = 0, y = 287)

        #Mensaje de verificación
        texto5 = Label(self.ventana, bg="light blue", font = (20))

        #campos de texto
        caja1 = Text(self.ventana, height = 1, width = 16)
        caja1.place(x = 120, y = 4)
        caja2 = Text(self.ventana, height = 1, width = 16)
        caja2.place(x = 120, y = 34)
        caja3 = ScrolledText(self.ventana, height = 8, width = 25)
        caja3.place(x = 120, y = 64)
        caja4 = Text(self.ventana, height = 2, width = 25)
        caja4.place(x = 430, y = 4)

        #función del botón verificador (boton1)
        def verificar():
            estado_inicial = caja1.get(1.0,"end-1c")
            estado_final = caja2.get(1.0,"end-1c")
            transicion = caja3.get(1.0,"end-1c")
            palabra = caja4.get(1.0,"end-1c")
            
            registro = work.workString(transicion)
            booleano = MT.turing(registro,palabra,int(estado_inicial),int(estado_final))
            
            if(booleano):texto5.config(text="Palabra aceptada",fg="green") 
            else:texto5.config(text="Palabra rechazada",fg="red")
            texto5.place(x = 435, y = 100)

        #botón verificador
        boton1 = Button(self.ventana, text="verificar", width=10, height=1, command=verificar).place(x = 460, y = 60)

#ventana principal
ventana_principal = Tk()
maquina = Interfaz(ventana_principal)
ventana_principal.mainloop()
