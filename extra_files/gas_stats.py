import pandas as pd

df = pd.read_excel('assets/gas_stats.xlsx')

dg = pd.read_json('assets/gas_stats.json')

dh = pd.read_csv('assets/gas_stats.csv')

print(df)
print(dg)
print(dh)