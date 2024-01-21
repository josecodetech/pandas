import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
df['A_cumsum'] = df['A'].cumsum()
print(df)
print('*'*25)

