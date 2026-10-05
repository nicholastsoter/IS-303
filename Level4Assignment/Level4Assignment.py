# Nick Soter
# Level 4 
# Financial Summarizer

# Initialize a list of finances and other variables needed
finance_list = []

finance = 1
small_expense = 0
medium_expense = 0
large_expense = 0
expense_counter = 0

# Ask the user for items in a list in a while loop, iterating depending on the amount of money entered
while finance != 0:
    finance = float(input("Enter an expense or 0 to finish: $"))
    if finance < 0:
        print("Please enter a positive number.")
    elif finance != 0:
        finance_list.append(finance)
        expense_counter += 1
        if finance < 25.0:
            small_expense += 1
        elif finance >= 25 and finance <= 100:
            medium_expense += 1
        elif finance > 100:
            large_expense += 1

# We then need to classify the items in the list:
num_total = 0
for num in finance_list:
    num_total += num

# Calculations
average = num_total / expense_counter
smallest = min(finance_list)
largest = max(finance_list)

print("\n---Expense Summary---")
# Total number of expenses
print(f"Number of expenses: {expense_counter}")
# Total expenses
print(f"Total: ${round(num_total, 2)}")
# Average expense
print(f"Average: ${round(average, 2)}")
# Smallest expense
print(f"Smallest: ${round(smallest, 2)}")
# Largest expense
print(f"Largest: ${round(largest, 2)}")
# Number of small, medium, and large expenses
print(f"\nSmall expenses: {small_expense}")
print(f"Medium expenses: {medium_expense}")
print(f"Large expenses: {large_expense}")

