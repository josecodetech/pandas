import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6]})
print(df)
df.drop(columns=['B'], inplace=True)
print('-'*25)
print(df)
