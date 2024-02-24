import pandas as pd
df = pd.DataFrame({'A': [3, 6, 9],
                   'B': [4, 5, 6]})
df['A_cuadrado'] = df['A'] ** 2
print(df)
