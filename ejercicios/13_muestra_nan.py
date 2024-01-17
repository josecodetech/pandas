import pandas as pd
import numpy as np
df = pd.DataFrame({'A': [1, np.nan, 3],
                   'B': [4, 5, 6]})
df_nan = df[df['A'].isna()]
print(df)
print(df_nan)
