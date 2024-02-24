import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
df['nueva_columna'] = df['A'] + df['B']
print(df)
