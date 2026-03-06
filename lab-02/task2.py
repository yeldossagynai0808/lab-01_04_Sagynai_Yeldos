import csv
with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","department","salary"])
    writer.writerow(["Ali","IT",500000])
    writer.writerow(["Dana","HR",300000])
    writer.writerow(["Arman","IT",400000])
    writer.writerow(["Aruzhan","Marketing",400000])
    writer.writerow(["Dias","IT",450000])

employees = []
department_salaries = {}

with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["salary"] = int(row["salary"])
        employees.append(row)

        dept = row["department"]
        if dept not in department_salaries:
            department_salaries[dept] = []
            
        department_salaries[dept].append(row["salary"])

average_salary = sum(emp["salary"] for emp in employees) / len(employees)
print("Средняя зарплата:", average_salary)

average_salary_department = {}

for dept, salaries in department_salaries.items():
    avg = sum(salaries ) / len(salaries)
    average_salary_department[dept] = avg
    print(f"Средняя зарплата отдела{dept}: {avg}")
max_dept = max(average_salary_department, key=average_salary_department.get)
print("Отдел с самой высокой средней зарплатой:",max_dept)

highest_paid = max(employees, key=lambda x: x["salary"])
print("Самый выскооплачииваемый сотрудник:", highest_paid["name"], highest_paid["salary"])

high_salary_employees = []
for emp in employees:
    if emp["salary"] > average_salary:
        high_salary_employees.append(emp)

print("Сотрудники с зарплатой выше средней:")
for emp in high_salary_employees:
    print(emp["name"], emp["salary"])

with open("high _salary.csv","w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name","department", "salary"])
    writer.writeheader()
    writer.writerows(high_salary_employees)