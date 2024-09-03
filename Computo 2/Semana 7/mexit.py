import sys

nombre = None
print("Escribe tu nombre: ")
sys.stdin.read(nombre)
#print(f"Hola {nombre}")
sys.stdout.write(f"Hola {nombre}")