from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QMainWindow,QFormLayout,QLineEdit,
                             QPushButton)
from PyQt5.QtCore import Qt
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 2")
        self.setGeometry(200,200,400,300)
        
        sesion = QLabel("Inicio de sesion")
        sesion.setAlignment(Qt.AlignCenter)
        self.sesion_iniciada = QLabel()
        self.sesion_iniciada.setAlignment(Qt.AlignCenter)

        # Nombre
        nombre = QLabel(f"Nombre: ")
        nombre_edit = QLineEdit()

        # Contraseña
        contraseña = QLabel(f"Contraseña: ")
        pwd = QLineEdit()
        pwd.setEchoMode(QLineEdit.Password)

        # Boton de sesion
        boton = QPushButton("Iniciar Sesion")
        boton.clicked.connect(self.cambiar_label)

        # Mostrar en pantalla
        layout = QFormLayout()
        layout.addRow(sesion)
        layout.addRow(nombre,nombre_edit)
        layout.addRow(contraseña,pwd)
        layout.addRow(boton)
        layout.addRow(self.sesion_iniciada)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def cambiar_label(self):
        self.sesion_iniciada.setText("!Sesion Iniciada con Exito!")

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()