from PIL import Image
from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,QVBoxLayout)
from PyQt5.QtGui import QPixmap
import sys
import io

def convertir(imagen):
    arreglo = io.BytesIO()
    imagen.save(arreglo.getvalue())
    imagenv = QPixmap()
    imagenv.loadFromData(arreglo.getvalue())
    return imagenv

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Imagen de ventana de PyQt5")
img = Image.open("base.jpg")
mapa = convertir(img)
label = QLabel()
label.setPixmap(mapa)

layout = QVBoxLayout()
layout.addWidget(label)

ventana.show()
app.exec_()