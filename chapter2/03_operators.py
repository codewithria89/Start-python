# ========== 1. Arithmetic Operators ==========
print("🔢 Arithmetic Operators")
a = 10
b = 3

print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a // b =", a // b) # Floor division
print("a % b =", a % b)   # Remainder (modulus)
print("a ** b =", a ** b) # Exponentiation (power)

print("\n📝 Assignment Operators")
# ========== 2. Assignment Operators ==========
x = 5
print("Initial x =", x)

x += 2
print("x += 2:", x)  # Adds 2 to x

x *= 3
print("x *= 3:", x)  # Multiplies x by 3

x -= 4
print("x -= 4:", x)  # Subtracts 4 from x

x /= 2
print("x /= 2:", x)  # Divides x by 2

print("\n🔍 Comparison Operators")
# ========== 3. Comparison Operators ==========
a = 10
b = 3

print("a == b:", a == b)   # Checks if a equals b
print("a != b:", a != b)   # Checks if a is not equal to b
print("a > b:", a > b)     # Checks if a is greater than b
print("a < b:", a < b)     # Checks if a is less than b
print("a >= b:", a >= b)   # Checks if a is greater than or equal to b
print("a <= b:", a <= b)   # Checks if a is less than or equal to b

print("\n🧠 Logical Operators")
# ========== 4. Logical Operators ==========
print("True and False:", True and False)   # Returns True if both are True
print("True or False:", True or False)     # Returns True if at least one is True
print("not True:", not True)               # Reverses the result

print("\n🆔 Identity Operators")
# ========== 5. Identity Operators ==========
x = [1, 2]
y = x
z = [1, 2]

print("x is y:", x is y)             # True if x and y refer to the same object
print("x is z:", x is z)             # False because z is a different object
print("x is not z:", x is not z)     # True

print("\n🔎 Membership Operators")
# ========== 6. Membership Operators ==========
name = "anjali"
print("'a' in name:", 'a' in name)             # Checks if 'a' is in the string
print("'z' in name:", 'z' in name)             # Checks if 'z' is in the string

nums = [1, 2, 3]
print("2 in nums:", 2 in nums)                 # Checks if 2 is in the list
print("5 not in nums:", 5 not in nums)         # Checks if 5 is NOT in the list
