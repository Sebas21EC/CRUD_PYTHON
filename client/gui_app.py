from cgitb import enable
from math import fabs
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

    ## Constructor
    def __init__(self,root=None):
        super().__init__(root,width=720, height=520)
        self.root = root
        self.pack()
        #self.config( bg='gray')
        self.campos_peliculas()
        self.deshabilitar_campos()
    
    ##Crear los elementos del frame.
    def campos_peliculas(self):
        #Labels de los campos
        self.label_nombre=tk.Label(self, text="Nombre:")
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_duracion=tk.Label(self, text="Duración:")
        self.label_duracion.config(font=('Arial',12,'bold'))
        self.label_duracion.grid(row=1,column=0,padx=10,pady=10)

        self.label_genero=tk.Label(self, text="Género:")
        self.label_genero.config(font=('Arial',12,'bold'))
        self.label_genero.grid(row=2,column=0,padx=10,pady=10)

        #campos de entrada
        self.entry_nombre=tk.Entry(self)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.entry_duracion=tk.Entry(self)
        self.entry_duracion.config(width=50,font=('Arial',12))
        self.entry_duracion.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.entry_genero=tk.Entry(self)
        self.entry_genero.config(width=50,font=('Arial',12))
        self.entry_genero.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        #botones
        self.btn_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
        self.btn_nuevo.config(width=20,font=('Arial',12,'bold'),fg='white',background='#04B404', curso='hand2',activebackground='#35BD6F')
        self.btn_nuevo.grid(row=4,column=0)

        self.btn_guardar=tk.Button(self,text="Guardar")
        self.btn_guardar.config(width=20,font=('Arial',12,'bold'),fg='white',background='blue', curso='hand2',activebackground='cyan')
        self.btn_guardar.grid(row=4,column=1)

        self.btn_cancelar=tk.Button(self,text="Cancelar",command=self.deshabilitar_campos)
        self.btn_cancelar.config(width=20,font=('Arial',12,'bold'),fg='white',background='orange', curso='hand2',activebackground='brown')
        self.btn_cancelar.grid(row=4,column=2)

        # Metodo para habilitar los campos
    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')

        
