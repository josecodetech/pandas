import pandas as pd
df = pd.DataFrame({'A': [1, 25, 13,41, 5, 6], 
                   'B': [4, 5, 6,9,10,54], 
                   'C': [72, 18, 9, 10, 11,14]})
agrupado = df.groupby(['A','B']).count()
print(df)
print('*'*25)
print(agrupado)
