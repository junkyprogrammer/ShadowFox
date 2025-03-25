
#1: Friends' names and lengths
friends_names = ["Aditya", "Mohnish", "Shubham", "Kunj", "Chanda Malla"]
name_lengths = [(name, len(name)) for name in friends_names]

print("Friends' names and their lengths:")
for name, length in name_lengths:
    print(f"{name}: {length} characters")

print("\n" + "="*50 + "\n")

#2 tracking the expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculating the total expenses  
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

# Printing the total expenses
print("Total Expenses:")
print(f"Your total: {your_total} INR")
print(f"Partner's total: {partner_total} INR")

# Determining the differences
if your_total > partner_total:
    print(f"\nYou spent more by {your_total - partner_total} INR")
elif partner_total > your_total:
    print(f"\nYour partner spent more by  {partner_total - your_total} INR")
else:
    print("\nYou both spent the same amount")

# Finding the significant expenses
print("\nSignificant differences in spending:")
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > 100:  # Consider differences over $100 as significant
        print(f"{category}: {difference} INR difference")
