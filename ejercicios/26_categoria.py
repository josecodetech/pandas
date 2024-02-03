import pandas as pd
df = pd.DataFrame(
    {'A': ['cat', 'dog', 'fish']})
print(df.dtypes)
df['A'] = df['A'].astype('category')
print('*'*15)
print(df.dtypes)
