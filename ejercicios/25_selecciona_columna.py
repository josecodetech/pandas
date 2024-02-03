import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
a_columna = df['A']
print(df)
print('*'*20)
print(a_columna)
