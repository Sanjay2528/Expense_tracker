# Smart Expense Tracker (CLI)

## Project Title
Smart Expense Tracker – Budget, Savings, and Spending Insights

## Overview of the Project

Smart Expense Tracker is a Python console application that helps users record daily expenses, see where their money is going, and understand whether they are staying within a monthly budget. It goes beyond a simple total-expense calculator by providing category-wise summaries, highest-spending category insight, and a basic savings view based on monthly income.

This project is designed for an Introduction to Problem Solving & Programming course and showcases modular programming, data structures (lists and dictionaries), loops, conditionals, and simple input validation.

## Features

- Add new expenses with amount, category, and an optional note.
- View all recorded expenses in a clean, numbered list.
- Calculate total expenses across all entries.
- Category-wise summary showing how much was spent in each category.
- Highlight of the highest spending category (“You are spending the most on …”).
- Set and view a monthly budget with automatic alerts:
  - Warning when spending crosses 80% of budget.
  - Warning when spending exceeds the budget.
- Enter monthly income and view savings (income − total expenses) with simple feedback messages.
- Menu-driven interface with basic validation for safer input.

## Technologies / Tools Used

- **Language:** Python 3.x  
- **Environment:** Any Python-capable IDE or terminal (VS Code, PyCharm, IDLE, command prompt/terminal)  
- **Data Handling:** In-memory lists and dictionaries (no external database)  

## Steps to Install & Run the Project

1. **Install Python 3**  
   - Download from the official Python website and complete installation.  
   - Confirm installation in terminal/command prompt:
     ```
     python --version
     ```
     or
     ```
     python3 --version
     ```

2. **Clone or download this repository**
  https://github.com/Sanjay2528/Expense_tracker.git 
3. **Run the program**


4. **Use the menu**
- Choose from options like:
  - Add Expense  
  - View All Expenses  
  - Total Expenses  
  - Category Summary  
  - Set / View Monthly Budget  
  - Enter Income & View Savings  
  - Exit  

## Instructions for Testing

Try the following scenarios to test all features:

- **Test 1: Basic expense entry**
- Add 3–4 expenses in different categories (Food, Travel, Bills, Others).
- View all expenses and check that each entry is listed with amount, category, and note.

- **Test 2: Total expenses**
- After adding several expenses, choose “Total Expenses”.
- Manually add the values and confirm the total printed by the program is correct.

- **Test 3: Category summary + top category**
- Add multiple expenses in at least two categories.
- Use “Category Summary” and confirm:
 - Each category total is correct.
 - The “You are spending the most on …” line points to the correct category.

- **Test 4: Budget and alerts**
- Set a monthly budget (for example, 1000).
- Add expenses so that:
 - Total crosses 800 but stays below 1000 – expect 80% warning.
 - Total crosses 1000 – expect “exceeded budget” warning.

- **Test 5: Income and savings**
- Enter a monthly income (for example, 5000).
- Check different cases:
 - Total expenses < income → positive savings message.
 - Total expenses = income → break-even message.
 - Total expenses > income → overspending message.

- **Test 6: Invalid input handling**
- Try entering non-numeric amount, negative amount, or blank category.
- Program should show an error and not crash.
