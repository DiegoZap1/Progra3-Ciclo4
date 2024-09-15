'''
Problema:
Un restaurante de nombre China Fast Food busca desarrollar un programa para la de compra de sus productos en linea de parte
de los usuarios, por lo tanto se deben de cumplir los siguientes criterios:

Productos a mostrar:
- Arroz Cantones Mixto
- Pollo con verduras
- Chao Mein
- Cerdo Asado

Metodos de pago:
- Tarjeta de credido o debito
- Efectivo

Funcionamiento: El programa debe mostrar una lista de productos y el cliente debera seleccionar el
producto deseado y este se mostrara junto con su precio y si este no es seleccionado debe pedirsele al 
usuario seleccionar uno, de igual forma con el metodo de pago.
'''

from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QMainWindow,QFormLayout,QComboBox,
                             QRadioButton,QPushButton)
from PyQt5.QtCore import Qt
import sys

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("Restaurante")

        inicio = QLabel("China Fast Food Restaurant\n")
        inicio.setAlignment(Qt.AlignCenter)
        elegir = QLabel("Eliga un producto: ")
        elegir.setAlignment(Qt.AlignCenter)

        # Productos
        self.productos = QComboBox()
        self.productos.addItems(["Seleccionar","Arroz Cantones Mixto","Pollo con verduras",
                                "Chao Mein","Cerdo Asado"])
        self.productos.currentIndexChanged.connect(self.declarar_factura)
        self.precios = {
            "Arroz Cantones Mixto" : 6.99,
            "Pollo con verduras" : 4.99,
            "Chao Mein" : 4.99,
            "Cerdo Asado" : 5.99
        }
        
        # Factura
        self.factura = QLabel()
        self.factura.setAlignment(Qt.AlignCenter)

        # Metodo de pago
        metodo = QLabel("Metodo de pago")
        self.tarjeta = QRadioButton("Tarjeta de credito o debito")
        self.efectivo = QRadioButton("Efectivo")
        pagar = QPushButton("Pagar")
        pagar.clicked.connect(self.pago)
        self.pagado = QLabel()
        self.pagado.setAlignment(Qt.AlignCenter)

        # Mostrar en pantalla
        layout = QFormLayout()
        layout.addRow(inicio)
        layout.addRow(elegir)
        layout.addRow(self.productos)
        layout.addRow(self.factura)
        layout.addRow(metodo)
        layout.addRow(self.tarjeta)
        layout.addRow(self.efectivo)
        layout.addRow(pagar)
        layout.addRow(self.pagado)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def declarar_factura(self,i):
        producto_seleccionado = self.productos.currentText()
        
        if producto_seleccionado != "Seleccionar":
            precio = self.precios.get(producto_seleccionado)
            self.factura.setText(f"{producto_seleccionado}: ${precio}")
        else:
            self.factura.setText("")
    
    def pago(self):
        tarjeta = self.tarjeta
        efectivo = self.efectivo

        if (self.productos.currentText() == "Seleccionar"):
            self.pagado.setText("Primero seleccione un producto")
        elif not (tarjeta.isChecked() or efectivo.isChecked()):
            self.pagado.setText("Seleccione un metodo de pago")
        else:
            if tarjeta.isChecked():
                self.pagado.setText("!Compra realizada con tarjeta!")
            else:
                self.pagado.setText("!Compra realizada con efectivo!")

app = QApplication(sys.argv)
ventana = mainwindow()
ventana.show()
app.exec()