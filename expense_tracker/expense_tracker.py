import csv
import json
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.csv"

def load_expenses():
    """Load expenses from the CSV file."""
    expenses = []
    try:
        with open(EXPENSE_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    """Save expenses to the CSV file."""
    with open(EXPENSE_FILE, mode="w", newline="") as file:
        fieldnames = ["amount", "category", "date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(amount, category):
    """Add a new expense."""
    expenses = load_expenses()
    expense = {
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(category=None):
    """View all expenses or filter by category."""
    expenses = load_expenses()
    if category:
        expenses = [expense for expense in expenses if expense["category"] == category]
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")

def expense_summary():
    """Show a summary of expenses by category."""
    expenses = load_expenses()
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

def main():
    """Main function to run the expense tracker."""
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            add_expense(amount, category)
        elif choice == "2":
            category = input("Enter category to filter (or leave blank for all): ")
            view_expenses(category)
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
