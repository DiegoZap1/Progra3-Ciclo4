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
        nombre1 = QLabel(f"Nombre: Diego Alexander Zapata López")
        edad1 = QLabel(f"Edad: {19} años")
        nombre2 = QLabel("Jose Luis Escobar Caceres")
        edad2 = QLabel(f"Edad: {19} años")
        nombre1.setAlignment(Qt.AlignCenter)
        edad1.setAlignment(Qt.AlignCenter)
        nombre2.setAlignment(Qt.AlignCenter)
        edad2.setAlignment(Qt.AlignCenter)

        # Mostrar en pantalla
        layout = QFormLayout()
        layout.addRow(nombre1)
        layout.addRow(edad1)
        layout.addRow(nombre2)
        layout.addRow(edad2)
        layout.setFormAlignment(Qt.AlignCenter)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()