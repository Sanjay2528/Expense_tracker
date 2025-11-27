# Problem Statement

Managing daily expenses is a common challenge, especially for students and working professionals who often have limited income and many small, frequent transactions. Without a clear system, people tend to lose track of where their money is going, which categories consume most of their budget, and whether they are staying within a safe spending limit.

Most simple tools or manual methods only show a total amount spent. They do not highlight which category is draining money, whether spending is crossing a planned budget, or how much is actually being saved at the end of the month. As a result, users struggle to control overspending and build healthy financial habits.

The goal of this project is to provide a lightweight, console-based application that helps users record their expenses, see category-wise spending, compare total expenses with income, and receive basic alerts when they approach or exceed a monthly budget.

---

# Scope of the Project

The Smart Expense Tracker project focuses on personal expense management in a simple, text-based environment suitable for beginners in programming. The scope includes:

- Recording individual expense entries with amount, category, and optional note.
- Summarizing total expenses and category-wise spending in the current session.
- Allowing the user to set and view a monthly budget and receive warnings when spending crosses certain thresholds.
- Accepting monthly income and calculating savings (income minus total expenses).
- Providing small, human-readable insights, such as which category has the highest spending.

The project intentionally does **not** include advanced features like online sync, authentication, complex databases, or graphical interfaces. Instead, it concentrates on applying core programming concepts such as functions, loops, conditionals, lists, dictionaries, and basic validation to solve a realistic everyday problem.

---

# Target Users

The primary target users are:

- **Students** who want to monitor their pocket money usage and avoid end-of-month cash shortages.
- **Early-stage professionals** who are learning to manage their salary and control unnecessary spending.
- **Beginner programmers** looking for a practical example of applying fundamental programming concepts to a real-world use case.
- Anyone who prefers a simple, offline, and distraction-free tool to quickly log and review expenses.

Because the application is console-based and uses only standard Python, it can be run easily on lab machines or home computers without extra setup.

---

# High-Level Features

At a high level, the Smart Expense Tracker provides the following features:

1. **Expense Entry**
   - Add a new expense with:
     - Amount (must be positive and numeric)
     - Category (for example: Food, Travel, Shopping, Bills, Others)
     - Optional short note or description

2. **View All Expenses**
   - Display all recorded expenses in the current session as a numbered list.
   - Show amount, category, and note for each entry for easier review.

3. **Total Expense Calculation**
   - Compute and display the total amount spent based on all recorded expenses.

4. **Category-wise Summary and Insight**
   - Calculate how much has been spent in each category.
   - Identify and display the highest spending category to highlight where most money is going.

5. **Monthly Budget Management**
   - Allow the user to set or update a monthly budget value.
   - Show the current budget if already set.
   - When adding expenses, automatically check the cumulative total against the budget:
     - Display an alert when spending exceeds 80% of the budget.
     - Display a warning when the budget is fully exceeded.

6. **Income and Savings View**
   - Accept the user’s monthly income.
   - Calculate savings as `income − total_expenses`.
   - Provide a simple interpretation:
     - Saving money (positive savings)
     - Breaking even (zero savings)
     - Overspending (negative savings)

7. **Menu-Driven Console Interface**
   - Present a clear, numbered menu for all main operations:
     - Add Expense
     - View All Expenses
     - Total Expenses
     - Category Summary
     - Set / View Monthly Budget
     - Enter Income & View Savings
     - Exit
   - Validate menu choices and handle invalid input gracefully.

These high-level features together make the project more than just a basic total calculator. They turn it into a small personal finance assistant that helps users understand their spending habits, stay closer to their budget, and become more aware of their savings.
