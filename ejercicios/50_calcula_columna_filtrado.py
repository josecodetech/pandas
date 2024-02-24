import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [10, 20, 30, 40, 50]})
df['C'] = df['A'] * df['B']
print(df)
print('*'*25)
df_filtrado = df[df['C'] > 100]
print(df_filtrado)