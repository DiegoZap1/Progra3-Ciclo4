import matplotlib.pyplot as plt
import pandas as pd
# Archivo
df = pd.read_csv('Computo 2\Laboratorio 2\csv\BreakingBadData.csv')
filtrotemporada = pd.to_numeric(df['Season'])
filtroRating = pd.to_numeric(df['Rating'])

nEpisodiosTemp1 = df[(df['Season'] == 1)].shape[0]# 7 Episodios
ratingTemp1 = 61.4 # Total calculado sumando los ratings de cada episodio
promedioTemp1 = round(ratingTemp1 / nEpisodiosTemp1,2)

nEpisodiosTemp2 = df[(df['Season'] == 2)].shape[0] # 13 Episodios
ratingTemp2 = 115.1 # Total calculado sumando los ratings de cada episodio
promedioTemp2 = round(ratingTemp2 / nEpisodiosTemp2,2)

nEpisodiosTemp3 = df[(df['Season'] == 3)].shape[0] # 13 Episodios
ratingTemp3 = 114.5 # Total calculado sumando los ratings de cada episodio
promedioTemp3 = round(ratingTemp3 / nEpisodiosTemp3,2)

nEpisodiosTemp4 = df[(df['Season'] == 4)].shape[0] # 13 Episodios
ratingTemp4 = 117.3 # Total calculado sumando los ratings de cada episodio
promedioTemp4 = round(ratingTemp4 / nEpisodiosTemp4,2)

nEpisodiosTemp5 = df[(df['Season'] == 5)].shape[0] # 16 Episodios
ratingTemp5 = 150.9 # Total calculado sumando los ratings de cada episodio
promedioTemp5 = round(ratingTemp5 / nEpisodiosTemp5,2)

fig, ax = plt.subplots()

# Datos a mostrar
temporadas = ["Temporada 1","Temporada 2","Temporada 3","Temporada 4","Temporada 5"]
ratings = [promedioTemp1,promedioTemp2,promedioTemp3,promedioTemp4,promedioTemp5]

plt.plot(temporadas,ratings,"D-")
plt.title("Ratings Breaking Bad por temporadas")
plt.ylabel("Ratings")
plt.show()