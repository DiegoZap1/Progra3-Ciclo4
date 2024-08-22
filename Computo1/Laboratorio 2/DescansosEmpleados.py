'''
Problema:
Una compañia desea poder medir cuanto tiempo debe de permitirle a los trabajadores tomar un descanso de sus labores
por lo tanto se tienen en cuenta las siguientes politicas de la compañia:

1- Si el empleado tiene menos de 6 meses trabajando, todavia no tiene derecho a un descanso.
2- Si el empleado tiene de 6 o 12 meses trabajando, tendra derecho a una semana de descanso.
3- Si el empleado tiene de 12 a 18 meses trabajando, tendra derecho a un mes de descanso.

Objetivo:
Implementar un programa que calcule a cuanto tiempo de descanso posee un empleado en base a los meses de trabajo
que este haya hecho.
'''
import os

class DescansoEmpleados:
    def __init__(self, nombre, mesestrabajados):
        self.nombre = nombre
        self.mesestrabajados = mesestrabajados
        self.descanso = ""

    def calcular_descanso(self):
        if self.mesestrabajados < 6:
            self.descanso = "Todavía no hay descanso"
        elif 6 <= self.mesestrabajados <= 12:
            self.descanso = "1 Semana de descanso"
        elif 13 <= self.mesestrabajados <= 18:
            self.descanso = "1 Mes de descanso"
        else:
            self.descanso = "Valor no admitido"

    def mostrarinfo(self):
        info = ["Nombre del empleado: ", "Meses trabajados: ", "Descanso: "]
        tipo = [self.nombre, self.mesestrabajados, self.descanso]
        for i in range(len(tipo)):
            print(f"{info[i]}{tipo[i]}")

def gestiondescansos():
    nombre = input("Ingrese el nombre del empleado: ")
    meses = int(input("Ingrese los meses trabajados: "))
    desc = DescansoEmpleados(nombre, meses)
    desc.calcular_descanso()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==================================")
    desc.mostrarinfo()
    print("==================================")

gestiondescansos()