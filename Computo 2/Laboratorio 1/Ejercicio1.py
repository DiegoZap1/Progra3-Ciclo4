from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QMainWindow,QFormLayout)
from PyQt5.QtCore import Qt
import sys


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 1")
        self.setGeometry(200,200,400,300)

        # Datos personales
        nombre = QLabel(f"Nombre: Diego Alexander Zapata López")
        edad = QLabel(f"Edad: {19} años")
        nombre.setAlignment(Qt.AlignCenter)
        edad.setAlignment(Qt.AlignCenter)

        # Mostrar en pantalla
        layout = QFormLayout()
        layout.addRow(nombre)
        layout.addRow(edad)
        layout.setFormAlignment(Qt.AlignCenter)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()