import pandas as pd

df = pd.read_csv("data/tabela_brasileirao_2024.csv")

print(df.info)

print(df.head(10).to_string(index=False))
df = df.set_index("Posição")
print(df.head(10))