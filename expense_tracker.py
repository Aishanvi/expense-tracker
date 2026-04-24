def load_data():
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category = line.strip().split(",")
                expenses.append((float(amount), category))
    except FileNotFoundError:
        pass
    return expenses
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expenses.append((amount, category))

    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{category}\n")

    print("Expense added!")
def view_expense(expenses):
    if not expenses:
        print("No expenses yet!")
    else:
        total = 0
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. Amount: {exp[0]}, Category: {exp[1]}")
            total += exp[0]

        print(f"\nTotal Expense: {round(total, 2)}")
expenses = load_data()
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expense(expenses)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
        