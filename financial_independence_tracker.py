rent = float(input("Enter your monthly rent: $"))
phone = float(input("Enter the cost of your phone bill: $"))
groceries = float(input("Enter how mucb you spend on groceries monthly: $"))
transportation =  float(input("Enter how much you spend on transportation monthly: $"))

bi_weekly_income = float(input("Enter your bi-weekly income: $"))
monthly_income = bi_weekly_income * 26/12
monthly_expenses = rent + phone + groceries + transportation
monthly_gap = monthly_expenses - monthly_income

print(f"Monthly expenses: ${monthly_expenses:.2f}")
print(f"Average monthly income: ${monthly_income:.2f}")
print(f"Monthly income gap: ${monthly_gap:.2f}")

