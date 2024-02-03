import pandas as pd
json_data = '{"A": [1, 2, 3], "B": [4, 5, 6]}'
df = pd.read_json(json_data)
print(df)
