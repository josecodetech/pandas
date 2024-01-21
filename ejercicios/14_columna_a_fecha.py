import pandas as pd
df = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-02'], 
    'value': [1, 2]})
df['date'] = pd.to_datetime(df['date'])
print(df)
