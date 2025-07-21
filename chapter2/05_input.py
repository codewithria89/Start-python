# Example 1: Taking a name as input
name = input("Enter your name: ")
print("Hello", name)

# Example 2: Taking age as input and using it
age = input("Enter your age: ")
print("You are", age, "years old")

# Example 3: Taking two numbers and adding them as strings
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print("String Addition:", num1 + num2)  # Just joins the strings

# Example 4: Converting input to integer before addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Numeric Addition:", num1 + num2)

# Example 5: Taking float input and multiplying
price = float(input("Enter price of item: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print("Total Price:", total)

# Example 6: Boolean-like input (manual check)
ans = input("Do you want to continue? (yes/no): ")
if ans.lower() == "yes":
    print("Continuing...")
else:
    print("Stopped.")
