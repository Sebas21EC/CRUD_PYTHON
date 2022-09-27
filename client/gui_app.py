from cgitb import enable
from math import fabs
from pydoc import cram
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.pelicula_dao import crear_tabla,eliminar_tabla
from model.pelicula_dao import Pelicula,guardar,listar_peliculas,editar

##Funcion para crear el menu
def barra_menu (root):
    barra_menu=tk.Menu(root)
    root.config(menu=barra_menu,width=300,height=300)

    menu_inicio=tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio',menu=menu_inicio)
    
    menu_inicio.add_command(label='Crear Registro',command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro',command=eliminar_tabla)
    menu_inicio.add_command(label='Exit',command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Help')

class Frame(tk.Frame):

    ## Constructor
    def __init__(self,root=None):
        super().__init__(root,width=720, height=520)
        self.root = root
        self.pack()
        self.id_pelicula=None

        #self.config( bg='gray')
        self.campos_peliculas()
        self.deshabilitar_campos()
        self.tabla_datos()
    
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
        self.nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)

        self.duracion=tk.StringVar()
        self.entry_duracion=tk.Entry(self,textvariable=self.duracion)
        self.entry_duracion.config(width=50,font=('Arial',12))
        self.entry_duracion.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.genero=tk.StringVar()
        self.entry_genero=tk.Entry(self,textvariable=self.genero)
        self.entry_genero.config(width=50,font=('Arial',12))
        self.entry_genero.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        #botones
        self.btn_nuevo=tk.Button(self,text="Nuevo",command=self.habilitar_campos)
        self.btn_nuevo.config(width=20,font=('Arial',12,'bold'),fg='white',background='#04B404', curso='hand2',activebackground='#35BD6F')
        self.btn_nuevo.grid(row=3,column=0)

        self.btn_guardar=tk.Button(self,text="Guardar",command=self.guardar_datos)
        self.btn_guardar.config(width=20,font=('Arial',12,'bold'),fg='white',background='blue', curso='hand2',activebackground='cyan')
        self.btn_guardar.grid(row=3,column=1)

        self.btn_cancelar=tk.Button(self,text="Cancelar",command=self.deshabilitar_campos)
        self.btn_cancelar.config(width=20,font=('Arial',12,'bold'),fg='white',background='orange', curso='hand2',activebackground='brown')
        self.btn_cancelar.grid(row=3,column=2)

        # Metodo para habilitar los campos
    def habilitar_campos(self):
        self.nombre.set('')
        self.duracion.set('')
        self.genero.set('')

        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.nombre.set('')
        self.duracion.set('')
        self.genero.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')

    def guardar_datos(self):

        pelicula=Pelicula(
            self.nombre.get(),
            self.duracion.get(),
            self.genero.get(),
        )
        if self.id_pelicula==None:
            guardar(pelicula)
        else:
            editar(pelicula,self.id_pelicula)

        self.tabla_datos()
        self.deshabilitar_campos()
        self.id_pelicula=None

    #Diseñar la tabla de datos
    def tabla_datos(self):
        self.lista_peliculas=listar_peliculas()
        self.lista_peliculas.reverse()

        self.table=ttk.Treeview(self,columns=('Nombre','Duración','Género'))
        self.table.grid(row=4,column=0,columnspan=4,sticky='nse')
       
        #ScrollBar para la tabla
        self.scroll=ttk.Scrollbar(self,orient='vertical',command=self.table.yview)
        self.scroll.grid(row=4, column=4,sticky='nse')
        self.table.configure(yscrollcommand=self.scroll.set)

        self.table.heading('#0',text='ID')
        self.table.heading('#1',text='NOMBRE')
        self.table.heading('#2',text='DURACIÓN')
        self.table.heading('#3',text='GÉNERO')

        #INSERTAR DAOTS EN LA TABLA
        for p in self.lista_peliculas:
            self.table.insert('',0,text=p[0],values=(p[1],p[2],p[3]))
        
        self.btn_editar=tk.Button(self,text="Editar",command=self.editar_datos)
        self.btn_editar.config(width=20,font=('Arial',12,'bold'),fg='white',background='#04B404', curso='hand2',activebackground='#35BD6F')
        self.btn_editar.grid(row=5,column=0)

        self.btn_eliminar=tk.Button(self,text="Eliminar")
        self.btn_eliminar.config(width=20,font=('Arial',12,'bold'),fg='white',background='orange', curso='hand2',activebackground='brown')
        self.btn_eliminar.grid(row=5,column=1)
    
    def editar_datos(self):
        try:
            self.id_pelicula=self.table.item(self.table.selection())['text']
            self.nombre_pelicula=self.table.item(self.table.selection())['values'][0]
            self.duracion_pelicula=self.table.item(self.table.selection())['values'][1]
            self.genero_pelicula=self.table.item(self.table.selection())['values'][2]

            self.habilitar_campos()

            self.entry_nombre.insert(0,self.nombre_pelicula)
            self.entry_duracion.insert(0,self.duracion_pelicula)
            self.entry_genero.insert(0,self.genero_pelicula)

        
        except:
            
            messagebox.showinfo('Edición de datos','No ha seleccionado ningun registro')
    