import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, 4], 
                   'B': [4, 5, 6, 7]})
df_agrupado = df.groupby('A')['B'].count()
print(df)
print('*'*25)
print(df_agrupado)
