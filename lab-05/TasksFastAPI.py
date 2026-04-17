from datetime import datetime
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, EmailStr

import numpy as np
import pandas as pd
from fastapi import FastAPI


app = FastAPI(title="Tasks 1-45 API")

# =========================================================
# 1-10 
# =========================================================

class User:
    def __init__(self, id: int, name: str, email: str):
        self._id = id
        self._name = name.strip().title()
        if "@" not in email or "." not in email:
            raise ValueError("Неверный email")
        self._email = email.strip().lower()
        self._registration_date = datetime.now().date()

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def registration_date(self):
        return self._registration_date

    def __str__(self) -> str:
        return (
            f"User(id={self._id}, name='{self._name}', "
            f"email='{self._email}', registration_date='{self._registration_date}')"
        )

    @classmethod
    def from_string(cls, data: str) -> "User":
        parts = data.split(",")
        if len(parts) != 3:
            raise ValueError("Формат должен быть: id,name,email")
        id_str, name, email = parts
        return cls(int(id_str.strip()), name.strip(), email.strip())


class Product:
    def __init__(self, id: int, name: str, price: float, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self) -> str:
        return (
            f"Product(id={self.id}, name='{self.name}', "
            f"price={self.price}, category='{self.category}')"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Product) and self.id == other.id

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
        }


class Inventory:
    def __init__(self):
        self._products: Dict[int, Product] = {}

    def add_product(self, product: Product) -> None:
        self._products[product.id] = product

    def remove_product(self, product_id: int) -> None:
        if product_id in self._products:
            del self._products[product_id]

    def get_product(self, product_id: int) -> Optional[Product]:
        return self._products.get(product_id)

    def get_all_products(self) -> List[Product]:
        return list(self._products.values())

    def unique_products(self) -> set[Product]:
        return set(self._products.values())

    def filter_by_price(self, min_price: float) -> List[Product]:
        return [p for p in self._products.values() if p.price >= min_price]

    def to_dict(self) -> Dict[int, Product]:
        return self._products


class Logger:
    @staticmethod
    def log_action(user: User, action: str, product: Product, filename: str) -> None:
        timestamp = datetime.now().isoformat()
        line = f"{timestamp};{user.id};{action};{product.id}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)

    @staticmethod
    def read_logs(filename: str) -> List[Dict[str, Any]]:
        logs: List[Dict[str, Any]] = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                if len(parts) != 4:
                    continue
                logs.append({
                    "timestamp": parts[0],
                    "user_id": int(parts[1]),
                    "action": parts[2],
                    "product_id": int(parts[3]),
                })
        return logs


class Order:
    def __init__(self, id: int, user: User):
        self.id = id
        self.user = user
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product_id: int) -> None:
        self.products = [p for p in self.products if p.id != product_id]

    def total_price(self) -> float:
        return sum(p.price for p in self.products)

    def most_expensive_products(self, n: int) -> List[Product]:
        return sorted(self.products, key=lambda p: p.price, reverse=True)[:n]

    def __str__(self) -> str:
        product_names = ", ".join(p.name for p in self.products)
        return (
            f"Order(id={self.id}, user='{self.user.name}', "
            f"products=[{product_names}], total={self.total_price()})"
        )


def price_stream(products: List[Product]):
    for p in products:
        yield p.price


class OrderIterator:
    def __init__(self, orders: List[Order]):
        self.orders = orders
        self.index = 0

    def __iter__(self) -> "OrderIterator":
        return self

    def __next__(self) -> Order:
        if self.index >= len(self.orders):
            raise StopIteration
        order = self.orders[self.index]
        self.index += 1
        return order


# =========================================================
# 11-20 NumPy
# =========================================================

def prices_to_numpy(products: List[Product]) -> np.ndarray:
    return np.array([p.price for p in products])


def price_stats(prices: np.ndarray):
    return {
        "mean": float(np.mean(prices)),
        "median": float(np.median(prices)),
    }


def normalize_prices(prices: np.ndarray) -> np.ndarray:
    min_price = np.min(prices)
    max_price = np.max(prices)
    if max_price == min_price:
        return np.zeros_like(prices, dtype=float)
    return (prices - min_price) / (max_price - min_price)


def category_array(products: List[Product]) -> np.ndarray:
    return np.array([p.category for p in products])


def count_unique_categories(categories: np.ndarray) -> int:
    return len(np.unique(categories))


def products_above_mean(products: List[Product]) -> List[Product]:
    mean_price = np.mean([p.price for p in products])
    return [p for p in products if p.price > mean_price]


def discounted_prices(products: List[Product]) -> np.ndarray:
    return np.array([p.price * 0.9 for p in products])


def orders_array(orders: List[Order]) -> np.ndarray:
    return np.array([order.total_price() for order in orders])


def mean_order_value(arr: np.ndarray) -> float:
    return float(np.mean(arr))


def expensive_orders_indices(arr: np.ndarray) -> np.ndarray:
    return np.where(arr > 1000)[0]


# =========================================================
# 21-45 Pandas
# =========================================================

def users_dataframe(users: List[User]) -> pd.DataFrame:
    return pd.DataFrame([
        (u.id, u.name, u.email, u.registration_date)
        for u in users
    ], columns=["id", "name", "email", "registration_date"])


def products_dataframe(products: List[Product]) -> pd.DataFrame:
    return pd.DataFrame([
        (p.id, p.name, p.category, p.price)
        for p in products
    ], columns=["id", "name", "category", "price"])


