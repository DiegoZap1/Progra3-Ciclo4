class carro():
    def __init__(self,color,marca,modelo,placa,clase,trm):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.clase = clase
        self.trm = trm

    def datos(self):
        tipo = ["Color: ","Marca: ","Modelo: ","Placa: ", "Clase: ","Transmision: "]
        datos = [self.color,self.marca,self.modelo,self.placa, self.clase,self.trm]

        print("Datos Vehiculo: \n===================")
        for i in range(0,len(datos)+1):
            print(f"{tipo[i-1]} {datos[i-1]}")
        print("===================")
    
    def encender(self):
        if (self.trm == "Manual"):
            while True:
                estado = input("¿El carro esta en neutro? (S/N): ")
                if (estado.lower() == "s"):
                    print("Se ha dado vuelta a la llave")
                    print("El carro esta encendido")
                    break
                else:
                    print("El carro no enciende")
                    continue
            print("===========================")

    def cambio():
        pass

    def acelerar(self):
        if (self.trm == "Manual"):
            print("Se ha utilizado el clutch")
            print("Se ha cambiado a primera velocidad")
            print("Se ha soltado el clucth despacio")
            print("Se ha utilizado el acelerador")
            print("El carro se ha puesto en marcha")
        else:
            print("Se ha presionado el clutch")
            print("Se ha utilizado el freno")
            

    def frenar():
        pass


car = carro("Rojo","Mitsubishi","Eclipse","P35DFD","Automovil","Manual")
car.datos()
car.encender()
car.acelerar()











'''class MIPERRO():
    def __init__(self,nombre,raza,pasos):
        self.nombre = nombre
        self.raza = raza
        self.pasos = pasos

    def saludo(self):
        print(f"Hola mi perro se llama{self.nombre}, y es raza {self.raza}")
    
    def ladrar(self):
        print(f"{self.nombre} ladra a otros perros")
    
    def camina(self):
        print(f"{self.nombre} camina {self.pasos} pasos")
    
miperro = MIPERRO("Tito","Maltes",60)

miperro.saludo()
miperro.ladrar()
miperro.camina()'''