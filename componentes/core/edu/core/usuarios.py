from edu.cableado.api import IRegla

import tkinter as tk

class Usuarios(IRegla):
    def verificar_reglas(self):
        master = tk.Tk()
        tk.Message(master, text="Creando usuario").pack()
        tk.Message(master, text="Eliminar usuario").pack()
        tk.Message(master, text="Modificar Usuario").pack()
        tk.Message(master, text="Ingresando con el usuario").pack()        
        tk.mainloop()   