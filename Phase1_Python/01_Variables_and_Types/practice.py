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

# ==========================================
# ADVANCED DEEP DIVE (LLM Engineer Level)
# ==========================================

print("\n--- Advanced: NoneType ---")
# 'None' is a special primitive type that means "empty" or "null".
# We use this to initialize variables before we have data for them.
model_weights = None
print(f"[Debug] model_weights is type: {type(model_weights)}")

print("\n--- Advanced: Multiple Assignment ---")
# You can assign multiple variables on a single line!
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

print("\n--- Advanced: Truthiness ---")
# Any primitive can be cast to a Boolean using bool()
# 0, 0.0, None, and empty strings "" are always False.
# EVERYTHING else is True.
print(f"bool(0) is: {bool(0)}")
print(f"bool(1) is: {bool(1)}")
print(f"bool('') is: {bool('')}")
print(f"bool('hello') is: {bool('hello')}")

print("\n--- Advanced: Type Hinting ---")
# In modern Python (and especially AI), we use 'Type Hints' to make code readable.
# It doesn't force the type, but it helps the IDE catch bugs.
ai_model_name: str = "GPT-4"
parameter_count: float = 1.76e12

print("\n--- Advanced: memory addresses with id() ---")
# Where exactly does Python store this box in RAM?
print(f"The word '{ai_model_name}' is stored at memory address: {id(ai_model_name)}")

print("\n--- Advanced: Complex Numbers ---")
# Used heavily in advanced math and quantum computing.
# Python uses 'j' for the imaginary part.
complex_num = 3 + 4j
print(f"Complex number: {complex_num}. Type: {type(complex_num)}")

print("\n--- Advanced: isinstance() Check ---")
# The professional way to check a variable's type before doing math on it.
if isinstance(parameter_count, float):
    print("Yes, parameter count is a float!")

print("\n--- Advanced: Deleting variables ---")
# In AI, large tensors take up huge RAM. We use 'del' to destroy the variable and free memory.
massive_data = "100GB of text"
del massive_data
# print(massive_data) # This would now crash with a NameError!

print("\n--- Advanced: Small Integer Caching (CPython Quirks) ---")
# Python pre-loads numbers -5 to 256 to save memory.
a = 256
b = 256
print(f"Is 256 the EXACT same object in RAM? {a is b}") # True
c = 257
d = 257
print(f"Is 257 the EXACT same object in RAM? {c is d}") # False! Python made two separate 257s.

print("\n--- Advanced: Immutability ---")
# Strings and Integers CANNOT be changed. When you 'modify' them, Python destroys the old one.
original_word = "hello"
print(f"Memory address of 'hello': {id(original_word)}")
original_word = "hello!"
print(f"Memory address of 'hello!': {id(original_word)} (Notice it completely changed!)")

print("\n--- Advanced: Garbage Collection (Reference Counting) ---")
# Python tracks how many variables point to a memory box. When it hits 0, it deletes it.
import sys
shared_data = "This is a very specific string we are tracking."
pointer_2 = shared_data
# getrefcount() returns the true number of variables pointing to that string + 1 (for the getrefcount function itself)
print(f"Number of pointers looking at our string: {sys.getrefcount(shared_data)}")

print("\n--- Advanced: Bytes and Encoding (Pre-AI Tokens) ---")
# AI models don't read text, they read bytes.
# We convert strings to raw computer bytes using UTF-8 encoding.
raw_text = "AI"
encoded_bytes = raw_text.encode('utf-8')
print(f"Raw text: {raw_text}. Bytes format: {encoded_bytes}. Type: {type(encoded_bytes)}")