def merge_users_orders(users_df: pd.DataFrame, orders_df: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(orders_df, users_df, left_on="user_id", right_on="id")
    merged = merged[["order_id", "name", "total"]]
    return merged.rename(columns={"name": "user_name"})


def filter_orders(df: pd.DataFrame, min_value: float) -> pd.DataFrame:
    return df[df["total"] > min_value]


def group_orders_by_user(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("user_name")["total"].sum().reset_index(name="total_sum")


def group_mean_by_user(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("user_name")["total"].mean().reset_index(name="mean_total")


def count_orders_per_user(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("user_name")["order_id"].count().reset_index(name="orders_count")


def mean_price_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("category")["price"].mean().reset_index(name="mean_price")


def add_discount(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["discounted_price"] = df["price"] * 0.9
    return df


def sort_products_by_price(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by="price", ascending=False)


def add_quantity(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["quantity"] = 1
    return df


def add_total_price(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["total_price"] = df["price"] * df["quantity"]
    return df


def filter_electronics(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["category"] == "Electronics"]


def count_category(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("category")["name"].count().reset_index(name="count")


def mean_price_each(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("category")["price"].mean().reset_index(name="mean_price")


def category_sum_sorted(df: pd.DataFrame) -> pd.DataFrame:
    result = df.groupby("category")["price"].sum().reset_index(name="total_price")
    return result.sort_values(by="total_price", ascending=False)


def top_n_products(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by=["category", "price"], ascending=[True, False])


def merge_df(users_df: pd.DataFrame, order_df: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(users_df, order_df, on="user_id")


def mean_user(user_df: pd.DataFrame) -> pd.DataFrame:
    return user_df.groupby("user_name")["total_price"].mean().reset_index(name="mean_total")


def count_buy(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("user_name").size().reset_index(name="orders_count")


def max_order(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("user_name")["total_price"].max().reset_index(name="max_order")


def unique_order(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("user_name")["category"].nunique().reset_index(name="unique_categories")


def degree_user(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["VIP"] = df["total_sum"] > 1000
    return df


def sort_users(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by=["total_sum", "mean_total"], ascending=[False, True])


def final_report(df: pd.DataFrame) -> pd.DataFrame:
    report = df.groupby("user_name").agg(
        total_orders=("order_id", "count"),
        total_sum=("total_price", "sum"),
        mean_total=("total_price", "mean"),
        max_order=("total_price", "max"),
        unique_categories=("category", "nunique"),
    ).reset_index()
    report["VIP"] = report["total_sum"] > 1000
    return report


# =========================================================
# Pydantic schemas
# =========================================================

class UserIn(BaseModel):
    id: int
    name: str
    email: EmailStr


class ProductIn(BaseModel):
    id: int
    name: str
    price: float
    category: str


class OrderLineIn(BaseModel):
    user_name: str
    order_id: int
    total_price: float
    category: str


class OrdersReportRequest(BaseModel):
    items: List[OrderLineIn]


# =========================================================
# Demo data
# =========================================================

sample_products = [
    Product(1, "Laptop", 1200, "Electronics"),
    Product(2, "Mouse", 25, "Clothing"),
    Product(3, "Monitor", 450, "Electronics"),
]

sample_users = [
    User(1, "John", "john@example.com"),
    User(2, "Alice", "alice@example.com"),
]

sample_report_df = pd.DataFrame([
    ("John", 101, 1200, "Electronics"),
    ("John", 103, 500, "Clothing"),
    ("Alice", 102, 25, "Clothing"),
], columns=["user_name", "order_id", "total_price", "category"])

sample_category_df = pd.DataFrame([
    (1, "Laptop", 1200, "Electronics"),
    (2, "Mouse", 25, "Clothing"),
    (3, "Monitor", 450, "Electronics"),
], columns=["id", "name", "price", "category"])


# =========================================================
# FastAPI endpoints
# =========================================================

@app.get("/")
def home():
    return {"message": "Tasks 1-45 FastAPI is running"}


@app.get("/task21/users-dataframe")
def api_users_dataframe():
    return users_dataframe(sample_users).to_dict(orient="records")


@app.get("/task22/products-dataframe")
def api_products_dataframe():
    return products_dataframe(sample_products).to_dict(orient="records")


@app.get("/task28/mean-price-by-category")
def api_mean_price_by_category():
    return mean_price_by_category(sample_category_df).to_dict(orient="records")


@app.get("/task30/sort-products")
def api_sort_products():
    return sort_products_by_price(sample_category_df).to_dict(orient="records")


@app.get("/task34/count-category")
def api_count_category():
    return count_category(sample_category_df).to_dict(orient="records")


@app.get("/task35/mean-price-each")
def api_mean_price_each():
    return mean_price_each(sample_category_df).to_dict(orient="records")


@app.get("/task39/mean-user")
def api_mean_user():
    user_df = pd.DataFrame([
        ("John", 1200),
        ("John", 500),
        ("Alice", 50),
    ], columns=["user_name", "total_price"])
    return mean_user(user_df).to_dict(orient="records")


@app.get("/task40/count-orders")
def api_count_orders():
    return count_buy(sample_report_df).to_dict(orient="records")


@app.get("/task41/max-order")
def api_max_order():
    return max_order(sample_report_df).to_dict(orient="records")


@app.get("/task42/unique-categories")
def api_unique_categories():
    return unique_order(sample_report_df).to_dict(orient="records")


@app.get("/task43/vip")
def api_vip():
    report = final_report(sample_report_df)
    return degree_user(report).to_dict(orient="records")


@app.get("/task44/sort-users")
def api_sort_users():
    report = final_report(sample_report_df)
    return sort_users(report).to_dict(orient="records")


@app.get("/task45/final-report")
def api_final_report():
    return final_report(sample_report_df).to_dict(orient="records")


@app.post("/task45/final-report")
def api_final_report_post(payload: OrdersReportRequest):
    df = pd.DataFrame([item.model_dump() for item in payload.items])
    return final_report(df).to_dict(orient="records")
