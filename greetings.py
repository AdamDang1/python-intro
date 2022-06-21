# def greeting(name):
#     print("Hello", name)

# input_name = input("Enter your name:\n")
# greeting(input_name)

# THIS IS USING GLOBAL SCOPE
# Bad scope because name is defined globally so you would have to reassign it every time or make a new variable
# def greeting():
#     print("Hello", name)

# name = input("Enter your name:\n")
# greeting()

# THIS IS USING LOCAL SCOPT
# def greeting(name):
#     print("Hello", name)

# name1 = input("Enter your name:\n")
# greeting(name1)
# name2 = input("Enter your name:\n")
# greeting(name2)

# Creating a function
def addition(a, b):
    return a + b

# Main program
num1 = float(input("Enter your 1st number:\n"))
num2 = float(input("Enter your 2nd number:\n"))

# Calling our function
result = addition(num1, num2)
print("The result is", result)