# creating variables and simple math
amount = 200
tax = .07
total = amount + amount*tax
print(total)

# brings decimal to whole number
amount = int(10.6)
print(amount)

# brings whole number to decimal
amount = float(10)
print(amount)

# creating name variable and printing to console single quotes
name = 'Sarah'
print(name)

# using double quotes
store_name = "Sarah's Store"
print(store_name)

# concatenating 2 variables while adding a space in between
hello = "Hello"
name = "Sarah"
greeting = hello + " " + name
print(greeting)

#concatenating variables while entering an input
hello = "Hello"
name = input("What's your name?")
greeting = hello + " " + name
print(greeting)

# concatenating variables while entering an input with a line break
hello = "Hello"
name = input("What's your name?\n")
greeting = hello + " " + name
print(greeting)