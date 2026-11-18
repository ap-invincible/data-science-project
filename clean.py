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
print(df.shape)
print("#####################")

df_filled = df.fillna({"Points": 0, "Driver": "Unknown"})
print(df_filled.head(6))

df_clean = df.dropna()
print(df_clean.shape)

df_clean.to_csv("f1_2026_cleaned.csv", index=False)
