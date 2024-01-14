import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
df_filtrado= df[df['A'] > 2]
print(df)
print(df_filtrado)
