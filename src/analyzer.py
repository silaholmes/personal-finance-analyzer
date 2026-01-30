def category_totals(transactions):
    totals = {}
    for row in transactions:
        category = row["Category"]
        amount = row["Amount"]
        totals[category] = totals.get(category, 0) + amount
    return totals

def analyze_income_expenses(transactions):
    total_income = sum(row["Amount"] for row in transactions if row["Category"] == "income")
    total_expenses = abs(sum(row["Amount"] for row in transactions if row["Category"] != "income"))
    return total_income, total_expenses

def yearly_summary(transactions):
    year = set(row["Date"].split("-")[0][2:4] for row in transactions)
    for y in year:
        yearly_income = sum(row["Amount"] for row in transactions if row["Category"] == "income" and row["Date"].startswith(f"20{y}"))
        yearly_expenses = abs(sum(row["Amount"] for row in transactions if row["Category"] != "income" and row["Date"].startswith(f"20{y}")))
    return year, yearly_income, yearly_expenses

def count_category(transactions):
    dic = {}
    for row in transactions:
        dic[row["Category"]] = dic.get(row["Category"], 0) + 1
    return dic
