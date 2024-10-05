import matplotlib.pyplot as plt
import pandas as pd

# Archivo
df = pd.read_csv('Computo 2\Laboratorio 2\csv\Rendimiento de estudiantes.csv')
df['Hours_Studied'] = pd.to_numeric(df['Hours_Studied'])

# Datos de horas
menos10Horas = df[(df['Hours_Studied'] >= 1) & (df['Hours_Studied'] <= 10)].shape[0] #365
entre11a25 = df[(df['Hours_Studied'] >= 11) & (df['Hours_Studied'] <= 25)].shape[0] #5069
entre26a44 = df[(df['Hours_Studied'] >= 26) & (df['Hours_Studied'] <= 44)].shape[0] #1173
valores = [menos10Horas,entre11a25,entre26a44]

# Convertir a porcentajes
total = sum(valores)
porcentaje_horas = [(valor/total)*100 for valor in valores]

# Mostrar en grafico de pastel
label = ['Menos de 10 Horas','Entre 11 a 25 Horas','Entre 26 a 44 Horas']
plt.pie(porcentaje_horas, autopct='%1.1f%%',labels=label)
plt.title('Horas estudiadas')
plt.show()