import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Catálogo de Películas')
    root.iconbitmap('C:/Users/User/Documents/Python/CatalogoPeliculas_Escritorio/Proyecto_CatalogoPeliculas/img/icono.ico')
               ## (Lados/ArribaAbajo)
    root.resizable(0,0)


    ##Crear Frame y empaquetar a la raiz
    ##frame=tk.Frame(root)
   ## frame.pack()
   ## frame.config(width=720, height=520, bg='gray')

    ##Importar Frame  y barra de menu

    barra_menu(root)
    app=Frame(root=root)
    
    app.mainloop()


if __name__ == '__main__':
    main()