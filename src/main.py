import csv
with open("data/sample.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)
    # print(data[:5])
    # print(reader.fieldnames)
    EXPECTED = {"Date", "Description", "Amount", "Type", "Balance"}

    if set(reader.fieldnames) != EXPECTED:
        raise ValueError("Unexpected CSV schema")

    unique_values = set(row["Description"] for row in data)
    print(unique_values)

    def clean_and_validate(row):
        cleaned = {}
        for key, value in row.items():
            if value in ("None", None, ""):
                return None
            cleaned[key] = value
        try:
            cleaned["Amount"] = float(cleaned["Amount"])
            cleaned["Balance"] = float(cleaned["Balance"])
        except ValueError:
            return None
        return cleaned
    
    new_data = [r for row in data if (r := clean_and_validate(row))]

    categories = {
        'Income': ['Salary Deposit', 'freelance payment', 'refund'],
        'Food & Drinks': ['Starbucks', 'Pizza Hut', 'Subway', 'Restaurant XYZ', 'Local Cafe', 'Coffee Shop', "McDonald's", "Grocery Store"],
        'Shopping': ["Walmart", "Target", "Clothing Store", "Amazon", "Best Buy", "Game Store"],
        'Transport': ["Uber", "Gas Station", "Parking Garage", "Metro Card"],
        'Utilities': ["Internet Provider", "Phone Bill", "Electric Company", "Water Company"],
        'Health & Wellness': ["Doctor Visit", "Gym Membership", "Pharmacy"],
        'Entertainment': ["Netflix", "Spotify", "Cinema"]
    }
    def categorize(description):
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword.lower() in description.lower():
                    return category
        return "Other"

    for row in new_data:
        row['Category'] = categorize(row['Description'])
with open("data/transactions_categorized.csv", "w", newline='', encoding='utf-8') as csvfile:
    fieldnames = ["Date", "Description", "Amount", "Type", "Balance", "Category"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(new_data)