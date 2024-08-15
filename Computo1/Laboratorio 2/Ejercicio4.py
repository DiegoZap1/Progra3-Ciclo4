import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

class celulares():
    def __init__(self,nombre,procesador,ram,pantalla,camara,bateria,os,almacenamiento,precio_compra):
        self.marca = "PHR"
        self.nombre = nombre
        self.procesador = procesador
        self.ram = f"{ram} Ram"
        self.pantalla = f"{pantalla} px"
        self.camara = f"{camara} Mpx"
        self.bateria = f"{bateria   } mAh"
        self.os = os
        self.almacenamiento = f"{almacenamiento} GB"
        self.precio_compra = precio_compra
        self.precio_venta = round(precio_compra * 1.7, 2)

    def mostrarinfo(self):
        tipo = ["Marca: ","Nombre: ","Procesador: ","Ram","Pantalla: ","Camara: ",
                "Bateria: ","Sistema Operativo: ","Almacenamiento: ","Precio: "]
        lista = [self.marca,self.nombre,self.procesador,self.ram,self.pantalla,
                 self.camara,self.bateria,self.os,self.almacenamiento,self.precio_venta]
        print("===========Celular==================")
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")

class tablets():
    def __init__(self,nombre,procesador,ram,pantalla,camara,bateria,os,almacenamiento,precio_compra):
        self.marca = "PHR"
        self.nombre = nombre
        self.procesador = procesador
        self.ram = f"{ram} Ram"
        self.pantalla = f"{pantalla} px"
        self.camara = f"{camara} Mpx"
        self.bateria = f"{bateria} mAh"
        self.os = os
        self.almacenamiento = f"{almacenamiento} GB"
        self.precio_compra = precio_compra
        self.precio_venta = round(precio_compra * 1.7, 2)

    def mostrarinfo(self):
        tipo = ["Marca: ","Nombre: ","Procesador: ","Ram","Pantalla: ","Camara: ",
                "Bateria: ","Sistema Operativo: ","Almacenamiento: ","Precio: "]
        lista = [self.marca,self.nombre,self.procesador,self.ram,self.pantalla,
                 self.camara,self.bateria,self.os,self.almacenamiento,self.precio_venta]
        print("=========== Tablet =============")
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")

class laptops():
    def __init__(self,nombre,procesador,ram,pantalla,camara,bateria,os,almacenamiento,precio_compra):
        self.marca = "PHR"
        self.nombre = nombre
        self.procesador = procesador
        self.ram = f"{ram} Ram"
        self.pantalla = f"{pantalla} px"
        self.camara = f"{camara} Mpx"
        self.bateria = f"{bateria} mAh"
        self.os = os
        self.almacenamiento = almacenamiento
        self.precio_compra = precio_compra
        self.precio_venta = round(precio_compra * 1.7, 2)
    
    def mostrarinfo(self):
        tipo = ["Marca: ","Nombre: ","Procesador: ","Ram","Pantalla: ","Camara: ",
                "Bateria: ","Sistema Operativo: ","Almacenamiento: ","Precio: "]
        lista = [self.marca,self.nombre,self.procesador,self.ram,self.pantalla,self.camara,
                 self.bateria,self.os,self.almacenamiento,self.precio_venta]
        print("=========== Laptop =============")
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")

def menu():
    limpiar_consola()
    print("========= Menu ========")
    print("1. Registrar Celular")
    print("2. Registrar Tablet")
    print("3. Registrar Laptop")
    print("=======================")
    opcion = int(input("Que quiere hacer? : "))
    if opcion == 1:
        registrocelulares()
    elif opcion == 2:
        registrotablets()
    elif opcion == 3:
        registrolaptops()
    else:
        print("Opcion no valida")

def registrocelulares():
    limpiar_consola()
    nombre = input("Como se llama el celular: ")
    procesador = input("Procesador: ")
    ram = int(input("Ram: "))
    pantalla = input("Resolución de pantalla: ")
    camara = int(input("Megapixeles de camara: "))
    bateria = int(input("Capacidad de la bateria: "))
    os = input("Sistema operativo: ")
    almacenamiento = int(input("Capacidad de almacenamiento: "))
    precio = float(input("Precio de compra: "))
    telefono = celulares(nombre,procesador,ram,pantalla,camara,bateria,os,almacenamiento,precio)
    limpiar_consola()
    telefono.mostrarinfo()
    print("=================================")  

def registrotablets():
    limpiar_consola()
    nombre = input("Como se llama la tableta: ")
    procesador = input("Procesador: ")
    ram = int(input("Ram: "))
    pantalla = input("Resolución de pantalla: ")
    camara = int(input("Megapixeles de camara: "))
    bateria = int(input("Capacidad de la bateria: "))
    os = input("Sistema operativo: ")
    almacenamiento = int(input("Capacidad de almacenamiento: "))
    precio = float(input("Precio de compra: "))
    tablet = tablets(nombre,procesador,ram,pantalla,camara,bateria,os,almacenamiento,precio)
    tablet.mostrarinfo()
    print("=================================")

def registrolaptops():
    limpiar_consola()
    nombre = input("Como se llama la laptop: ")
    procesador = input("Procesador: ")
    ram = int(input("Ram: "))
    pantalla = input("Resolución de pantalla: ")
    camara = int(input("Megapixeles de camara: "))
    bateria = int(input("Capacidad de la bateria: "))
    os = input("Sistema operativo: ")
    almacenamiento = int(input("Capacidad de almacenamiento: "))
    precio = float(input("Precio de compra: "))
    laptop = laptops(nombre,procesador,ram,pantalla,camara,bateria,os,almacenamiento,precio)
    limpiar_consola()
    laptop.mostrarinfo()
    print("=================================")

menu()