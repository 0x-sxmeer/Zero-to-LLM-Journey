# ==========================================
# Topic: Variables, Primitive Types, and Type Conversion
# ==========================================
# This script demonstrates all 4 primitive types in Python:
# 1. str (String): Text
# 2. int (Integer): Whole numbers
# 3. float (Floating point): Decimal numbers
# 4. bool (Boolean): True or False
# ==========================================

print("--- Data Entry System ---")

# 1. STRING (str)
# input() ALWAYS returns a string, no matter what you type.
user_name = input("Enter your name: ")
print(f"[Debug] user_name is type: {type(user_name)}")

# 2. INTEGER (int) & TYPE CONVERSION
# We must convert the string from input() into an int to do math.
birth_year_str = input("Enter your birth year (e.g., 1995): ")
birth_year = int(birth_year_str)  # Type conversion (Casting)
age = 2026 - birth_year
print(f"[Debug] age is type: {type(age)}")

# 3. FLOAT (float) & TYPE CONVERSION
# Floats are used for precision (decimals).
coffee_price_str = input("How much did your coffee cost today? (e.g., 4.50): ")
coffee_price = float(coffee_price_str) # Type conversion to float
yearly_coffee_cost = coffee_price * 365
print(f"[Debug] coffee_price is type: {type(coffee_price)}")

# 4. BOOLEAN (bool)
# Booleans evaluate to True or False. Often created using comparison operators (> , < , ==).
is_adult = age >= 18
print(f"[Debug] is_adult is type: {type(is_adult)}")

print("\n--- Generating Your Profile ---")

# 5. Putting it all together using an f-string!
# f-strings let you inject variables directly into text, no matter their type.
profile_message = f"""
Name: {user_name}
Age: {age} years old
Adult Status: {is_adult}
Coffee Habit: You spend roughly ${yearly_coffee_cost:.2f} a year on coffee!
"""

print(profile_message)
