import tkinter as tk
from tkinter import messagebox
import re

class Validar:

    def operar(self):
        try:
            expresion=str(entrada1.get())

            if(patron.match(expresion)):

                return var.set("¡Es correcta la expresión!")
            else:
                return var.set("¡Es incorrecta la expresión!")
                

        except:
            messagebox.showinfo("ERROR","Uy eso no es valido, intenta nuevamente")


    def cerrar(self):
        messagebox.showinfo("¡Genial!", "Gracias por usar nuestros servicios")
        ventana.destroy()
        
#Creamos la ventana 
#expresion que operamos en la ventana
patron=re.compile('^([A-Z]{1}[0-9]{3}[a-z]+[\W]{3})$')

validarexp=Validar()
ventana=tk.Tk()
ventana.title("validador de expresiones Regulares")
ventana.geometry('700x600')
ventana.iconbitmap("img\icono.ico") #esta es la ruta del icono
ventana.configure(background='gray25')


image=tk.PhotoImage(file="img\RegEx.png") #esta es la linea de la ruta de la imagen
image=image.subsample(4,4)
label=tk.Label(image=image)
#label.place(x=0,y=0,relwidth=1.0,relheight=1.0)
label.pack(pady=20)

#variable que muestra el mensaje
var=tk.StringVar()

#entrada
e1=tk.Label(ventana,text= "Por favor ingresa la expresión a validar :", font=('Comic Sans MS',18),bg='dodger blue',fg='white')
e1.pack(padx=50,pady=10, ipadx=10, ipady=10, fill=tk.X) #distribucion a lo ancho de las X
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=140,pady=10, ipadx=10, ipady=10)

#operación
operacion=tk.Button(ventana,text='Operar',fg='white',background='lime green',command=validarexp.operar)
operacion.pack(fill=tk.X,padx=200,pady=10, ipadx=5, ipady=10)

#Cajón de resultado
resultado=tk.Label(ventana,bg='plum',textvariable=var, background='snow2',font=('Comic Sans MS',18), padx=5,pady=5,width=50)
resultado.pack(fill=tk.X,padx=120,pady=5, ipadx=5, ipady=10)

#boton de cerrar
botoncerrar=tk.Button(ventana,text='Cerrar',fg='white',background='red',command=validarexp.cerrar)
botoncerrar.pack(fill=tk.X,padx=300,pady=10, ipadx=5, ipady=10)

ventana.mainloop()

