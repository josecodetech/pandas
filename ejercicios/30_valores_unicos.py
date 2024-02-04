import pandas as pd
df = pd.DataFrame(
    {'A': [1, 2, 2, 3, 3]})
cuenta_unicos = df['A'].nunique()
print(df)
print('-'*20)
print(cuenta_unicos)
