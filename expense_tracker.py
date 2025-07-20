import os

FILENAME = "expenses.txt"

# Load expenses from file
def load_expenses():
    expenses = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    expenses.append((parts[0], float(parts[1])))
    return expenses

# Save expenses to file
def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        for item, amount in expenses:
            file.write(f"{item},{amount}\n")

# Show expenses
def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\n--- Your Expenses ---")
        total = 0
        for item, amount in expenses:
            print(f"{item}: ₹{amount:.2f}")
            total += amount
        print(f"\nTotal: ₹{total:.2f}")

# Main program
def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save & Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            item = input("Enter item name: ")
            try:
                amount = float(input("Enter amount (in ₹): "))
                expenses.append((item, amount))
                print("Expense added.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            save_expenses(expenses)
            print("Expenses saved. Exiting...")
            break
        else:
            print("Invalid option. Try again.")

main()
