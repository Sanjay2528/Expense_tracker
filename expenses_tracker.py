expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/Bills/Others): ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    for i in expenses:
        print(f"Amount: {i['amount']} | Category: {i['category']}")
    print()

def total_expenses():
    total = sum(i['amount'] for i in expenses)
    print(f"Total Expenses: {total}\n")

def category_summary():
    summary = {}
    for i in expenses:
        cat = i['category']
        summary[cat] = summary.get(cat, 0) + i['amount']
    print("Category-wise Summary:")
    for cat, amt in summary.items():
        print(f"{cat}: {amt}")
    print()

while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total_expenses()
    elif choice == 4:
        category_summary()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")