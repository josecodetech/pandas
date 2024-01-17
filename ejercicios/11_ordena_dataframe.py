import pandas as pd
df = pd.DataFrame({'A': [3, 1, 2], 
                   'B': [6, 5, 4]})
df_ordenado = df.sort_values(by='A')
print(df_ordenado)
