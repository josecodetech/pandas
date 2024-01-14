import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [4, 5, 6], 'C': [7, 8, 9]})
agrupado = df.groupby('A').sum()
print(df)
print("*"*25)
print(agrupado)