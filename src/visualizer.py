import matplotlib.pyplot as plt

def bar_chart(categories, values):
    plt.bar(categories, values)
    plt.xlabel("Category")
    plt.ylabel("Amount (EGP)")
    plt.title("Expenses")
    plt.show()

def line_chart(categories, values):
    plt.plot(categories, values)
    plt.xlabel("Category")
    plt.ylabel("Amount (EGP)")
    plt.title("Expenses")
    plt.show()