import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1

df = pd.read_excel("catalog_products.xlsx")

print("Форма DataFrame:", df.shape)
print("====================================================")

print("\n Типы данных:")
print(df.dtypes)
print("====================================================")

print("\nПропуски")
print(df.isnull().sum())
print(df.head)

print("====================================================")
print("\nПервые 5 строк:")
print(df.head())


# 2
numeric_col = df.select_dtypes(include=['number']).columns

df[numeric_col] = df[numeric_col].astype(float)

df[numeric_col] = df[numeric_col].fillna(df[numeric_col].mean())

print(df[numeric_col])


# 3
df["total_price"] = df["col_2"] * df["col_3"]
df["double_stock"] = df["col_5"] * 2
df["log_price"] = np.log(df["col_2"])

print(df[["total_price", "double_stock", "log_price"]].head())


# 4
electronics = df[df['col_7'] == 'Electronics']
price_500 = df[df['col_2'] > 500]

print(electronics.head(5), price_500.head(5))

# 5
grouped_df = df.groupby("col_7").agg(
    mean_price=("col_2", "max"),
    max_price=("col_2","mean"),
    total_quantity=('col_3', 'sum')
).reset_index()

print(grouped_df.head())


# 6
print("6")
numeric = df.loc[:, 'col_2':'col_11']
for col in numeric:
    numeric[col] = pd.to_numeric(numeric[col], errors ='coerce')
numeric_df = numeric.agg(["mean", "median", "std"]).T

df_num = numeric_df.reset_index()
df_num.columns = ['column', 'mean', 'median', 'std']

print(df_num.head())

# 7
price_mean = df['col_2'].mean()
price_std = df['col_2'].std()

anomalies = df[df["col_2"] > price_mean + 3 * price_std]

result = anomalies[["col_2"]]
print(result.head())

#8


arrange = df.loc[:, 'col_2':'col_11']
to_number = arrange.apply(pd.to_numeric, errors='coerce')

corr = to_number.corr()


print(corr)

# 9
# plt.figure()

# plt.hist(df['col_2'], bins=50)

# plt.title('Price Distribution')
# plt.xlabel('Price')
# plt.ylabel('Count')

# plt.grid(True)
# plt.show()

# 10
# plt.figure()

# sns.regplot(x=df['col_6'], y=df['col_5'])
# plt.xlabel("Price")
# plt.ylabel("count")

# plt.grid()

# plt.show()

# 11
plt.figure()

# sns.boxplot(x=df['col_7'], y=df['col_2'])

# plt.title('Category price')
# plt.xlabel('Category')
# plt.xlabel('Price')

# plt.grid()
# plt.show()

# 12
# numeric = df.loc[:, 'col_2':'col_6']

# for col in numeric:
#     numeric[col] = pd.to_numeric(numeric[col], errors = 'coerce')

# numeric['category'] = df['col_7']
# sns.pairplot(numeric, hue='category')

# plt.show()


#13
# numeric = df.loc[:, 'col_2':'col_11']

# for col in numeric:
#     numeric[col] = pd.to_numeric(numeric[col], errors='coerce')

# corr = numeric.corr()

# plt.figure()

# sns.heatmap(corr, annot=True)

# plt.title("Корреляционная матрица")

# plt.show()

#14
# final_df = df[["col_2", "col_3", "total_price", "double_stock", "log_price"]]

# final_df.to_excel("catalog_analysis.xlsx", index=False)

# 15
category_summary = df.groupby("col_7").agg(
    count=("col_2", "count"),
    mean_price=("col_2", "mean"),
    total_quantity=("col_3", "sum"),
    mean_log_price=("log_price", "mean")
).reset_index()

print(category_summary.head())

#16
price_category = df.groupby('col_7').agg(
    max_price=('col_2', 'max'),
    name_item=('col_1', 'first')
)


print(price_category.head())


#17
df["total_value"] = df["col_2"] * df["col_3"]

print(df[["col_2", "col_3", "total_value"]].head(10))

#18
# bins = [0, 50, 200, 500, 1000, float('inf')]
# labels = ['до 50', '50-200', '200-500', '500-1000', '1000+']

# df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)
# count_df = df['price_range'].value_counts().sort_index()

# count_df = count_df.reset_index()
# count_df.columns = ["price_range", "count"]
# plt.figure()

# sns.barplot(x="price_range", y="count", data=count_df)

# plt.title("Распределение товаров по диапазонам цен")
# plt.xlabel("Диапазон цен")
# plt.ylabel("Количество товаров")

# plt.grid()
# plt.show()

#19
df["stock_value"] = df["col_2"] * df["col_3"]
grouped = df.groupby("col_7").agg(
    total_stock_value=("stock_value", "sum")
).reset_index()
max_category = grouped.loc[grouped["total_stock_value"].idxmax()] # I MUST CHEK TOMORROW

print(max_category)
# plt.figure()

# sns.barplot(x="col_7", y="total_stock_value", data=grouped)

# plt.title("Суммарная стоимость товаров по категориям")
# plt.xlabel("Категория")
# plt.ylabel("Общая стоимость")

# plt.xticks(rotation=45)
# plt.grid()

# plt.show()

#20
grouped = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    third_price=('col_3', 'mean')
).reset_index()

print(grouped.head())
# plt.figure()

# sns.scatterplot(x='mean_price', y='third_price', data=grouped)
# plt.title('mean price and stock')
# plt.xlabel('mean_price')
# plt.ylabel('third_price')

# plt.show()

#21
grouped = df.groupby('col_7').agg(
    std=('col_2', 'std')
).reset_index()


print(grouped.head())
# plt.figure()

# sns.barplot(x='std', y = 'col_7', data=grouped)

# plt.title('Разброс цен по категорям')
# plt.xlabel('standart std price')
# plt.ylabel('category')

# plt.grid()
# plt.show()

#22
df_zero = df[df['col_3'].fillna(0) != 0]
print(df_zero.head())

df_sort = df[['col_1', 'col_7', 'col_2']]

print(df_sort.head())

#23
grouped = df.groupby("col_7").agg(
    count=("col_7", "count")
).reset_index()
grouped = grouped.rename(columns={"col_7": "category"})

top5 = grouped.sort_values(by="count", ascending=False).head(5)

print(top5)
# plt.figure()

# sns.barplot(x="count", y="category", data=top5)

# plt.title("Топ-5 категорий по количеству товаров")
# plt.xlabel("Количество товаров")
# plt.ylabel("Категория")

# plt.grid()
# plt.show()


#24
sd_df = df.sort_values(by='col_3', ascending=False)
print(sd_df.head(10))

# plt.figure()

# sns.barplot(x='col_3', y='col_1', data=sd_df)

# plt.show()

#25

bins = [0, 50, 200, 500, 1000, float("inf")]
labels = ["0-50", "50-200", "200-500", "500-1000", ">1000"]

df["price_range"] = pd.cut(df["col_2"], bins=bins, labels=labels)


pivot = pd.pivot_table(
    df,
    index="col_7",
    columns="price_range",
    values="col_2",
    aggfunc="count",
    fill_value=0
)

print(pivot)


plt.figure()

sns.heatmap(pivot, annot=True)

plt.title("Тепловая карта категорий и диапазонов цен")
plt.xlabel("Диапазон цены")
plt.ylabel("Категория")

plt.show()