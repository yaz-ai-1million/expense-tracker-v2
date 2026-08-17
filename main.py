import json

FILE_NAME = "expenses.json"
expenses = []


# Load Expenses
try:
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []
except json.JSONDecodeError:
    print("Warning: Could not read expenses.json. Starting with an empty list.")
    expenses = []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    name = input("Enter expense name: ")

    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")

    category = input("Enter expense category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses()

    print(f"Expense '{name}' added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nExpenses:")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['name']} - "
            f"${expense['amount']:.2f} ({expense['category']})"
        )


def search_expense():
    if not expenses:
        print("No expenses recorded.")
        return

    search_name = input("Enter expense name to search: ")

    found_expenses = [
        expense
        for expense in expenses
        if search_name.lower() in expense["name"].lower()
    ]

    if not found_expenses:
        print("No expenses found.")
        return

    print("\nSearch Results:")

    for index, expense in enumerate(found_expenses, start=1):
        print(
            f"{index}. {expense['name']} - "
            f"${expense['amount']:.2f} ({expense['category']})"
        )


def delete_expense():
    if not expenses:
        print("No expenses recorded.")
        return

    view_expenses()

    while True:
        try:
            expense_number = int(
                input("Enter expense number to delete: ")
            )

            if 1 <= expense_number <= len(expenses):
                break

            print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

    deleted_expense = expenses.pop(expense_number - 1)
    save_expenses()

    print(f"Expense '{deleted_expense['name']}' deleted successfully!")


def show_total_expenses():
    total = sum(expense["amount"] for expense in expenses)

    print(f"Total Expenses: ${total:.2f}")


def edit_expense():
    if not expenses:
        print("No expenses recorded.")
        return

    view_expenses()

    while True:
        try:
            expense_number = int(
                input("Enter expense number to edit: ")
            )

            if 1 <= expense_number <= len(expenses):
                break

            print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

    expense = expenses[expense_number - 1]

    print(
        f"\nEditing Expense: {expense['name']} - "
        f"${expense['amount']:.2f} ({expense['category']})"
    )

    new_name = input(
        "Enter new name (leave blank to keep current): "
    )

    new_amount = input(
        "Enter new amount (leave blank to keep current): "
    )

    new_category = input(
        "Enter new category (leave blank to keep current): "
    )

    if new_name:
        expense["name"] = new_name

    if new_amount:
        try:
            new_amount = float(new_amount)

            if new_amount < 0:
                print("Amount cannot be negative.")
                return

            expense["amount"] = new_amount

        except ValueError:
            print("Invalid amount. The old amount was kept.")

    if new_category:
        expense["category"] = new_category

    save_expenses()

    print("Expense updated successfully!")


def main():
    while True:
        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Show Total Expenses")
        print("6. Edit Expense")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            show_total_expenses()

        elif choice == "6":
            edit_expense()

        elif choice == "7":
            save_expenses()
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()