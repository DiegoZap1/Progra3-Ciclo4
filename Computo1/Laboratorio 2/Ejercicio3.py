# Laboratorio 2- Ejercicio 3
import os

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

class carrosNacionales():
    def __init__(self,placa,marca,modelo,año,clase,transmision,color,motor,chasis,precio_compra):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.clase = clase
        self.asientos = "5.00 asientos"
        self.ruedas = 4
        self.transmision = transmision
        self.color = color
        self.motor = motor
        self.chasis = chasis
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.4
    
    def mostrarinfo(self):
        tipo = ["Placa: ","Marca: ","Modelo: ","Año: ","Clase: ","Asientos: ",
                "Ruedas: ","Transmision: ","Color: ","Motor: ","Chasis: ","Precio: $"]
        lista = [self.placa,self.marca,self.modelo,self.año,self.clase,self.asientos,
                 self.ruedas,self.transmision,self.color,self.motor,self.chasis,self.precio_venta]
        print("============ Carro Nacional ===============")
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")

class carrosImportados():
    def __init__(self,placa,marca,modelo,año,pais,clase,transmision,color,motor,chasis,precio_compra):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.pais = pais
        self.clase = clase
        self.asientos = "5.00 asientos"
        self.ruedas = 4
        self.transmision = transmision
        self.color = color
        self.motor = motor
        self.chasis = chasis
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.4
    
    def mostrarinfo(self):
        tipo = ["Placa: ","Marca: ","Modelo: ","Año: ","Pais: ","Clase: ","Asientos: ",
                "Ruedas: ","Transmision: ","Color: ","Motor: ","Chasis: ","Precio: $"]
        lista = [self.placa,self.marca,self.modelo,self.año,self.pais,self.clase,self.asientos,
                 self.ruedas,self.transmision,self.color,self.motor,self.chasis,self.precio_venta]
        print("============ Carro Importado =================")
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")
        print("==============================================")

def menu():
    limpiar_consola()
    print("========= Menu ========")
    print("1. Registrar Autos Nacionales")
    print("2. Registrar Autos Importados")
    print("=======================")
    opcion = int(input("Que quiere hacer? : "))
    if opcion == 1:
        registroCNacionales()
    elif opcion == 2:
        registrarCImportado()
    else:
        print("Opcion no valida")

def registroCNacionales():
    limpiar_consola()
    placa = input("Numero de placa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))
    clase = input("Clase: ")
    transmision = input("Transmisión: ")
    color = input("Color")
    motor = input("Motor: ")
    chasis = input("Chasis: ")
    precio = float(input("Comprado por: $"))
    nacionales = carrosNacionales(placa,marca,modelo,año,clase,transmision,color,motor,chasis,precio)
    limpiar_consola()
    nacionales.mostrarinfo()
    print("==============================================")

def registrarCImportado():
    limpiar_consola()
    placa = input("Numero de placa: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))
    pais = input("País: ")
    clase = input("Clase: ")
    transmision = input("Transmisión: ")
    color = input("Color")
    motor = input("Motor: ")
    chasis = input("Chasis: ")
    precio = float(input("Comprado por: $"))
    importados = carrosImportados(placa,marca,modelo,año,pais,clase,transmision,color,motor,chasis,precio)
    limpiar_consola()
    importados.mostrarinfo()    
    print("==============================================")

menu()