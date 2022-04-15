import pandas as pd

df_races = pd.read_csv(r"races_UK2.csv")
df_runs = pd.read_csv(r"runners_UK2.csv")

print(df_races.head())
print(df_runs.head())

df_races = df_races.drop(df_races.columns[:2], axis=1)
df_runs = df_runs.drop(df_runs.columns[:2], axis=1)

print(df_races.head())
print(df_runs.head())

df_races.to_csv(r"..\HorsebettingTipsterML\races_UK2.csv")
df_runs.to_csv(r"..\HorsebettingTipsterML\runners_UK2.csv")