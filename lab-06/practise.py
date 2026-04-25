import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

df = pd.read_excel('catalog_products.xlsx')
#1

grouped = df.groupby('col_7').agg(
    max_price=('col_2', 'max')
).reset_index()

grouped = grouped.rename(columns={'col_7':'catalog'})

print(grouped.head())

#2
numeric_to = df.loc[df['col_2'] > 700, ['col_1', 'col_2']]

numeric_to = numeric_to.rename(columns={'col_1':'catalog', 'col_2':'price>700'})

print(numeric_to.head())

#3
df['col_3'] = df['col_3'].fillna(df['col_2'].mean())

df['col_3'] = df['col_3'].fillna(0)

# df = df.rename(columns={
#     'col_2':'price',
#     'col_3':'stock'
# })

# print(df[['price', 'stock']].head())

#4


# выбрать col_2 - col_11
numeric = df.loc[:, 'col_2':'col_11']

# статистика
grouped = numeric.agg(['mean', 'median', 'std']).T.reset_index()

# переименовать колонки
grouped.columns = ['column', 'mean', 'median', 'std']

print(grouped.head(10))
