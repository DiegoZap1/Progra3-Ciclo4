import os
import math
'''velocidad = [98,85,99,91,94,97,86,75]
media_velocidad = round(sum(velocidad) / len(velocidad), 2)

print(f"La media de velocidad es: {media_velocidad}")

suma = lambda x : x + 2
print(suma(3))

def suma(x):
    return x+2

print(suma(20))

texto = lambda x,y,z: print(f"El valor es {x}")
texto(2,3,4)

def hacer_pizza(size, *toppings):
    print(f"Haciendo una Pizza {size} con los siguientes ingredientes: ")
    for topping in toppings:
        print(f"- {topping}")

def datoscli(nombre, dir, telf):
    print(f"------Datos Cliente-----\nNombre: {nombre}\nDireccion: {dir}\nTelefono: {telf}")'''

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


def volumen_cilindro():
    limpiar_consola()
    radio = float(input("Inserte el radio: "))
    altura = float(input("Inserte la altura: "))
    print("==============")
    print(f"El volumen del cilindro es: {round(math.pi * (radio ** 2) * altura, 2)} m3")
    

def volumen_esfera():
    limpiar_consola()
    radio = float(input("Ingrese el radio: "))
    print("==============")
    print(f"El volumen de la esfera es: {round(math.pi*(radio**3)*(4/3), 2)} m3")

def volumen_cono():
    limpiar_consola()
    radio = float(input("Ingrese el radio: "))
    altura = float(input("Ingrese la altura: "))
    print("==============")
    print(f"El volumen del cono es: {round(altura*math.pi*(radio**2)*(1/3), 2)} m3")

def menu():
    limpiar_consola()
    tipo = ["Volumen Cilindro", "Volumen Esfera", "Volumen Cono"]
    print("==== Menu ====")
    for i in range(1,4):
        print(f"{i}. {tipo[i-1]}")
    print("==============")
    respuesta = int(input("Que quiere hacer?: "))

    if respuesta == 1:
        volumen_cilindro()
    elif respuesta == 2:
        volumen_esfera()
    elif respuesta == 3:
        volumen_cono()
    else:
        print("La respuesta no existe")
