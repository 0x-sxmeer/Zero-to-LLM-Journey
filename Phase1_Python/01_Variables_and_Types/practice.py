# ==========================================
# Topic: Variables, Primitive Types, and Type Conversion
# ==========================================
# Think of a variable as a labeled box where you store information.
# Python has 4 primitive (basic) types of boxes:
# 1. str (String): Text data.
# 2. int (Integer): Whole numbers (for math).
# 3. float (Floating point): Decimal numbers (for precise math).
# 4. bool (Boolean): True or False logic.
# ==========================================

print("--- Data Entry System ---")

# ------------------------------------------
# 1. STRING (str)
# ------------------------------------------
user_name = input("Enter your name: ")
print(f"[Debug] user_name is type: {type(user_name)}")


# ------------------------------------------
# 2. INTEGER (int) & TYPE CONVERSION
# ------------------------------------------
birth_year_str = input("Enter your birth year (e.g., 1995): ")
birth_year = int(birth_year_str)  
age = 2026 - birth_year
print(f"[Debug] age is type: {type(age)}")


# ------------------------------------------
# 3. FLOAT (float) & TYPE CONVERSION
# ------------------------------------------
coffee_price_str = input("How much did your coffee cost today? (e.g., 4.50): ")
coffee_price = float(coffee_price_str) 
yearly_coffee_cost = coffee_price * 365
print(f"[Debug] coffee_price is type: {type(coffee_price)}")


# ------------------------------------------
# 4. BOOLEAN (bool)
# ------------------------------------------
is_adult = age >= 18
print(f"[Debug] is_adult is type: {type(is_adult)}")


# ==========================================
# ADVANCED DEEP DIVE SECTION
# ==========================================
print("\n--- ADVANCED DEEP DIVE ---")

# A. NoneType
# None is a special type representing the ABSENCE of a value.
# It is heavily used in machine learning when a variable is empty before training.
model_weights = None
print(f"model_weights is {model_weights}, Type: {type(model_weights)}")

# B. Truthiness (Casting to bool)
# Python considers empty things as False, and non-empty things as True.
# 0 is False, any other number is True.
print(f"bool(0) is {bool(0)}")           # False
print(f"bool(1) is {bool(1)}")           # True
print(f"bool('') is {bool('')}")         # False (Empty string)
print(f"bool('AI') is {bool('AI')}")     # True (String has text)
print(f"bool(None) is {bool(None)}")     # False

# C. Multiple Assignment
# You can unpack values into multiple variables on a single line.
x, y, z = 10, 20, 30
print(f"Multiple assignment: x={x}, y={y}, z={z}")

# D. String Conversion (str)
# Sometimes we need to turn a number back into text.
# For example, to concatenate (glue) it to another string without f-strings.
price_tag = "The cost is $" + str(coffee_price)
print(price_tag)
