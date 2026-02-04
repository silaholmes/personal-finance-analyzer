import calendar

def months(transactions):
    months_number = set(row["Date"][5:7] for row in transactions)
    return months_number

def category_month(transaction, month):
    return set(row["Category"] for row in transaction if int(row["Date"][5:7]) == month and row["Category"] != "income")

def data_per_month(transaction, month):
    return [row for row in transaction if int(row["Date"][5:7]) == month]

def category_total(transactions, category):
    total = 0
    for row in transactions:
        if row["Category"] == category:
            total += row["Amount"]
    return total

def income_per_month(transactions):
    total_income = sum(row["Amount"] for row in transactions if row["Category"] == "income")
    return total_income

def csv_report(transaction, months):
    report_dict = []
    for month in months:
        month = int(month)
        categories = category_month(transaction, month)
        data = data_per_month(transaction, month)
        income = income_per_month(data)
        for category in categories:
            total = category_total(data, category)
            report_dict.append({"Month" : calendar.month_name[int(month)],
                                 "Category" : category, "Total" : abs(total), "Monthly_Income" : income})
    return report_dict
