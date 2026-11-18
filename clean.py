import pandas as pd

df = pd.read_csv("f1_2026.csv")

print(df.head(5))
print("#####################")
print(df.tail())
print("#####################")
print(df.info())
print("#####################")
print(df.describe())
print("#####################")

df_filled = df.dropna()
print(df_filled.head(6))
print(df_clean.shape)

df_clean.to_csv("f1_2026_cleaned.csv", index=False)
