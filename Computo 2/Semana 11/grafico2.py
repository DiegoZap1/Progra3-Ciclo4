import matplotlib.pyplot as plt

dep = ['San Miguel','Morazan','La Union','Usulutan']
frec = [18,2,3,3]
colores = ['green','purple','black','Blue']

plt.bar(dep,frec, color = colores)
plt.title("Lugares de procedencia")
plt.xlabel("Departamentos")
plt.ylabel("Frecuencia")
plt.show()