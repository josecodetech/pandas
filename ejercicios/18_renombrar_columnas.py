import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
print(df)
print('*'*25)
df.rename(columns={'A': 'Column1', 
                   'B': 'Column2'}, 
          inplace=True)
print(df)
