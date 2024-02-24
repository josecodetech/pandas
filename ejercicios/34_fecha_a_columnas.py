import pandas as pd
df = pd.DataFrame({'date': 
    pd.date_range(start='2024-01-01', 
                  periods=30)})
df['año'] = df['date'].dt.year
df['mes'] = df['date'].dt.month
df['dia'] = df['date'].dt.day
print(df.head())
