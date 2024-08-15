class ave():
    def __init__(self, col_plumas,puedev,habitat):
        self.alas = 2
        self.color_plumas = col_plumas
        self.puedev = puedev
        self.habitat = habitat
    
    def graznido(self):
        print("El ave a graznado")
    
    def comer(self, comida):
        print(f"El ave come {comida}")
    
    def dormir(self):
        print("El ave esta durmiendo")

    def ponehuevos(self):
        print(f"El ave ha puesto un huevo")

class gallina(ave):
    def __init__(self,tipo,tcresta,col_plumas, puedev, habitat):
        super().__init__(col_plumas, puedev, habitat)
        self.tipo = tipo
        self.tcresta = tcresta
    
    def datos(self):
        tipo = ["Tipo: ","Tamaño de cresta: ","Color de plumas: ","Puede volar: ","Habitat: "]
        lista = [self.tipo,self.tcresta,self.color_plumas,self.puedev,self.habitat]
        for i in range(1,len(lista)+1):
            print(f"{tipo[i-1]}{lista[i-1]}")
        print("==========================")

    # Overriding
    def graznido(self):
        print("La gallina esta cacareando")
    
    def comer(self, comida):
        print(f"La gallina come {comida}")


gallina1 = gallina("India","Mediana","Negro con anaranjado","No","Granja")
gallina1.datos()
gallina1.graznido()
gallina1.comer("semillas")