import pandas as pd
df = pd.DataFrame({'A': [1, 2], 
                   'B': [3, 4]})
df_transpuesta = df.T
print(df)
print('*'*20)
print(df_transpuesta)
