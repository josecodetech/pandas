import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
print(df)
df['C'] = df['A'] * df['B']
print('-'*25)
print(df)
