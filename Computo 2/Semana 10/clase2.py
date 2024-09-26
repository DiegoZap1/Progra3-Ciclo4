import pandas as pd

archivo = "canciones.csv"
df = pd.read_csv(archivo)
#print(df)

filtro = df[df['artist(s)_name'].str.contains("Guns")]
print(filtro.head(10))