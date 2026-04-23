
import numpy as np
import pandas as pd
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name.strip()

        if "@" in email:
            self.email = email
        else:
            raise ValueError("Ошибка в формате email")

        self.registration_date = datetime.now().date()

    def __str__(self):
        return f"User={self.name}, id={self.id}, email={self.email}"

    @staticmethod
    def users_dataframe(users):
        return pd.DataFrame(
            [
                (u.id, u.name, u.email, u.registration_date)
                for u in users
            ],
            columns=["id", "name", "email", "registration_date"]
        )


class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.category = category

        if price < 0:
            self.price = 0
        else:
            self.price = price

    def __str__(self):
        return f"id={self.id}, name={self.name}, price={self.price}, category={self.category}"

    @staticmethod
    def products_dataframe(products):
        return pd.DataFrame(
            [
                (p.id, p.name, p.price, p.category)
                for p in products
            ],
            columns=["id", "name", "price", "category"]
        )


class Order:
    @staticmethod
    def merge_users_orders(users_df, order_df):
        merged = pd.merge(
            order_df,
            users_df,
            left_on="user_id",
            right_on="id"
        )
        merged = merged[["order_id", "name", "total"]]
        merged = merged.rename(columns={"name": "user_name"})
        return merged

    @staticmethod
    def expensive_orders(df):
        return df[df["total"] > 100]

    @staticmethod
    def total_by_user(df):
        return df.groupby("user_name")["total"].sum().reset_index(name="total_sum")


# 20
@app.get("/home")
def home():
    n = np.array([1200, 900, 1500])
    return np.where(n > 1000)[0].tolist()


# 21
users = [
    User(1, "John Doe", "john@example.com"),
    User(2, "Alice", "alice@example.com")
]

users_df = User.users_dataframe(users)
print(users_df)


# 22
products = [
    Product(1, "Laptop", 1200, "Electronics"),
    Product(2, "T-shirt", 20, "Clothing")
]

products_df = Product.products_dataframe(products)
print(products_df)


# 23
users_df2 = pd.DataFrame([
    (1, "John"),
    (2, "Alice")
], columns=["id", "name"])

order_df = pd.DataFrame([
    (101, 1, 1200),
    (102, 2, 25)
], columns=["order_id", "user_id", "total"])

merged_df = Order.merge_users_orders(users_df2, order_df)
print(merged_df)


# 24
df_orders = pd.DataFrame([
    (101, "John", 1200),
    (102, "Alice", 25)
], columns=["order_id", "user_name", "total"])

print(Order.expensive_orders(df_orders))


# 25
df_orders2 = pd.DataFrame([
    (101, "John", 1200),
    (103, "John", 500),
    (102, "Alice", 25)
], columns=["order_id", "user_name", "total"])

print(Order.total_by_user(df_orders2))

#20
# n = np.array([1200, 900, 1500])

# def expensive(n):
#     return np.where( n > 1000)[0]
    

# print(expensive(n))

#21

# def date_frame(df):
#     return pd.DataFrame([
#         (u.id, u.name, u.email, u.registration_date)
#         for u in df
#     ], columns = ["id", "name", "email", "registration_date"])


# df = [
#     User(1, "John Doe", "john@example.com"), 
#     User(2, "Alice", "alice@example.com")
# ]
    
        
    
    

# print(date_frame(df))
#22

# def all_products(products):
#     return pd.DataFrame([
#         (p.id, p.name, p.category, p.price) 
#         for p in products
#     ], columns = ["id", "name", "price", "category"])


# products = [
#     Products(1, "Laptop", 1200, "Electronics"), 
#     Products(2, "T-shirt", 20, "Clothing")
    
# ]

# print(all_products(products))

#23
# users_df = pd.DataFrame([
#     (1, "John"),
#     (2, "Alice")
# ], columns = ["id", "name"])

# order_df = pd.DataFrame([
#     (101, 1, 1200),
#     (102, 2, 25)
# ], columns = ["order_id", "user_id", "total"])

# def merge_df(user_df, order_df):
#     merged = pd.merge(
#         order_df,
#         user_df,
#         left_on = "user_id",
#         right_on = "id"
#     )
#     merged = merged[["order_id", "name", "total"]]
#     merged = merged.rename(columns={"name": "user_name"})

#     return merged

# df  = merge_df(users_df, order_df)
# print(df)

#24
# df = pd.DataFrame([
#     (101, "John", 1200),
#     (102, "Alice", 25)
# ], columns = ["order_id", "user_name", "total"])

# def sorted_price(df):
#     return df[df['total'] > 100]

# print(sorted_price(df))

#25
# df = pd.DataFrame([
#     (101, "John", 1200),
#     (103, "John", 500),
#     (102, "Alice", 25)
# ], columns = ["order_id", "user_name", "total"])

# def total_sum(df):
#     result = df.groupby("user_name")["total"].sum().reset_index(name="total_sum")
#     return result

# print(total_sum(df))







