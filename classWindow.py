import tkinter as tk
class Window:
    __ancho = 500
    __alto = 500
    __titulo = "Mi primera App"
    __resize = False  # Debe ser un atributo privado, lo he agregado aquí.

    def setDimensions(self, width, height):
        self.__ancho = width
        self.__alto = height

    def getDimensions(self):
        return [self._ancho, self._alto]

    def setResize(self, resize):
        self.__resize = resize

    def getResize(self):
        return self.__resize

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getTitulo(self):
        return self.__titulo

    def crear_ventana(self):
        # Crear la ventana principal
        ventana = tk.Tk()
        ventana.title(self.__titulo)
        # Establecer el tamaño de la ventana (n x m píxeles)
        ventana.geometry(f"{self._ancho}x{self._alto}")
        # Evitar que la ventana sea redimensionable
        ventana.resizable(self._resize,self._resize)
        # Iniciar el bucle principal de la ventana
        ventana.mainloop()