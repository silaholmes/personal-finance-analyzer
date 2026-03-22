categories = {
        'income': ['salary deposit', 'freelance payment', 'refund'],
        'food & drinks': ['starbucks', 'pizza hut', 'subway', 'restaurant xyz', 'local cafe', 'coffee shop', "mcdonald's", "grocery store"],
        'shopping': ["walmart", "target", "clothing store", "amazon", "best buy", "game store"],
        'transport': ["uber", "gas station", "parking garage", "metro card"],
        'utilities': ["internet provider", "phone bill", "electric company", "water company"],
        'health & wellness': ["doctor visit", "gym membership", "pharmacy"],
        'entertainment': ["netflix", "spotify", "cinema"]
    }
def categorize(description):
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in description:
                return category
    return "Other"

print("hello")
