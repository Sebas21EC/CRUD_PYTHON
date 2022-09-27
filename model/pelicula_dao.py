from .conexion_db import Conexion_DB
from tkinter import messagebox

def crear_tabla():
    conexion=Conexion_DB()

    sql='''
    CREATE TABLE peliculas_tb(
        id_pelicula INTEGER, 
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(50),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )'''
    titulo = 'Crear Registro'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_db()
        mensaje = 'Se creó la tabla en la base de datos'

    except:
        mensaje = 'La tabla ya se encuentra creada'

    messagebox.showinfo(titulo,mensaje)
    

def eliminar_tabla():
    conexion=Conexion_DB()
    sql = ' DROP TABLE peliculas_tb'
    conexion.cursor.execute(sql)
    conexion.cerrar_db()
    titulo = 'Borrar Registro'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_db()
        mensaje = 'Se eliminó la tabla en la base de datos'

    except:
        mensaje = 'No existe esta tabla para eliminar'
    
    messagebox.showerror(titulo,mensaje)