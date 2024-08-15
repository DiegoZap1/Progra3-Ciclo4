class libro():
    def __init__(self,titulo,autor,edicion):
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.editorial = "Libreria El Salvador"

    def datos(self):
        print(f"Titulo: {self.titulo}\n"+
              f"Autor: {self.autor}\n"+
              f"Edicion: {self.edicion}\n"+
              f"Editorial: {self.editorial}")

lib = libro("La illiada","Homero","Primera Edicion")
lib.datos()