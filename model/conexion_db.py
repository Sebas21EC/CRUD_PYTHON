import sqlite3

class Conexion_DB:
    def __init__(self):
        self.base_datos='C:/Users/User/Documents/Python/CatalogoPeliculas_Escritorio/Proyecto_CatalogoPeliculas/database/peliculas.db'
        self.conexion=sqlite3.connect(self.base_datos)
        self.cursor=self.conexion.cursor()

    def cerrar_db(self):
        self.conexion.commit()
        self.conexion.close()

    