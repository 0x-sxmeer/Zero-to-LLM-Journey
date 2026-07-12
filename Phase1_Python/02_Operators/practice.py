# ==========================================
# Topic: Operators
# ==========================================
# This script demonstrates EVERY major operator in Python:
# 1. Arithmetic (Math)
# 2. Assignment (Changing variables)
# 3. Comparison (Asking questions)
# 4. Logical (Combining questions)
# ==========================================

print("--- 1. ARITHMETIC OPERATORS ---")
print(f"Addition (+): 10 + 3 = {10 + 3}")
print(f"Subtraction (-): 10 - 3 = {10 - 3}")
print(f"Multiplication (*): 10 * 3 = {10 * 3}")
print(f"Division (/): 10 / 3 = {10 / 3}") # Always returns a float
print(f"Floor Division (//): 10 // 3 = {10 // 3}") # Chops off the decimal
print(f"Modulo/Remainder (%): 10 % 3 = {10 % 3}")  # 10 divided by 3 leaves a remainder of 1
print(f"Exponent/Power (**): 10 ** 3 = {10 ** 3}") # 10 to the power of 3

print("\n--- 2. ASSIGNMENT OPERATORS ---")
score = 100
print(f"Original score (=): {score}")
score += 50  
print(f"After += 50: {score}")
score -= 20  
print(f"After -= 20: {score}")
score *= 2   
print(f"After *= 2: {score}")
score /= 10  
print(f"After /= 10: {score}")

print("\n--- 3. COMPARISON OPERATORS ---")
print(f"Equal (==): 5 == 5 is {5 == 5}")
print(f"Not Equal (!=): 5 != 3 is {5 != 3}")
print(f"Greater Than (>): 10 > 5 is {10 > 5}")
print(f"Less Than (<): 10 < 5 is {10 < 5}")
print(f"Greater/Equal (>=): 10 >= 10 is {10 >= 10}")
print(f"Less/Equal (<=): 8 <= 10 is {8 <= 10}")

print("\n--- 4. LOGICAL OPERATORS ---")
has_ticket = True
has_id = False
print(f"has_ticket AND has_id: {has_ticket and has_id}") 
print(f"has_ticket OR has_id: {has_ticket or has_id}") 
print(f"NOT has_ticket: {not has_ticket}")

# ==========================================
# ADVANCED DEEP DIVE (LLM Engineer Level)
# ==========================================
print("\n--- Advanced: Identity vs Equality ---")
a = [1, 2, 3]
b = [1, 2, 3]
print(f"a == b? (Equal values): {a == b}")
print(f"a is b? (Same memory box): {a is b}")

print("\n--- Advanced: Membership Operators ---")
word = "Artificial Intelligence"
print(f"Is 'Art' in the word? {'Art' in word}")
print(f"Is 'Dog' NOT in the word? {'Dog' not in word}")

print("\n--- Advanced: Bitwise Operators (&, |, ^, ~, <<, >>) ---")
print(f"5 & 3 (Bitwise AND): {5 & 3}")  
print(f"5 | 3 (Bitwise OR): {5 | 3}")   
print(f"5 ^ 3 (Bitwise XOR): {5 ^ 3}")
print(f"~5 (Bitwise NOT): {~5}")
print(f"5 << 1 (Left Shift): {5 << 1}")
print(f"5 >> 1 (Right Shift): {5 >> 1}")

print("\n--- Advanced: Short-Circuit Logic ---")
def crash():
    return 1 / 0
if False and crash():
    print("This will never run, and the crash is ignored!")
if True or crash():
    print("This runs perfectly, the crash is ignored!")

print("\n--- Advanced: Short-Circuit Assignment ---")
user_input = ""
final_name = user_input or "Anonymous_User"
print(f"Assigned name: {final_name}")

print("\n--- Advanced: Chained Comparisons ---")
test_age = 25
print(f"Is 18 <= 25 < 65? {18 <= test_age < 65}")

print("\n--- Advanced: The Matrix Multiplication Operator (@) ---")
class Matrix:
    def __init__(self, name):
        self.name = name
    def __matmul__(self, other):
        return f"Multiplying Matrix {self.name} by Matrix {other.name}"

A = Matrix("A")
B = Matrix("B")
print(f"A @ B = {A @ B}")
