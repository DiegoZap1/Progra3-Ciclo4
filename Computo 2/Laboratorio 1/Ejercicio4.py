from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QMainWindow,QFormLayout,QLineEdit,
                             QPushButton)
from PyQt5.QtCore import Qt
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 4")
        self.setGeometry(200,200,400,300)

        inicio = QLabel("Datos de animales")
        inicio.setAlignment(Qt.AlignCenter)
        self.mostrar = QLabel()
        self.mostrar.setAlignment(Qt.AlignCenter)

        # Datos del animal
        nombre = QLabel("Nombre: ")
        self.nombre_edit = QLineEdit()
        raza = QLabel("Raza: ")
        self.raza_edit = QLineEdit()
        especie = QLabel("Especie: ")
        self.especie_edit = QLineEdit()

        # Boton
        boton = QPushButton("Registrar")
        boton.clicked.connect(self.cambiar_label)

        # Mostrar en pantalla 
        layout = QFormLayout()
        layout.addRow(inicio)
        layout.addRow(nombre,self.nombre_edit)
        layout.addRow(raza,self.raza_edit)
        layout.addRow(especie,self.especie_edit)
        layout.addRow(boton)
        layout.addRow(self.mostrar)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)
    
    def cambiar_label(self):
        nombre = self.nombre_edit.text()
        raza = self.raza_edit.text()
        especie = self.especie_edit.text()

        if not nombre or not raza or not especie:
            self.mostrar.setText("Ingrese datos validos")
        else:
            self.mostrar.setText(f"!Mascota registrada con exito! \n\nDatos de la mascota:\nNombre: {nombre}\nRaza: {raza}\nEspecie: {especie}")

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()