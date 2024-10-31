import sys
from PyQt6.QtWidgets import QApplication, QWidget

class VentanaVacia(QWidget):

    #defino el constructor del objeto
    def __init__(self):
        super().__init__()
        self.incializarUI()
    
    def incializarUI(self):
        self.setGeometry(100,100,250,250) #recibe parametros que son el tamaño de la ventana son 4, posición en X e Y. Luego ancho y largo en pixeles.
        self.setWindowTitle("Mi Primera Ventana")
        self.show() #con este método visualizamos la ventana
        

if __name__ == '__main__':
    #generamos una instancia de QApplication
    app = QApplication(sys.argv)  #sys.argv se usa para enviar  por consola parámetros.
    ventana = VentanaVacia()
    #ejecuto la app
    sys.exit(app.exec()) #el exit nos permite cortar todos los recursos de la app.





        
