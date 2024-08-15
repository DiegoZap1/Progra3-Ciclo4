# Laboratorio 2- Ejercicio 1
import os

class Perros():
    def __init__(self, nombre, raza, edad, peso, color, dueño, telefono):
        self.nombre = nombre
        self.raza = raza
        self.edad = f"{edad} años"
        self.peso = f"{peso} KG"
        self.tamaño = "Perro Pequeño" if peso < 10 else "Perro Grande"
        self.estado = "NO ATENDIDO"
        self.color = color
        self.dueño = dueño
        self.telefono = telefono

    def registrar(self):
        limpiar_consola()
        self.estado = "ATENDIDO"
        self.mostrar_info()
    
    def mostrar_info(self):
        tipo = ["Nombre: ","Raza: ","Edad: ","Peso: ","Tamaño: ","Color: ","Estado: ","Dueño: ","Telefono: "]
        lista = [self.nombre, self.raza, self.edad, self.peso, self.tamaño, self.color, self.estado, self.dueño, self.telefono]
        print("=========== Perros ==============")
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")
        print("=================================")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def registro():
    nombre = input("Ingrese el nombre del perro: ")
    raza = input("Raza: ")
    edad = int(input("Ingrese la edad: "))
    peso = int(input("Ingrese el peso: "))
    color = input("Ingrse el color: ")
    dueño = input("Nombre del dueño: ")
    telefono = input("Telefono: ")
    miperro = Perros(nombre,raza,edad,peso,color,dueño,telefono)
    miperro.registrar()

registro()