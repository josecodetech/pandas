import pandas as pd
import numpy as np
fechas = pd.date_range('20230101', periods=6)
serie = pd.Series(np.random.randn(6), index=fechas)
print(serie)
