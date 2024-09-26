import pandas as pd

data = {'Nombre': ['Ana','Luis','Carlos'],
        'Edad': [23,24,25],
        'Ciudad': ['Madrid','Barcelona','Sevilla']}
df = pd.DataFrame(data)
print(df)