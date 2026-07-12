# ==========================================
# Topic: Functions
# ==========================================
# THE FEYNMAN CHECK (Plain English Summary)
# - Function: A mini-program or recipe you write once and can run (call) anytime.
# - Parameter: The blank labels on the recipe (e.g. "ingredient_1").
# - Argument: The actual data you put in (e.g. "chicken").
# - Return Value: The finished meal the function hands back to you.
# - Scope: The "Vegas Rule". Variables created inside a function stay in the function.
#          The rest of the program cannot see them.
# ==========================================

print("--- 1. BASIC FUNCTIONS & RETURNS ---")
# Defining a function uses 'def'
def greet_user(name):
    # This string is the 'Return Value'. It hands the data back instead of just printing it.
    return f"Hello, {name}! Welcome to the system."

# We 'call' the function and store what it hands back (returns) in a variable
message = greet_user("Alice")
print(message)


print("\n--- 2. DEFAULT ARGUMENTS ---")
# You can give parameters a default value just in case the user forgets to provide one.
def calculate_tax(amount, tax_rate=0.08):
    total = amount + (amount * tax_rate)
    return total

print(f"Tax on $100 (using default 8%): ${calculate_tax(100):.2f}")
print(f"Tax on $100 (custom 10% rate): ${calculate_tax(100, 0.10):.2f}")


print("\n--- 3. *args and **kwargs (The 'Catch-All' Parameters) ---")
# *args (Arguments): Collects any number of regular ingredients into a Tuple.
def add_all_numbers(*args):
    total = sum(args)
    return total

print(f"Adding 3 numbers: {add_all_numbers(1, 2, 3)}")
print(f"Adding 6 numbers: {add_all_numbers(10, 20, 30, 40, 50, 60)}")

# **kwargs (Keyword Arguments): Collects any number of labeled ingredients into a Dictionary.
def build_profile(first, last, **kwargs):
    profile = {'first_name': first, 'last_name': last}
    profile.update(kwargs) # Add all the extra key-value pairs
    return profile

user_profile = build_profile("John", "Doe", age=28, role="Admin", planet="Earth")
print(f"User Profile: {user_profile}")


print("\n--- 4. SCOPE (Local vs Global) ---")
# Global scope (everyone can see this)
database_name = "Main_DB"

def update_database():
    # Local scope (ONLY this function can see this)
    temp_data = "Secret info"
    print(f"Inside function: I can see '{database_name}' and '{temp_data}'")

update_database()
# print(temp_data) # This would CRASH! 'temp_data' was destroyed when the function ended.


print("\n--- 5. RECURSION (Inception) ---")
# A function that calls itself! It MUST have a 'base case' (a reason to stop),
# otherwise it loops forever and crashes with a RecursionError.
def countdown(n):
    if n <= 0:  # Base case (The stopping condition)
        print("Boom!")
    else:
        print(f"{n}...")
        countdown(n - 1)  # The function calls itself with a smaller number

countdown(3)


# ==========================================
# ADVANCED DEEP DIVE (LLM Engineer Level)
# ==========================================
print("\n--- Advanced: First-Class Functions ---")
# In Python, functions are just objects. You can pass them as arguments to OTHER functions!
def shout(text):
    return text.upper()

def process_text(func, text):
    # It takes a function 'func' and runs it on the 'text'
    return func(text)

print(process_text(shout, "machine learning is cool"))

print("\n--- Advanced: Lambda Functions (Anonymous Functions) ---")
# Sometimes you need a tiny function for just one line of code.
# You write it using the 'lambda' keyword instead of 'def'. No return statement needed!
multiply = lambda x, y: x * y
print(f"Lambda multiply (5 * 4): {multiply(5, 4)}")

print("\n--- Advanced: Type Hinting for Functions ---")
# Professional AI engineers ALWAYS type-hint what a function takes and what it returns '->'
def clean_data(raw_text: str, remove_spaces: bool = True) -> str:
    if remove_spaces:
        return raw_text.strip()
    return raw_text
print(f"Cleaned string: '{clean_data('   noisy text   ')}'")

print("\n--- Advanced: Decorators (The @ Symbol) ---")
# A decorator is a function that wraps another function to change its behavior.
# It is heavily used in AI (PyTorch) and web servers (FastAPI/Flask).
def my_timer_decorator(func):
    def wrapper():
        print("Starting timer...")
        func()
        print("Stopping timer...")
    return wrapper

@my_timer_decorator
def heavy_ai_computation():
    print("Crunching billions of numbers...")

heavy_ai_computation()

# ==========================================
# YOUR CHALLENGE:
# Write a function called `calculate_grade` that takes a `score` (e.g., 85).
# It should return "A" for >=90, "B" for >=80, "C" for >=70, and "F" otherwise.
# Type-hint the function so it expects an `int` and returns a `str`.
# Then, call your function and print the result!
# ==========================================
