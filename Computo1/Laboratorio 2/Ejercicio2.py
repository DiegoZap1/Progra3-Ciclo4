# Laboratorio 2- Ejercicio 2
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

class lapices():
    def __init__(self,tipo,precio_compra):
        self.nombre = "Lapiz"
        self.tipo = tipo
        self.precio_compra = precio_compra
        self.precio_venta = round(precio_compra * 1.30, 2)
    
    def mostrarinfo(self):
        limpiar_consola()
        tipo = ["Nombre: ","Tipo: ","Precio: "]
        lista = [self.nombre,self.tipo,self.precio_venta]
        print("============= Lapiz ===============")
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")
        
class cuadernos():
    def __init__(self,hojas,precio_compra):
        self.nombre = "Cuadernos HOJITAS"
        self.hojas = hojas
        self.precio_compra = precio_compra
        self.precio_venta = round(precio_compra * 1.30, 2)
        
    def mostrarinfo(self):
        tipo = ["Nombre: ","Hojas: ","Precio: "]
        lista = [self.nombre,self.hojas,self.precio_venta]
        print("============= Cuaderno ============")
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")
        print("===================================")

def menu():
    print("========= Menu ========")
    print("1. Registrar Lapices")
    print("2. Registrar Cuadernos")
    print("=======================")
    opcion = int(input("Que quiere hacer? : "))
    if str(opcion) == "1":
        registroLapices()
    elif str(opcion) == "2":
        registroCuadernos()
    else:
        print("Opcion no valida")


def registroLapices():
    limpiar_consola()
    print("===================================")
    tipo = input("Tipo de lapiz: ")
    precio = float(input("Precio de compra: "))
    items_lapices = lapices(tipo,precio)
    limpiar_consola()
    items_lapices.mostrarinfo()
    print("===================================")


def registroCuadernos():
    limpiar_consola()
    print("===================================")
    hojas = int(input("Numero de hojas: "))
    precio = float(input("Precio de compra: "))
    items_cuadernos = cuadernos(hojas,precio)
    limpiar_consola()
    items_cuadernos.mostrarinfo()
    print("===================================")

menu()
