import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [1, np.nan, 3], 
                   'B': [4, 5, 6]})
print(df)
df.dropna(inplace=True)
print('*'*25)
print(df)
