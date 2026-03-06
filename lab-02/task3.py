import json
from collections import Counter

<<<<<<< HEAD:lab-02/task3.py
data =   [{
=======
data =   {
>>>>>>> 7edac72064c3432bdc85a9e7ddba2e345e1a2982:task3.py
    "order_id": 1,
    "user": "Ali",
    "items": ["phone", "case"],
    "total": 300000
  },{
    "order_id": 2,
    "user": "Dana",
    "items": ["laptop"],
    "total": 800000
  }, {
    "order_id": 3,
    "user": "Ali",
    "items": ["mouse", "keyboard"],
    "total": 70000
<<<<<<< HEAD:lab-02/task3.py
  }]
=======
  }
>>>>>>> 7edac72064c3432bdc85a9e7ddba2e345e1a2982:task3.py


with open("orders.json", "w") as file:
    json.dump(data, file, indent=4)

with open("orders.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

<<<<<<< HEAD:lab-02/task3.py
total_sum = 0
buy_item_each_person = {}
bought_item = []
top_expensive_sum = 0
top_user_buy = ""


with open("orders.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    for order in data:
        total_sum += order["total"]

        user_id = order["user"]
        if user_id not in buy_item_each_person:
            buy_item_each_person[user_id] = 0
        buy_item_each_person[user_id] += 1

        bought_item.extend(order["items"])

        
        if order["total"] > top_expensive_sum:
            top_expensive_sum = order["total"]
            top_user_buy = user_id
        
most_popular_item = Counter(bought_item).most_common(1)[0][0]

summary = {
    "total_revenue": total_sum,
    "top_user": top_user_buy,
=======
print("Файл orders.json успешно создан!")
total_revenue = 0
user_orders_count = {}
all_items = []
max_order_value = 0
top_user_by_order = ""


for order in data:
    
    total_revenue += order["total"]
    
    
    user = order["user"]
    user_orders_count[user] = user_orders_count.get(user, 0) + 1
    
    
    all_items.extend(order["items"])
    
    
    if order["total"] > max_order_value:
        max_order_value = order["total"]
        top_user_by_order = user
item_counts = Counter(all_items)
most_popular_item = item_counts.most_common(1)[0][0]
summary = {
    "total_revenue": total_revenue,
    "top_user": top_user_by_order,
>>>>>>> 7edac72064c3432bdc85a9e7ddba2e345e1a2982:task3.py
    "most_popular_item": most_popular_item,
    "total_orders": len(data)
}

with open('summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print("Файл summary.json успешно создан!")
