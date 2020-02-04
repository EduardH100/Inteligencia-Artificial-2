import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

class Ventana():
    def __init__(self, master):
        
        self.master = master
        self.frame = tk.Frame(master)
        self.fig = Figure(figsize=(500, 800))

        self.ax1 = self.fig.add_subplot(1,1,1)
        self.ax1.set_title("Perceptron")


        self.canvas = FigureCanvasTkAgg(self.fig, self.master)
        self.canvas.get_tk_widget().grid(row=0, column=0)
        self.canvas.show()
        
        toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        toolbar.update()

        self.canvas.mpl_connect("button_press_event", self.on_button_press)


        self.fig.plot(0.5, 0.3, color="#C41E3A", marker="o")
      

        self.canvas.draw()

        self.btn_quit = tkinter.Button(self, text="Quit", command=self._quit)
        self.btn_quit.place(x=500, y=500)


        def on_button_press(self):
            print("")

        
        def _quit():
            self.master.quit()     # stops mainloop
            self.master.destroy()  
            
root = tk.Tk()
app = Ventana(root)
root.mainloop()