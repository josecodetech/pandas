import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
print(df)
df['A'] = df['A'].apply(lambda x: x * 2)
print('*'*25)
print(df)