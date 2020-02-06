from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

import tkinter as tk
import numpy as np
from perceptron import *

color1 = "#336eff"  #azul
color2 = "#FF0000"  #rojo

error_ac = []

class Ventana():
    def __init__(self, master):

        self.master = master
        self.rango_a = tk.IntVar()
        self.epocas_max = tk.IntVar()
        self.pesos = []
        self.datos = []
        self.clases = []
        self.convergio = False

        self.fig = Figure(figsize=(5, 3))
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.set_xlim(-10, 10)
        self.ax1.set_ylim(-10, 10)
        self.ax1.set_title("Datos")

        self.canvas1 = FigureCanvasTkAgg(self.fig, master=self.master)  
        self.canvas1.draw()
        self.canvas1.get_tk_widget().place(x=0, y=0)

        self.fig2 = Figure(figsize=(5, 2))
        self.ax2 = self.fig2.add_subplot(111)
        self.ax2.set_title("Error")

        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.master)  
        self.canvas2.draw()
        self.canvas2.get_tk_widget().place(x=0, y=350)

        toolbar = NavigationToolbar2Tk(self.canvas1, self.master)
        #self.toolbar.update()

        self.canvas1.mpl_connect("button_press_event", self.clic)

        tk.Label(self.master, text="Rango de aprendizaje").place(x=600, y=80)
        self.val_ra = tk.Entry(self.master, textvariable=self.rango_a)
        self.val_ra.place(x=600, y=100)
        self.val_ra.insert(1, 0.50)

        tk.Label(self.master, text="Épocas máximas").place(x=600, y=120)
        self.val_epocas_max = tk.Entry(self.master, textvariable=self.epocas_max)
        self.val_epocas_max.place(x=600, y=140)
        self.val_epocas_max.insert(1,200)

        tk.Button(self.master, text="Inicializar Pesos", command=self.iniciar_pesos).place(x=600, y=170)
        self.lb_pesos = tk.Label(self.master, text="Pesos: ")
        self.lb_pesos.place(x=600, y=200)

        tk.Button(self.master, text="Perceptron", command=self.perceptron).place(x=600, y=250)
        #tk.Button(self.master, text="Probar", command=self.probar_perceptron).place(x=600, y=280)
        
        tk.Button(self.master, text="Salir", command=self.salir).place(x=600, y=600)
        tk.Button(self.master, text="Borrar", command=self.borrar).place(x=600, y=630)

    def perceptron(self):
        self.rango_a = self.val_ra.get()
        self.epocas_max = self.val_epocas_max.get()
        self.ptron = perceptron(self)
        self.convergio = self.ptron.proceso()

    def probar_perceptron(self, datos):
        return self.ptron.probar(datos)

    def iniciar_pesos(self):
        self.pesos = np.random.uniform(low=0.0, high=1.0, size=3)
        self.lb_pesos.config(text=str(self.pesos[0])+" - "+str(self.pesos[1])+" - "+str(self.pesos[2]))

    def clic(self, event):
        #print('button=%d, xdata=%f, ydata=%f' %
        #  (event.button, event.xdata, event.ydata))

        if self.convergio == False:
            if(event.button == 1):
                color = color1
                clase = 1
                marca = "."
            else:
                color = color2  
                clase = 0
                marca = "+"

            self.datos.append([1, event.xdata, event.ydata])
            self.clases.append(clase)
        else:
            datos_prueba = [1, event.xdata, event.ydata]
            clase = self.probar_perceptron(datos_prueba)
            if(clase == 1):
                color = "#336eff"
                marca = "."
            else:
                color = "#FF0000"
                marca = "+"

        self.ax1.scatter(event.xdata, event.ydata, marker=marca, color=color, linewidth=2)
        self.canvas1.draw()


    def salir(self):
        self.master.quit()     # stops mainloop
        self.master.destroy()  
    
    def borrar(self):
        self.datos = []
        self.clases = []
        self.convergio = False

        self.ax1.cla()
        self.ax1.set_xlim(-10, 10)
        self.ax1.set_ylim(-10, 10)
        self.ax1.set_title("Datos")

        self.ax2.cla()
        self.ax2.set_title("Error")

        self.canvas1.draw()
        self.canvas2.draw()


root = tk.Tk()
root.title("Perceptron")
root.geometry("1200x700+0+0")
app = Ventana(root)

tk.mainloop()
