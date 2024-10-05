import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'nombres': ['Diego Zapata','Juan Perez','María José',
                'Carlos ','Angel','Fernanda','Ana','Luis'],
    'edad': [19,21,20,20,19,18,20,24]
})

frecuencia = df['edad'].value_counts()

plt.bar(frecuencia.keys(),frecuencia)
plt.show()