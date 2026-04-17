
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Сервер работает"}

#uvicorn practise:app --reload

# class Mage(Player):
#     def event(self, event):
#         if event.type == "LOOK":
#             item = item.data["Item"]
#             item.damage *= 1.1
#             return f"(Mage damage = {item.damage})"

import pandas as pd

df = pd.DataFrame([
    ("John", 1200),
    ("John", 500),
    ("Alice", 25)
], columns=["user", "total"])

print(df.groupby("user")["total"].sum())
            