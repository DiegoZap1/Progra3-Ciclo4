from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QMainWindow,QFormLayout,QLineEdit,
                             QPushButton)
from PyQt5.QtCore import Qt
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 3")
        self.setGeometry(200,200,400,300)

        # Inicio de sesion
        inicio = QLabel("Inicio de sesion")
        inicio.setAlignment(Qt.AlignCenter)
        self.sesion_iniciada = QLabel()
        self.sesion_iniciada.setAlignment(Qt.AlignCenter)

        # Nombre
        nombre = QLabel("Nombre: ")
        self.nombre_edit = QLineEdit()

        # Cedula
        cedula = QLabel("Cedula: ")
        self.cedula_edit = QLineEdit()

        # Boton
        boton = QPushButton("Inicio de sesion")
        boton.clicked.connect(self.cambiar_label)

        # Mostrar en pantalla
        layout = QFormLayout()
        layout.addRow(inicio)
        layout.addRow(nombre,self.nombre_edit)
        layout.addRow(cedula,self.cedula_edit)
        layout.addRow(boton)
        layout.addRow(self.sesion_iniciada)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def cambiar_label(self):
        nombre = self.nombre_edit.text()
        cedula = self.cedula_edit.text()

        if not nombre or not cedula:
            self.sesion_iniciada.setText("Ingrese datos validos")
        else:
            self.sesion_iniciada.setText(f"!Inicio de Sesion Exitoso! \n\nBienvenido\n{nombre}\n{cedula}")

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()