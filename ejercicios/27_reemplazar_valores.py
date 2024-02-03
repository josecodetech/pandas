import pandas as pd
df = pd.DataFrame({'A': [1, 1, 2], 
                   'B': [3, 4, 5]})
print(df)
df['A'] = df['A'].replace(1, 10)
print(df)
