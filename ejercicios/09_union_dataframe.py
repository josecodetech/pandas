import pandas as pd
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 
                    'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 
                    'value': [4, 5, 6]})
merged_df = pd.merge(df1, df2, on='key')
print(df1)
print(df2)
print(merged_df)
