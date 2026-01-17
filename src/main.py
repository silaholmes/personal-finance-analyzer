"""
Personal Finance Analyzer
Author: [Alaa Ayesh]
Date: January 2, 2026
"""

import csv
with open("data/sample.csv", newline='') as csvfile:
    data = list(csv.reader(csvfile))
    for row in data:
        print(', '.join(row))
