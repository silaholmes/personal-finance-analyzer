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
    yearly_income = {}
    yearly_expenses = {}

    for row in transactions:
        year = row["Date"][:4]

        if row["Amount"] > 0:
            yearly_income[year] = yearly_income.get(year, 0) + row["Amount"]
        else:
            yearly_expenses[year] = yearly_expenses.get(year, 0) + abs(row["Amount"])

    years = sorted(set(yearly_income) | set(yearly_expenses))
    return years, yearly_income, yearly_expenses


def count_category(transactions):
    dic = {}
    for row in transactions:
        dic[row["Category"]] = dic.get(row["Category"], 0) + 1
    return dic

def expense_by_category(transactions):
    categories = []
    values = []
    for key, value in transactions.items():
        if key == "income":
            continue
        categories.append(key)
        values.append(abs(value))
    return categories, values