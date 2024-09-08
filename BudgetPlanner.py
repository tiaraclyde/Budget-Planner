class BudgetPlanner:
    def __init__(self):
        #define it's attributes
        self.monthly_income = 0
        self.monthly_expenses = {}
    
    def add_income(self, income):
        self.monthly_income += income

    def add_expenses(self, category, amount):
        self.monthly_expenses[category] += amount
    
    def get_total_expenses(self):

        return sum(self.monthly_expenses.values())

    def get_balance(self):

        return self.monthly_income - self.get_total_expenses()

    def get_expenses_by_category(self):

        return self.monthly_expenses

    def rest_budget(self):
        self.monthly_income = 0
        self.monthly_expenses = {}

#declaring class object
if __name__ == "__main__": () 
planner = BudgetPlanner()

    #user interaction
while True:
        print("\nPersonal Budgert Planner")
        print("1. Add Income")
        print("2. Add Expenses")
        print("3. View Total Expenses")
        print("4. View Balance")
        print("5. View Expenses by Category")
        print("6. Reset Budget")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            income = float(input("Enter Income amount: "))
            planner.add_income(income)
            print("Income added successfully.")

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            planner.add_expenses(category, amount)
            print("Expense added successfully")

        elif choice == "3":
            total_expense = planner.get_total_expenses()
            print("Total Expenses: {total_expenses}")

        elif choice == "4":
            balance = planner.get_balance()
            print("Total Balance: {balance}")

        elif choice == "5":
            expenses_by_category = planner.get_expense_by_category()
            print("Expenses by category: ")
            for category, amount in expenses_by_category.items():
                print("{category}: {amount}")

        elif choice == "6":
            planner.reset_budget()
            print("Budget has been reset.")

        elif choice == "7":
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please try again")




