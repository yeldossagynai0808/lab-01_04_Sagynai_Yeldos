from datetime import datetime

### 1 ###

class User:
    def __init__(self, id, name, email):
        self._id = id
        self._name = name.strip().lower()
        

        if "@" in email:
            self._email = email.strip().lower()
        else:
            raise ValueError
        
        self._registration = datetime.now().date()

    # def __str__(self):
    #     return f"User(id = {self._id}, name = {self._name}, email = {self._email})"

    # def __del__(self):
    #     print("User {self._name} удален ")


# u = User(1, "john dor", "John@Example.COM")
# print(u)

### 2 ###
@classmethod
def from_string(cls, data: str):
    parts = data.split(",")

    if len(parts) != 3:
        raise ValueError("Неверный формат")

    id_str, name, email = parts
    id = int(id_str.strip())
    name = name.strip()
    email = email.strip()

    if "@" not in email or "." not in email:
        raise ValueError("Неверный email")

    return cls(id, name, email)


### 3 ###



class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category='{self.category}')"

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Product) and self.id == other.id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category
        }


class Inventory:
    def __init__(self):
        self._product = {}

    def add_product(self, product):
        self._product[product.id] = product

    def remove_product(self, product_id):
        if product_id in self._product:
            del self._product[product_id]

    def get_product(self, product_id):
        return self._product.get(product_id)

    def get_all_products(self):
        return list(self._product.values())

    def unique_products(self):
        return set(self._product.values())

    def filter_by_price(self, min_price):
        return list(filter(lambda product: product.price >= min_price, self._product.values()))

    def to_dict(self):
        return self._product


class Logger:
    @staticmethod
    def log_action(user, action, product, filename):
        timestamp = datetime.now().isoformat()
        line = f"{timestamp};{user.id};{action};{product.id}\n"

        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)

    @staticmethod
    def read_logs(filename):
        logs = []

        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")

                if len(parts) != 4:
                    continue

                logs.append({
                    "timestamp": parts[0],
                    "user_id": int(parts[1]),
                    "action": parts[2],
                    "product_id": int(parts[3])
                })

        return logs


class Order:
    def __init__(self, id, user):
        self.id = id
        self.user = user
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_products(self, product_id):
        self.products = [p for p in self.products if p.id != product_id]

    def total_price(self):
        return sum(p.price for p in self.products)

    def __str__(self):
        names = ", ".join(p.name for p in self.products)
        return f"Order(id={self.id}, user={self.user}, products=[{names}], total={self.total_price()})"


# o = Order(1, "Talant")

# p1 = Product(1, "Apple", 10, "Food")
# p2 = Product(2, "Banana", 15, "Food")

# o.add_product(p1)
# o.add_product(p2)

# print(o)

# print(o)

### 8 ###
def most_expensive_products(self, n: int):
    return sorted(self.products, key=lambda p: p.price, reverse=True)[:n]

# p1 = Product(1, "Apple", 10, "Food")
# p2 = Product(2, "Banana", 15, "Food")
# p3 = Product(3, "Laptop", 1000, "Tech")

# o = Order(1, "Talant")

# o.add_product(p1)
# o.add_product(p2)
# o.add_product(p3)

# top = o.most_expensive_products(2)

# print([p.name for p in top])

### 9 ###
def price_stream(products):
    for p in products:
        yield p.price


### 10 ###
class OrderIterator:
    def __init__(self, orders):
        self.orders = orders
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.orders):
            raise StopIteration
        order = self.orders[self.index]
        self.index += 1
        return order


### 11 ###
import numpy as np
import pandas as pd

def ms_price(products):
    return np.array([product.price for product in products])

# products = [
#     Product(1, "Laptop", 1200000, "Electronic"),
#     Product(2, "Mobile", 2000000, "Electronic"),
# ]

# arr = ms_price(products)
# print(arr)


### 12 ###
def price_stats(prices):
    mean_prices = np.mean(prices)
    median_prices = np.median(prices)
    return mean_prices, median_prices

