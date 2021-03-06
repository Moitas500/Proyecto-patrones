from edu.cableado.api import IRegla

import tkinter as tk

class Nucleo(IRegla):
    def verificar_reglas(self):          
        p = Producto()
        p.verificar_reglas() 
        
        v = Ventas()
        v.verificar_reglas()
        
        u = Usuarios()
        u.verificar_reglas()
        
class Usuarios(IRegla):
    def verificar_reglas(self):
        master = tk.Tk()
        tk.Message(master, text="Creando usuario").pack()
        tk.Message(master, text="Eliminar usuario").pack()
        tk.Message(master, text="Modificar Usuario").pack()
        tk.Message(master, text="Ingresando con el usuario").pack()        
        tk.mainloop()   

class Producto(IRegla):
    def verificar_reglas(self):
        master = tk.Tk()
        tk.Message(master, text="Creando producto").pack()
        tk.Message(master, text="Eliminar producto").pack()
        tk.Message(master, text="Leyendo producto").pack()
        tk.Message(master, text="Actualizando producto").pack()
        tk.mainloop()                
        
class Ventas(IRegla):
    def verificar_reglas(self):        
        master = tk.Tk()       
        tk.Message(master, text="Crear venta").pack()
        tk.Message(master, text="Obtener ventas").pack()
        tk.mainloop() 
