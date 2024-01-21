import pandas as pd
df = pd.DataFrame({'A': [10, 21, 32], 
                   'B': [41, 15, 64]})
varianza = df.var()
print(df)
print('*'*20)
print(varianza)
