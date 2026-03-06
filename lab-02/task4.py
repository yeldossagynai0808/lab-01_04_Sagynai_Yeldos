import csv
import json

with open("transactions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["user_id", "amount"])
    writer.writerow(["user_1", 5000])
    writer.writerow(["user_2", 10000])
    writer.writerow(["user_1", 700000])
    writer.writerow(["user_3", 3000])
    writer.writerow(["user_2", 900000])
    writer.writerow(["user_4", 2000])

with open("transactions.csv", "r") as f:
    read = csv.DictReader(f)
    

    user_operations = {}
    suspicious_transactions = []
    suspicious_users = set()
    total_suspicious_amount = 0




    for row in read:
        user_id = row["user_id"]
        amount = int(row["amount"])

        if user_id not in user_operations:
            user_operations[user_id] = 0
        user_operations[user_id] += 1

        if amount > 500000:
            suspicious_transactions.append((user_id, amount))
            suspicious_users.add(user_id)
            total_suspicious_amount += amount


for user_id, count in user_operations.items():
    if count > 3:
        suspicious_users.add(user_id)

with open("fraud_report.txt", "w") as f:
        f.write(f"Подозрительных транзакций: {len(suspicious_transactions)}\n")
        f.write(f"Подозрительный пользователей: {len(suspicious_users)}\n")
        f.write("Список пользователей:" + ", ".join(suspicious_users) + "\n")
        f.write(f"Общая сумма подозрительныз операций: {total_suspicious_amount}\n")

with open("fraud_users.json","w") as f:
    json.dump(list(suspicious_users), f, indent = 4)

print('Подозрительные транзакции:', suspicious_transactions)
print("Подозрительные пользователи:", suspicious_users)
print("Общая сумма:", total_suspicious_amount)




            


