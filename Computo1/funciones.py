def doblar_valor(numero):
    n2 = numero * 2
    return n2

num = 20
print(doblar_valor(num))


def describir(tipo, nombre_mascota):
    print(f"Mi mascota es un {tipo} y se llama {nombre_mascota}")

describir("Perro", "Tito")
describir("Gato", "Michi")

def estudiante():
    nombre = input("Nombre del estudiante: ")
    carnet = input("Carnet del estudiante: ")
    carrera = input("Carrera del estudiante: ")
    sede = input("Sede del estudiante: ")
    print("==========================")
    print(f"Nombre: {nombre}")
    print(f"Carnet: {carnet}")
    print(f"Carrera: {carrera}")
    print(f"Sede: {sede}")

estudiante()