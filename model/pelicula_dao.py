from .conexion_db import Conexion_DB

def crear_tabla():
    conexion=Conexion_DB()
    sql='''
    CREATE TABLE peliculas_tb(
        id_pelicula INTEGER, 
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(50)
    )
    '''