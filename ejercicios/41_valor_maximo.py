import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
max_B = df['B'].max()
print(df)
print('*'*25)
print(max_B)
