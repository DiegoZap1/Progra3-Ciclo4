import matplotlib.pyplot as plt
import pandas as pd

# Archivo
df = pd.read_csv('Computo 2\Laboratorio 2\csv\datos de clientes.csv')
df['age'] = pd.to_numeric(df['age'])

clientesde20a29 = df[(df['age'] >= 20) & (df['age'] <= 29)].shape[0] #51
clientesde30a40 = df[(df['age'] >= 30) & (df['age'] <= 40)].shape[0] #82
clientesde41a55 = df[(df['age'] >= 41) & (df['age'] <= 55)].shape[0] #105

tipo = ["20-29","30-40","41-55"]
datos = [clientesde20a29,clientesde30a40,clientesde41a55]
colores = ['tab:orange', 'tab:green', 'tab:blue']

plt.bar(tipo, datos, color = colores)
plt.title('Cantidad de usuarios')
plt.xlabel('Edad de los clientes')
plt.ylabel('Edades')
plt.plot()
plt.show()