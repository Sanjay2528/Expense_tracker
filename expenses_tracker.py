expenses = []
monthly_budget = None
monthly_income = None

def add_expense():
    print("\n--- Add Expense ---")
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.\n")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.\n")
        return

    category = input("Enter category (Food/Travel/Shopping/Bills/Others): ").strip()
    if not category:
        print("Category cannot be empty.\n")
        return

    note = input("Short note/description (optional): ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }
    expenses.append(expense)
    print("Expense added successfully!")

    # If budget is set, warn when crossing thresholds
    if monthly_budget is not None:
        total = sum(i["amount"] for i in expenses)
        if total > monthly_budget:
            print("Warning: You have exceeded your monthly budget!")
        elif total > 0.8 * monthly_budget:
            print("Alert: You have used more than 80% of your monthly budget.")
    print()

def view_expenses():
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded.\n")
        return
    for idx, i in enumerate(expenses, start=1):
        note_text = f" | Note: {i['note']}" if i["note"] else ""
        print(f"{idx}. Amount: {i['amount']} | Category: {i['category']}{note_text}")
    print()

def total_expenses():
    print("\n--- Total Expenses ---")
    total = sum(i['amount'] for i in expenses)
    print(f"Total Expenses: {total}")
    print()

def category_summary():
    print("\n--- Category-wise Summary ---")
    if not expenses:
        print("No expenses recorded.\n")
        return

    summary = {}
    for i in expenses:
        cat = i['category']
        summary[cat] = summary.get(cat, 0) + i['amount']

    for cat, amt in summary.items():
        print(f"{cat}: {amt}")

    # Highest spending category insight
    top_cat = max(summary, key=summary.get)
    print(f"\nYou are spending the most on: {top_cat} ({summary[top_cat]})\n")

def set_budget():
    global monthly_budget
    print("\n--- Set / View Monthly Budget ---")
    if monthly_budget is not None:
        print(f"Current monthly budget: {monthly_budget}")
    try:
        choice = input("Do you want to update the budget? (y/n): ").strip().lower()
        if choice == "y":
            value = float(input("Enter new monthly budget amount: "))
            if value <= 0:
                print("Budget must be positive.\n")
                return
            monthly_budget = value
            print(f"Monthly budget set to: {monthly_budget}\n")
        else:
            print("Budget unchanged.\n")
    except ValueError:
        print("Invalid value.\n")

def set_income_and_savings():
    global monthly_income
    print("\n--- Income & Savings ---")
    try:
        monthly_income = float(input("Enter this month's income: "))
        if monthly_income <= 0:
            print("Income must be positive.\n")
            return
    except ValueError:
        print("Invalid income value.\n")
        return

    total = sum(i['amount'] for i in expenses)
    savings = monthly_income - total
    print(f"Total Expenses: {total}")
    print(f"Savings: {savings}")
    if savings > 0:
        print("Good job! You are saving money this month.")
    elif savings == 0:
        print("You are breaking even this month.")
    else:
        print("You are overspending this month. Try to cut down expenses.")
    print()

while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Set / View Monthly Budget")
    print("6. Enter Income & View Savings")
    print("7. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number.\n")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total_expenses()
    elif choice == 4:
        category_summary()
    elif choice == 5:
        set_budget()
    elif choice == 6:
        set_income_and_savings()
    elif choice == 7:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")
