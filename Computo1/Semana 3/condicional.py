'''name = input("Digita tu nombre: ")
age = int(input("Digita tu edad: "))
if (name.title() == "Alice"):
    print("Hi, Alice")
elif (name.title() == "Angela"):
    print("Hi, Angela")
elif age < 12:
    print("You are not Alice, kiddo")
else:
    print("Hi, stranger, you are not Alice")'''

'''num1 = int(input("Escribe un numero: "))
num2 = int(input("Escribe otro numero: "))
num3 = int(input("Escribe otro numero: "))

if (num1 > num2 and num1 > num3):
    print(f"El numero mayor es: {num1}")
elif (num2>num1 and num2 > num3):
    print(f"El numero mayor es: {num2}")
elif (num3>num2 and num3>num1):
    print(f"El numero mayor es: {num3}")
else:
    print("Los numeros son iguales")'''

'''num = int(input("Cuantos numeros ingresara?: "))
lista = []
while (num > 0):
    numeros = int(input("Ingrese un numero: "))
    lista.append(numeros)

    num -= 1
    if num == 0:
        break

mayor = max(lista)
menor = min(lista)

print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")

lista.remove(mayor)
lista.remove(menor)

print(f"El numero de en medio es: {lista[0]}")'''
# 🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀🙀

'''for i in range(5):
    print("Bucle for")

def datos(nomb, *materias):
    num = 1
    print(f"Nombre del estudiante: {nomb}")
    print("Materias que cursa: ")
    for m in materias:
        print(f"{num}-{m}")
        num+=1

datos("Juan Perez","Programacion","Base de datos","Redes")'''