import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [10,5,7,8,1,4]
colores = ['tab:green','tab:red','tab:blue']

plt.bar(x,y, color = colores)
plt.title("Numeros escogidos")
plt.xlabel("Numeros")
plt.ylabel("Frecuencia")
plt.show()