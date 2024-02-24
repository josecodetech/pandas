import pandas as pd
df = pd.DataFrame({'A': [10, 5, 3], 
                   'B': [4, 15, 6]})
df_ordenado = df.sort_values(by='A')
print(df)
print('*'*25)
print(df_ordenado)
