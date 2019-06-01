#curso:logica-en-sistemas

#semestre:primero

#nombre:Patricia.Anahi-Juarez-Peña

#carnet:0907-19-6959

#repositoriohttps://github.com/anahij9/examen-final-logica-en-sistemas-B.git

from tkinter import ttk
from tkinter import *

class Desk:
    def __init__(self, window):
        # Initializations
        
        #ancho
        ancho = 3100
        
        #alto
        alto = 2600
        
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('Aplicación con interface gráfica en Python - By Ing. Gerson Altamirano')
        
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'resta 2 valores')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        # creamos un etiqueta
        Label(frame, text = 'primer numero: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'segundo numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)

        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'tecer numero: ').grid(row = 3, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 3, column = 1)
        
         #Creamos un boton para ejecutar la multiplicacion, suma o resta
        Button(frame, text = 'multiplicacion', command = self.multiplicacion).grid(row = 4, columnspan = 2, sticky = W + E)
        Button(frame, text = 'suma var1=var2', command = self.suma).grid(row = 5, columnspan = 2, sticky = W + E)
        Button(frame, text = 'resta var2=0-var1-var3' , command = self.resta).grid(row = 5, columnspan = 2, sticky = W + E)
       
        #Creamos un boton para ejecutar la unir o respetir
        Button(frame, text = 'unir ', command = self.unir).grid(row = 5, columnspan = 2, sticky = W + E)
        Button(frame, text = 'repetir', command = self.unir).grid(row = 5, columnspan = 2, sticky = W + E)

        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get())  != 0 and len(self.var3.get()) != 0

    # esta es la función que ejecuta el primer boton 
    #si var1 es menor que var3 se multiplicaran los tres 
    def multiplicacion(self):
        if self.validation():
            resultado = float( self.var1.get() < float( self.var3.get() ) * float( self.var2.get())
            self.message['text'] ='el primer valor es menor que el tercero igual multiplicacion de los 3: {}'.format(resultado)
   #esta funcion si var1 var3 es igualse suman los tres
   def suma(self):
        if self.validation():
            resultado = float( self.var1.get() + float( self.var3.get() ) + float( self.var1.+var2.+var3. get())
            self.message['text'] = 'el primer valor1y valor3: {}'.format(resultado)
    # esta funcion si el var2 es 0 se resta del mayor a menor de los imput
    def resta(self):
        if self.validation():
            resultado = float( self.var2.get()=0  float( self.var1.get() ) + float( self.var1.-var2.-var3. get())
            self.message['text'] = 'el primer valor1y valor3: {}'.format(resultado)
        else:
            self.message['
            text'] = 'los campos son requeridos'

     # esta es la función que ejecuta la suma
    def suma(self):
        if self.validation():
            resultado = float( self.var1.get() ) + float( self.var2.get() )
            self.message['text'] = 'La suma de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'

#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()