import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
print(df)
print('*'*25)
df['A'] = df['A'].map(
    {1: 'uno', 2: 'dos', 3: 'tres'})
print(df)