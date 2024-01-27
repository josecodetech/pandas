import pandas as pd
df = pd.DataFrame({'A': [1, 3, 4], 
                   'B': [4, 5, 6]})
df_filtrado = df[(df['A'] > 2) & 
                 (df['A'] < 5)]
print(df)
print('*'*10)
print(df_filtrado)
