import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, None, 6],
                   'C': [None, 9, 4]
                   })
df_sin = df.fillna(0)
print(df)
print('*'*25)
print(df_sin)
