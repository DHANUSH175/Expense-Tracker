# Expense Tracker (Command-Line Version)
import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Initialize CSV file if not exists
def init_file():
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
    except FileExistsError:
        pass

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    amount = input("Enter amount: ")
    category = input("Enter category (Food, Travel, etc.): ")
    description = input("Enter description: ")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!\n")

def view_expenses():
    print("\n--- All Expenses ---")
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))
    print()

def category_summary():
    from collections import defaultdict
    summary = defaultdict(float)
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            summary[row['Category']] += float(row['Amount'])

    print("\n--- Category-wise Summary ---")
    for cat, total in summary.items():
        print(f"{cat}: ₹{total:.2f}")
    print()

def main():
    init_file()
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category-wise Summary")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
