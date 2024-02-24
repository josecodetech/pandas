import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
print(df)
print('*'*25)
df['B'] = df['B'].apply(lambda x: x ** 2)
print(df)
