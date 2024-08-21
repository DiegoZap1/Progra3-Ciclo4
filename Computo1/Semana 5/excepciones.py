while True:
    try:
        def dividir(n,n2):
            total = n / n2
            return total
        num1 = int(input("Escribe un numero: "))
        num2 = int(input("Escribe otro numero: "))
        print(dividir(num1,num2))
        op = input("Desea hacer otra division? (s/n): ").lower()
        if op == "s":
            continue
        elif op == "n":
            break
        else:
            print("Opcion no valida")
    except:
        print(Exception)