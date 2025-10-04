# @ disha raghav
#@date:- 4 oct 2025
# lab title:- assignment 1 

print('WELCOME MESSAGE')
print('THIS IS MY FIRST ASSIGNMENT OF PYTHON. AND HERE IS THE CODE AND THE RESULT FOR EXPENSE TRACKER ')

expenses = []
total_expense = 0

while True:
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    expenses.append((category, amount))
    total_expense += amount
    
    add_more = input("Do you want to add more? (yes/no): ")
    if add_more.lower() != 'yes':
        break

num_expenses = len(expenses)
average_expense = 0
if num_expenses > 0:
    average_expense = total_expense / num_expenses
    
print("\nYour Expenses:")
for category, amount in expenses:
    print(f"{category} - {amount:.1f}")

print(f"Total Expense: {total_expense:.1f}")
print(f"Average Expense: {average_expense:.1f}")

print("\nExpenses Record")
print("----------------")
for category, amount in expenses:
    print(f"{category} - {amount:.1f}")
print(f"Total Expense: {total_expense:.1f}")
print(f"Average Expense: {average_expense:.1f}")