import csv
import re
import logging
from analyzer import category_totals, analyze_income_expenses, yearly_summary, count_category, expense_by_category
from categorizer import categorize
from visualizer import bar_chart, line_chart
from report import csv_report, months

logging.basicConfig(
    filename="app.log",
    level = logging.DEBUG,
    format="%(asctime)s %(levelname)s:%(message)s"
)
with open("data/sample.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

    EXPECTED = {"Date", "Description", "Amount", "Type", "Balance"}

    if set(reader.fieldnames) != EXPECTED:
        logging.error("Unexpected CSV schema")  
        raise ValueError("Unexpected CSV schema")
    
    logging.info(f"Loaded {len(data)} rows from CSV")

    unique_values = set(row["Description"] for row in data)
    print(unique_values)

    def clean_and_validate(row):
        cleaned = {}
        for key, value in row.items():
            if value in ("None", None, ""):
                return None
            if key in ("Description", "Type"):
                value = value.strip().lower()
                value = re.sub(r'[^a-z0-9\s&]', '', value)
            cleaned[key] = value

        try:
            cleaned["Amount"] = float(cleaned["Amount"])
            cleaned["Balance"] = float(cleaned["Balance"])
        except ValueError:
            return None
        return cleaned
    
    new_data = [r for row in data if (r := clean_and_validate(row))]
    logging.info(f"Validated and cleaned data. {len(new_data)} rows remain after cleaning.")

    for row in new_data:
        row['Category'] = categorize(row['Description'])
    logging.info("Categorized transactions.")
with open("data/transactions_categorized.csv", "w", newline='', encoding='utf-8') as csvfile:
    fieldnames = ["Date", "Description", "Amount", "Type", "Balance", "Category"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(new_data)

totals = category_totals(new_data)
income, expenses = analyze_income_expenses(new_data)
years, yearly_income, yearly_expenses = yearly_summary(new_data)

for key, value in totals.items():
    if key == "income":
        continue
    print(f"{key}: {abs(value):.2f}")
print(f"Total Income: {income:.2f} \nTotal Expenses: {expenses:.2f}")
for year in years:
    print(f"Year {year} - Income: {yearly_income[year]:.2f}, Expenses: {yearly_expenses[year]:.2f}")

for category, count in count_category(new_data).items():
    print(f"count of {category}: {count}")
categories, values =expense_by_category(totals)

bar_chart(categories,values)
line_chart(categories, values)

month = months(new_data)
report = csv_report(new_data, month)

with open("data/report.csv", "w", newline='', encoding='utf-8') as csvfile:
    fieldnames = ["Month", "Category", "Total", "Monthly_Income"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(report)
