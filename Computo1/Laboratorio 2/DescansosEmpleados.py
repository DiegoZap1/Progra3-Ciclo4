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

class DescansoEmpleados():
    def __init__(self,nombre,mesestrabajados):
        self.nombre = nombre
        self.mesestrabajados = mesestrabajados
        self.descanso = ""

    def descansos(self):
        if self.mesestrabajados < 6:
            self.descanso = "Todavia no hay descanso"
        elif self.mesestrabajados > 6 and self.mesestrabajados == 12:
            self.descanso = "1 Semana de descanso"
        elif self.mesestrabajados >= 13 and self.mesestrabajados >= 18:
            self.descanso = "1 Mes de descanso"

    def mostrarinfo(self):
        self.descansos()
        info = ["Nombre del libro: ","Meses trabajados: ","Descanso: "]
        tipo = [self.nombre,self.mesestrabajados,self.descanso]
        for i in range(1,len(tipo)+1):
            print(f"{info[i-1]}{tipo[i-1]}")

def gestiondescansos():
    nombre = input("Ingrese el nombre del empleado: ")
    meses = int(input("Ingrese los meses trabajados: "))
    desc = DescansoEmpleados(nombre,meses)
    print("==================================")
    desc.mostrarinfo()
    print("==================================")

gestiondescansos()