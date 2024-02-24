import pandas as pd
datos = {'Nombre': ['Juan', 'Ana', 'Pedro', 'Maria'],
        'Edad': [23, 36, 16, 28]}
df = pd.DataFrame(datos)
df['Es_adulto'] = df['Edad'] >= 18
print(df)