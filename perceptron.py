
import numpy as np
import time

class perceptron():
    def __init__(self, master):
        self.master = master #quiza no vaya asi
        self.pesos = master.pesos
        self.rango_a = master.rango_a
        self.datos = master.datos #entradas
        self.salidas = master.clases
        self.epocas_max = master.epocas_max

    def proceso(self):
        bandera = 0
        epoca = 0
        errores_ac = []
        while bandera == 0 and epoca < int(self.epocas_max):
            bandera = 1
            error_acumulado = 0
            for i in range(len(self.datos)): #epoca

                net = np.dot(self.pesos, self.datos[i])

                #funcion escalon (transicion) Pw(x)
                if net >= 0:
                    y = 1
                else:
                    y = 0

                error = self.salidas[i] - y
                #print("Error: " + str(error))

                if error != 0:
                    self.adapta_pesos(self.datos[i], error)
                    error_acumulado = error_acumulado + 1
                    bandera = 0

            epoca = epoca + 1
            errores_ac.append(error_acumulado)
            self.dibuja_error(errores_ac)
            self.dibuja_recta()

        #self.dibuja_error(errores_ac)
        if bandera == 1:
            print("Convergió")
            self.dibuja_recta("#00FF00")
            return True
        else:
            print("No Convergió")
            self.master.ax1.clear()
            self.master.ax2.clear()
            return False

    def dibuja_recta(self, colorL="#EEEEEE"):
        xs = []
        ys = []
        for i in range(len(self.datos)):
            #variedad_lineal = (self.datos[i][0]*self.pesos[0] + self.datos[i][1]*self.pesos[1]) / self.pesos[2]
            variedad_lineal = ( - (self.pesos[1]/self.pesos[2]) * self.datos[i][1] ) - (self.pesos[0]/self.pesos[2])
            
            xs.append(self.datos[i][1])
            ys.append(variedad_lineal)
        #self.master.ax1.plot([-10,10],[(self.pesos[0]/self.pesos[2]),((self.pesos[0]/self.pesos[2]) - (self.pesos[1]/self.pesos[2]))], color=colorL)
        self.master.ax1.plot(xs, ys, color=colorL)
        self.master.canvas1.draw()

    def adapta_pesos(self, x, error):
        #print(self.pesos)
        for i in range(len(self.pesos)):
            self.pesos[i] = self.pesos[i] + ( float(self.rango_a) * error * x[i] )
        #print(self.pesos)

    def dibuja_error(self, errores):
        #self.master.ax2.clear()
        indices = []
        for i in range(len(errores)):
            indices.append(i)
        
        self.master.ax2.plot(indices, errores, color="#0000FF")
        self.master.canvas2.draw()

    def probar(self, datos):
        net = np.dot(datos, self.pesos)

        if net >= 0:
            y = 1
        else:
            y = 0

        return y

