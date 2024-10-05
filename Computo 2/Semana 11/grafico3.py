import matplotlib.pyplot as plt

# Barras
'''opciones = ['Taco Bell','Pizza Hut','Wendys','McDonalds','China Wok']
votos = [1,15,11,2,5]
colores = ['purple','red','blue','yellow','green']

plt.bar(opciones,votos,color = colores)
plt.title('Votacion de comida')
plt.xlabel('Restaurantes')
plt.ylabel('Votos')
plt.show()'''

# Pie
opciones = ['Taco Bell','Pizza Hut','Wendys','McDonalds','China Wok']
votos = [1,15,11,2,5]
colores = ['purple','red','blue','yellow','green']
label = opciones

plt.pie(votos, autopct='%1.1f%%',labels= label,colors=colores)
plt.title('Votacion de comida')
plt.show()