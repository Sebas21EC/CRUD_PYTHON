import tkinter as tk
##Funcion para crear el menu
def barra_menu (root):
    barra_menu=tk.Menu(root)
    root.config(menu=barra_menu,width=300,height=300)

    menu_inicio=tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio',menu=menu_inicio)
    
    menu_inicio.add_command(label='Crear Registro')
    menu_inicio.add_command(label='Eliminar Registro')
    menu_inicio.add_command(label='Exit',command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Help')

class Frame(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=720, height=520)
        self.root = root
        self.pack()
        self.config( bg='gray')

