import pandas as pd
df = pd.DataFrame({'A': [1, 1, 2], 
                   'B': [3, 4, 5], 
                   'C': [6, 7, 8],
                   'D': [1, 3, 6]})
agrupado = df.groupby('A').sum()
print(df)
print('-'*25)
print(agrupado)
