# Expense Tracker 💰

A simple command-line expense tracking application built with Python.

The program allows users to add, view, search, edit, and delete expenses. It also calculates the total amount of all recorded expenses and saves the data to a JSON file.

## Features

* ➕ Add expenses
* 📋 View all expenses
* 🔍 Search for expenses by name
* ✏️ Edit existing expenses
* 🗑️ Delete expenses
* 💰 Calculate total expenses
* 💾 Automatically save expenses to a JSON file
* 📂 Load saved expenses when the program starts
* 🛡️ Handle invalid user input
* ❌ Handle invalid or corrupted JSON data
* 🚫 Prevent negative expense amounts

## Technologies Used

* Python
* JSON
* `json` module

## Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
├── expenses.json
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Expense-Tracker
```

### 3. Run the program

```bash
python expense_tracker.py
```

The `expenses.json` file will be created automatically if it does not already exist.

## Menu

When the program starts, you will see:

```text
==============================
       EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Search Expense
4. Delete Expense
5. Show Total Expenses
6. Edit Expense
7. Exit
```

## How It Works

### Add Expense

The program asks for:

* Expense name
* Amount
* Category

The expense is then stored in the program and saved to `expenses.json`.

### View Expenses

Displays all recorded expenses with their name, amount, and category.

Example:

```text
Expenses:
1. Food - $15.50 (Food)
2. Bus - $3.00 (Transport)
```

### Search Expense

Allows the user to search for an expense by entering part or all of its name.

### Delete Expense

Allows the user to select an expense by its number and remove it from the list.

### Show Total Expenses

Calculates and displays the total amount of all recorded expenses.

Example:

```text
Total Expenses: $18.50
```

### Edit Expense

Allows the user to change the name, amount, or category of an existing expense.

Leaving a field blank keeps its current value.

### Exit

Before exiting, the program saves the current expenses to `expenses.json`.

## Data Storage

Expenses are stored in a JSON file.

Example:

```json
[
    {
        "name": "Food",
        "amount": 15.5,
        "category": "Food"
    },
    {
        "name": "Bus",
        "amount": 3.0,
        "category": "Transport"
    }
]
```

## Error Handling

The program handles common input problems, including:

* Invalid numbers
* Negative expense amounts
* Invalid expense numbers
* Missing `expenses.json`
* Invalid or corrupted JSON data

## What I Learned

Through this project, I practiced:

* Python functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* User input
* File handling
* JSON data
* `try` and `except`
* List comprehensions
* `sum()`
* String formatting
* Building a menu-driven application

## Future Improvements

Possible improvements for future versions:

* Add expenses by date
* Add monthly expense reports
* Add expense categories summary
* Add a budget system
* Export expenses to CSV
* Add a graphical user interface

## Author

**Yazan**

This project was created as part of my journey to improve my Python programming skills through practical projects.
