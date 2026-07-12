# ==========================================
# Topic: ALL Operators & Control Flow
# ==========================================
print("--- 1. ARITHMETIC OPERATORS ---")
print(f"Addition (+): 10 + 3 = {10 + 3}")
print(f"Floor Division (//): 10 // 3 = {10 // 3}") 
print(f"Modulo/Remainder (%): 10 % 3 = {10 % 3}")  
print(f"Exponent/Power (**): 10 ** 3 = {10 ** 3}") 

print("\n--- 2. ASSIGNMENT OPERATORS ---")
score = 100
score += 50  
score /= 10  
print(f"Final score: {score}")

print("\n--- 3. COMPARISON OPERATORS ---")
print(f"Equal (==): 5 == 5 is {5 == 5}")
print(f"Not Equal (!=): 5 != 3 is {5 != 3}")

print("\n--- 4. LOGICAL OPERATORS ---")
has_ticket = True
has_id = False
print(f"has_ticket AND has_id: {has_ticket and has_id}") 
print(f"NOT has_ticket: {not has_ticket}")

# ==========================================
# ADVANCED DEEP DIVE SECTION
# ==========================================
print("\n--- ADVANCED DEEP DIVE ---")

# A. Identity Operators (is, is not)
# '==' checks if values are equal. 
# 'is' checks if they are literally the SAME object in memory.
# ALWAYS use 'is' when checking for None!
x = None
print(f"Is x None? {x is None}")
print(f"Is x not None? {x is not None}")

# B. Membership Operators (in, not in)
# Checks if a sequence contains a value. Extremely useful for text processing (NLP).
text = "The quick brown fox"
print(f"Is 'fox' in text? {'fox' in text}")
print(f"Is 'cat' not in text? {'cat' not in text}")

# C. Order of Precedence (PEMDAS)
# Python respects math rules. Use parentheses ( ) to force order.
calculation = 10 + 5 * 2    # Multiplication happens first (20)
forced_calc = (10 + 5) * 2  # Addition happens first (30)
print(f"Standard: {calculation}, Forced: {forced_calc}")

# D. Bitwise Operators (&, |, ^, ~)
# These compare numbers at the binary (1s and 0s) level.
# In LLM Engineering, you'll see this when doing model quantization (e.g., 4-bit integers).
# 5 is 0101 in binary, 3 is 0011.
# 5 & 3 (Bitwise AND) compares them and returns 0001 (which is 1).
print(f"5 & 3 = {5 & 3}")

# E. Match / Case (Python 3.10+)
# This is an advanced alternative to massive if/elif/else chains.
status_code = 404
print("\n--- Match/Case Demo ---")
match status_code:
    case 200:
        print("OK - Request succeeded")
    case 404:
        print("Error - Not Found")
    case 500:
        print("Error - Server Crash")
    case _:
        # The underscore _ is the "catch-all" (like 'else')
        print("Unknown Status")
