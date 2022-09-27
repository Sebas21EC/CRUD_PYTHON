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

    titulo = 'Borrar Registro'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_db()
        mensaje = 'Se eliminó la tabla de la base de datos'
    except:
        mensaje = 'No existe esta tabla para eliminar'
    
    messagebox.showerror(titulo,mensaje)


class Pelicula:
    def __init__(self,nombre,duracion,genero):
        self.id_pelicula=None
        self.nombre=nombre
        self.duracion=duracion
        self.genero=genero

    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion},{self.genero}]'

def guardar(pelicula):
    conexion=Conexion_DB()
    sql=f"""INSERT INTO peliculas_tb ('nombre','duracion','genero') 
    VALUES('{pelicula.nombre}','{pelicula.duracion}','{pelicula.genero}')"""
    
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_db()
    except:
        titulo ="Conexion al registro"
        mensaje ="La tabla peliculas no esta creada en la base de datos"
        messagebox.showwarning(titulo,mensaje)

def listar_peliculas():
    conexion=Conexion_DB()

    lista_peliculas=[]
    sql='SELECT * FROM peliculas_tb'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas=conexion.cursor.fetchall()
        conexion.cerrar_db()
    except:
        messagebox.showwarning('Mostrar registros','No existe la tabla pelculas')
    
    return lista_peliculas

def editar(pelicula,id_pelicula):
    conexion=Conexion_DB()
    sql=f"""
    UPDATE peliculas_tb 
    SET nombre='{pelicula.nombre}',duracion='{pelicula.duracion}',genero='{pelicula.genero}' 
    WHERE id_pelicula={id_pelicula} 
    """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_db()
    except:
        messagebox.showwarning('Edicion de dato','No se pudo editar la película')
    
def eliminar(id_pelicula):
    conexion=Conexion_DB()
    sql=f'DELETE FROM peliculas_tb WHERE id_pelicula={id_pelicula}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_db()
    except:
        messagebox.showwarning('Elinar Datos','No se pudo eliminar el registro')