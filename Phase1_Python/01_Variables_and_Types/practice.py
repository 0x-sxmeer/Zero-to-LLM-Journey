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
# What happens: Python prints the text and waits. You type a word.
# The result: Python puts your word in a box labeled 'user_name'. 
# Because it is a word, this box is classified as a String (str).
# IMPORTANT: input() ALWAYS hands back a String, even if you type numbers!
user_name = input("Enter your name: ")
print(f"[Debug] user_name is type: {type(user_name)}")


# ------------------------------------------
# 2. INTEGER (int) & TYPE CONVERSION
# ------------------------------------------
# You type '1995', but input() stores it as TEXT ("1995"). 
# You can't do math with text (e.g., 2026 - "1995" crashes).
birth_year_str = input("Enter your birth year (e.g., 1995): ")

# THE SOLUTION: int() is a machine that takes the text, strips the quotes, 
# and turns it into a real, mathematical whole number. This is called Type Conversion (Casting).
birth_year = int(birth_year_str)  

# Now the math works perfectly!
age = 2026 - birth_year
print(f"[Debug] age is type: {type(age)}")


# ------------------------------------------
# 3. FLOAT (float) & TYPE CONVERSION
# ------------------------------------------
# You type '4.50'. Again, Python stores it as text.
coffee_price_str = input("How much did your coffee cost today? (e.g., 4.50): ")

# We can't use int() here, because int() destroys decimals (it turns 4.50 into 4).
# Instead, we use float(). This turns text into a highly precise decimal number.
coffee_price = float(coffee_price_str) 
yearly_coffee_cost = coffee_price * 365
print(f"[Debug] coffee_price is type: {type(coffee_price)}")


# ------------------------------------------
# 4. BOOLEAN (bool)
# ------------------------------------------
# Python looks in the 'age' box. It asks: "Is this number >= 18?"
# The answer is a simple True or False. 
# It creates a new box called 'is_adult' and puts True or False inside.
is_adult = age >= 18
print(f"[Debug] is_adult is type: {type(is_adult)}")


print("\n--- Generating Your Profile ---")

# ------------------------------------------
# 5. Bringing it together with f-strings
# ------------------------------------------
# The 'f' at the start tells Python: "Whenever you see curly brackets {}, 
# open the box with that name, take what's inside, and paste it here."
# Pro-trick: {:.2f} forces a float to round to exactly 2 decimal places!
profile_message = f"""
Name: {user_name}
Age: {age} years old
Adult Status: {is_adult}
Coffee Habit: You spend roughly ${yearly_coffee_cost:.2f} a year on coffee!
"""

print(profile_message)