# product = [
#     Product(1, "Laptop", 120000, "Electronic"),
#     Product(2, "Mobile", 570, "Electronic"),
# ]
# arr = np.array([p.price for p in product])

# result = price_stats(arr)
# print(result)


### 13 ###
def n_price(prices):
    min_price = np.min(prices)
    max_price = np.max(prices)
    return (prices - min_price) / (max_price - min_price)


# arr = np.array([1200.0, 25.0, 450.0])

# result = n_price(arr)
# print(result)


### 14 ###
def category_array(products):
    return np.array([product.category for product in products])

# products = [
#     Product(1, "Laptop", 1200.0, "Electronics"),
#     Product(2, "T-Shirt", 20.0, "Clothing")
# ]

# arr = category_array(products)
# print(arr)

### 15 ###
def count_unique_categories(categories):
    return len(set(categories))

# categories = np.array(["Electronics", "Clothing", "Electronics"])

# print(count_unique_categories(categories))


### 16 ###
def max_prices(products):
    mean_product = np.mean([p.price for p in products])

    return [p for p in products if p.price > mean_product]

# products = [
#     Product(1, "Laptop", 1200.0, "Electronics"),
#     Product(2, "Mouse", 25.0, "Electronics"),
#     Product(3, "Monitor", 450.0, "Electronics")
# ]

# result = max_prices(products)

# print([p.name for p in result])

### 17 ###
def sale_price(product):
    price = np.array([p.price for p in product])
    sale_product = price * 0.9
    return sale_product

# products = [
#     Product(1, "Laptop", 2400, "Electronics"),
#     Product(2, "Mobile", 400, "Electronics"),
#     Product(3, "Ipad", 1300, "Electronics"),
# ]

# sale_produc = sale_price(products)
# print(sale_produc)
        

### 18 ###
def orders_array(orders):
    return np.array([[sum(p.price for p in order.products)] for order in orders])

# u1 = User(1, "John", "john@example.com")

# p1 = Product(1, "Laptop", 1200, "Electronics")
# p2 = Product(2, "Mouse", 25, "Electronics")

# order1 = Order(1, u1, [p1])
# order2 = Order(2, u1, [p1, p2])

# orders = [order1, order2]

# arr = orders_array(orders)
# print(arr)

### 19 ###

def mean_order_value(orders_array):
    return np.mean(orders_array)


# arr = np.array([[1200],
#                 [1225]])

# print(mean_order_value(arr))


### 20 ###
def expensive_orders_indices(arr):
    return np.where(arr > 1000)[0]

# arr = np.array([1200.0, 900.0, 1500.0])

# print(expensive_orders_indices(arr))


### 21 ###
def users_dataframe(users):
    return pd.DataFrame([
        (u._id, u._name, u._email, u._registration)
        for u in users
    ], columns=["id", "name", "email", "registration"])


# users = [
#     User(1,"John Doe","john@example.com"),
#     User(2,"Alice","alice@example.com")
# ]

# df = users_dataframe(users)
# print(df)


### 22 ###
def appdata(products):
    return pd.DataFrame([
        (p.id, p.name, p.category, p.price)
        for p in products
    ], columns =["id", "name", "category", "price"])  

# products = [Product(1,"Laptop",1200.0,"Electronics"), Product(2,"T-Shirt",20.0,"Clothing")]

# df = appdata(products)
# print(df)


### 23 ###
users_df = pd.DataFrame([
    (1, "John"),
    (2, "Alice")
], columns=["id", "name"])
orders_df = pd.DataFrame([
    (101, 1, 1200),
    (102, 2, 25)
], columns =["order_id", "user_id", "total"])

def merge_users_orders(users_df, orders_df):
    merged = pd.merge(
        orders_df,
        users_df,
        left_on="user_id",
        right_on="id"
    )

    merged = merged[["order_id", "name", "total"]]
    merged = merged.rename(columns={"name": "user_name"})

    return merged

df  = merge_users_orders(users_df, orders_df)
# print(result)

### 24 ###
def filter_orders(df, min_value):
    return df[df["total"] > min_value]

# result = filter_orders(df, 100)
# print(result)


