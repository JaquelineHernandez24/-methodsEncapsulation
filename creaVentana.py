import tkinter as tk
def crear_ventana(n, m):

    # Crear la ventana principal

    ventana = tk.Tk()

    ventana.title("Ventana Fija")


    # Establecer el tamaño de la ventana (n x m píxeles)

    ventana.geometry(f"{n}x{m}")


    # Evitar que la ventana sea redimensionable

    ventana.resizable(False, False)


    # Iniciar el bucle principal de la ventana

    ventana.mainloop()