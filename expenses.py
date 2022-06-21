expenses = [10.50, 8, 5, 15, 20, 5, 3]


total = sum(expenses)
# sum = 0 this block of code will do the same as the line on top of this.


# for x in expenses:
#     sum = sum + x

# print("You spent " + str(total) + " on lunch this week.") this does the same as line beneath but more code
# print("You spent $", total, " on lunch this week.", sep="")

total2 = 0
expenses2 = []

# for i in range(7):
#     expenses2.append(float(input("Enter an expense:")))

total2 = sum(expenses2)

# print("You spent $", total2, sep="")

total3 = 0
expenses3 = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses3.append(float(input("Enter an expense:")))

total3 = sum(expenses3)

print("You spent $", total3, sep="")