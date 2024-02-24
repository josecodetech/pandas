import pandas as pd
df1 = pd.DataFrame({'A': [1, 2, 3], 
                    'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 
                    'B': [10, 11, 12]})
df_concatenado = pd.concat([df1, df2])
print(df_concatenado)