### 25 ###
def group_orders_by_user(df):
    return df.groupby("user_name")["total"].sum().reset_index(name="total_sum")



### 26 ###
def group_mean_by_user(df):
    return df.groupby("user_name")["total"].mean().sum().reset_index(name="total_sum")

### 27 ###
def count_orders_per_user(df):
    return df.groupby("user_name")["order_id"].count().reset_index(name="orders_count")

### 28 ###
def mean_price_by_category(df):
    return df.groupby("category")["price"].mean().reset_index(name="mean_price")

### 29 ###
def add_discount(df):
    df["discounted_price"] = df["price"] * 0.9
    return df

### 30 ###
df = pd.DataFrame([
    (1, "Laptop", 1200, "Electronics"),
    (2, "Mouse", 25, "Clothing"),
    (3, "Monitor", 450, "Electronics")
], columns=["id", "name", "price", "category"])

def sort_product(df):
    return df.sort_values(by="price",ascending =False)

# result = sort_product(df)
# print(result)


### 31 ###
def add_quantity(df):
    df["quantity"] = 1
    return df


# df = add_total_price(df)
# print(df)


### 32 ###
def total_price(df):
    df["total_price"] = df["price"] * df["quantity"]
    return df

# df = add_quantity(df)
# df = total_price(df)

# print(df)


### 33 ###
def filter_category(df):
    return df[df["category"] == "Electronics"]


# print(df)

### 34 ###
def count_category(df):
    return df.groupby("category")["name"].count().reset_index(name="count")
    



# df = count_category(df)
# print(df)

### 35 ###
def mean_price_each(df):
    return df.groupby("category")["price"].mean().reset_index(name="mean_price")

# df = mean_price_each(df)
# print(df)

### 36 ###
def sorted_product(df):
    return df.groupby("category")["price"].sum().sort_values(ascending=False)

# df = sorted_product(df)
# print(df)

### 37 ###
def top_n(df):
    return df.sort_values(by=["category", "price"], ascending=[True, False])

# df = top_n(df)
# print(df)



### 38 ###
# users_df = pd.DataFrame([
#     (1, "John"),
#     (2, "Alice")
# ], columns = ["user_id", "user_name"])


# order_df = pd.DataFrame([
#     (101, 1, 1200),
#     (102, 2, 50)
# ], columns = ["order_id", "user_id", "total_price"])

def merge_df(users_df, order_df):
    return pd.merge(users_df, order_df, on="user_id")

# df = merge_df(users_df, order_df)
# print(df)

### 39 ###
user_df = pd.DataFrame([
    ("John", 1200),
    ("John", 500),
    ("Alice", 50)
], columns = ["user_name", "total_price"])

def mean_user(user_df):
    return user_df.groupby("user_name")["total_price"].mean()

# print(mean_user(user_df))


### 40 ###
def count_buy(df):
    return df.groupby("name").size().reset_index(name="ordes_count")

print(count_buy(df))


### 41 ###
def max_order(df):
    return df.groupby("name")["price"].max().reset_index(name="max_order")

print(max_order(df))


### 42 ###

def unique_order(df):
    return df.groupby("name")["category"].nunique().reset_index(name="unique_category")

print(unique_order(df))

### 43 ###
def degree_user(df):
    df["VIP"] = df["price"] > 1000
    return df

# print(degree_user(df))

### 44 ###
def sort_users(df):
    return df.sort_values(
        by=["price"],
        ascending=[False]
    )
# print(sort_users(df))

### 45 ###


df = pd.DataFrame([
    ("John", 101, 1200, "Electronics"),
    ("John", 103, 500, "Clothing"),
    ("Alice", 102, 25, "Clothing")
], columns=["user_name", "order_id", "total_price", "category"])


def final_report(df):
    report = df.groupby("user_name").agg(
        total_orders=("order_id", "count"),
        total_sum=("total_price", "sum"),
        mean_total=("total_price", "mean"),
        max_order=("total_price", "max"),
        unique_categories=("category", "nunique")
    ).reset_index()

    report["VIP"] = report["total_sum"] > 1000
    return report


print(final_report(df))

