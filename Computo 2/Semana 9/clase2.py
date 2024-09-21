from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QMainWindow,QFormLayout,QLineEdit,
                             QPushButton,QTextEdit,QMessageBox)
from PyQt5.QtCore import Qt
import sys
import smtplib

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,200)
        self.setWindowTitle("Envio Email")
        
        inicio = QLabel("Envio de Email")
        inicio.setAlignment(Qt.AlignCenter)

        # Datos Email
        para = QLabel("Para: ")
        self.para_edit = QLineEdit()
        asunto = QLabel("Asunto: ")
        self.asunto_edit = QLineEdit()
        mensaje = QLabel("Mensaje")
        mensaje.setAlignment(Qt.AlignCenter)
        self.mensaje_edit = QTextEdit()
        boton = QPushButton("Enviar Email")
        boton.clicked.connect(self.envioEmail)

        #Mostrar en pantalla
        layout = QFormLayout()
        layout.addRow(inicio)
        layout.addRow(para,self.para_edit)
        layout.addRow(asunto, self.asunto_edit)
        layout.addRow(mensaje)
        layout.addRow(self.mensaje_edit)
        layout.addRow(boton)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def envioEmail(self):
        para = self.para_edit.text()
        asunto = self.asunto_edit.text()
        mensaje = self.mensaje_edit.toPlainText()

        if (not para or not asunto or not mensaje):
            QMessageBox.information(self,"Envio","Rellene todas las casillas")
        else:
            QMessageBox.information(self,"Envio","Correo enviado con exito")

        # DatosSS
        server = "smtp.gmail.com"
        puerto = 587
        correo = "deede782@gmail.com"
        remit = para
        contraseña = "rzlf iblw jvkw lhrv"

        # Envio del correo
        conex = smtplib.SMTP(server,puerto)
        #print(conex.ehlo())
        conex.starttls()
        conex.login(correo,contraseña)
        conex.sendmail(correo,remit,f"Subjetc: {asunto} \n\n {mensaje}")
        conex.quit()

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()