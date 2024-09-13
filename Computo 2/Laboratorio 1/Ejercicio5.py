from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QMainWindow,QFormLayout,QLineEdit,
                             QPushButton)
from PyQt5.QtCore import Qt
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 5")

        inicio = QLabel("Registro de Personas")
        inicio.setAlignment(Qt.AlignCenter)
        self.registro = QLabel()
        self.registro.setAlignment(Qt.AlignCenter)

        # Persona
        nombre = QLabel("Nombre: ")
        self.nombre_edit = QLineEdit()
        apellido = QLabel("Apellidos: ")
        self.apellido_edit = QLineEdit()
        edad = QLabel("Edad: ")
        self.edad_edit = QLineEdit()
        telefono = QLabel("Telefono: ")
        self.telefono_edit = QLineEdit()
        dui = QLabel("Dui: ")
        self.dui_edit = QLineEdit()
        email = QLabel("Email: ")
        self.email_edit = QLineEdit()
        pais = QLabel("Pais: ")
        self.pais_edit = QLineEdit()
        nacionalidad = QLabel("Nacionalidad: ")
        self.nacionalidad_edit = QLineEdit()
        ocupacion = QLabel("Ocupacion: ")
        self.ocupacion_edit = QLineEdit()
        fecha_nacimiento = QLabel("Fecha de nacimiento: ")
        self.fecha_nacimiento_edit = QLineEdit()

        # Boton
        boton = QPushButton("Registrar Persona")
        boton.clicked.connect(self.cambiar_label)
    

        # Mostrar en pantalla
        layout = QFormLayout()
        layout.addRow(inicio)
        layout.addRow(nombre,self.nombre_edit)
        layout.addRow(apellido,self.apellido_edit)
        layout.addRow(edad,self.edad_edit)
        layout.addRow(telefono,self.telefono_edit)
        layout.addRow(dui,self.dui_edit)
        layout.addRow(email,self.email_edit)
        layout.addRow(pais,self.pais_edit)
        layout.addRow(nacionalidad,self.nacionalidad_edit)
        layout.addRow(ocupacion,self.ocupacion_edit)
        layout.addRow(fecha_nacimiento,self.fecha_nacimiento_edit)
        layout.addRow(boton)
        layout.addRow(self.registro)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)
    
    def cambiar_label(self):
        nombre = self.nombre_edit.text()
        apellido = self.apellido_edit.text()
        edad = self.edad_edit.text()
        telefono = self.telefono_edit.text()
        dui = self.dui_edit.text()
        email = self.email_edit.text()
        pais = self.pais_edit.text()
        nacionalidad = self.nacionalidad_edit.text()
        ocupacion = self.ocupacion_edit.text()
        fecha_nacimiento = self.fecha_nacimiento_edit.text()

        
        if (not nombre or not apellido or not edad or not telefono or not dui
            or not email or not pais or not nacionalidad or not ocupacion or not fecha_nacimiento):
            self.registro.setText("Ingrese todos los datos")
        else:
            self.registro.setText(f"""!Persona registrada con exito\n\nNombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nTelefono: {telefono}\nDui: {dui}\nEmail: {email}\nPais: {pais}\nNacionalidad: {nacionalidad}\nOcupacion: {ocupacion}\nFecha de nacimiento: {fecha_nacimiento}""")

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()