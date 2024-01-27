import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
print(df)
correlacion = df['A'].corr(df['B'])
print('*'*25)
print(correlacion)
