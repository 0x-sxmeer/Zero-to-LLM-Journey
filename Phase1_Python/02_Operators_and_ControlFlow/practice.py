# ==========================================
# Topic: ALL Operators & Control Flow
# ==========================================
# This script demonstrates EVERY major operator in Python:
# 1. Arithmetic (Math)
# 2. Assignment (Changing variables)
# 3. Comparison (Asking questions)
# 4. Logical (Combining questions)
# ==========================================

print("--- 1. ARITHMETIC OPERATORS ---")
# Standard Math
print(f"Addition (+): 10 + 3 = {10 + 3}")
print(f"Subtraction (-): 10 - 3 = {10 - 3}")
print(f"Multiplication (*): 10 * 3 = {10 * 3}")
print(f"Division (/): 10 / 3 = {10 / 3}") # Always returns a float

# Advanced Math
print(f"Floor Division (//): 10 // 3 = {10 // 3}") # Chops off the decimal
print(f"Modulo/Remainder (%): 10 % 3 = {10 % 3}")  # 10 divided by 3 leaves a remainder of 1
print(f"Exponent/Power (**): 10 ** 3 = {10 ** 3}") # 10 to the power of 3

print("\n--- 2. ASSIGNMENT OPERATORS ---")
score = 100
print(f"Original score (=): {score}")

score += 50  # Same as: score = score + 50
print(f"After += 50 (Add and assign): {score}")

score -= 20  # Same as: score = score - 20
print(f"After -= 20 (Subtract and assign): {score}")

score *= 2   # Same as: score = score * 2
print(f"After *= 2 (Multiply and assign): {score}")

score /= 10  # Same as: score = score / 10
print(f"After /= 10 (Divide and assign): {score}")


print("\n--- 3. COMPARISON OPERATORS ---")
# These ALWAYS return a Boolean (True or False)
print(f"Equal (==): 5 == 5 is {5 == 5}")
print(f"Not Equal (!=): 5 != 3 is {5 != 3}")
print(f"Greater Than (>): 10 > 5 is {10 > 5}")
print(f"Less Than (<): 10 < 5 is {10 < 5}")
print(f"Greater/Equal (>=): 10 >= 10 is {10 >= 10}")
print(f"Less/Equal (<=): 8 <= 10 is {8 <= 10}")


print("\n--- 4. LOGICAL OPERATORS ---")
# Used to combine multiple True/False conditions
has_ticket = True
has_id = False

# 'and' requires BOTH to be True
print(f"has_ticket AND has_id: {has_ticket and has_id}") 

# 'or' requires AT LEAST ONE to be True
print(f"has_ticket OR has_id: {has_ticket or has_id}") 

# 'not' flips the True/False value
print(f"NOT has_ticket: {not has_ticket}")


# ==========================================
# PUTTING IT ALL TOGETHER: Control Flow
# ==========================================
print("\n--- The Nightclub Bouncer Program ---")
age = int(input("How old are you? "))
wallet_money = float(input("How much money do you have? $"))

drink_price = 15.00

# Using Comparison Operators
is_old_enough = age >= 21
has_enough_money = wallet_money >= drink_price

# Using Logical Operators (and, not)
if is_old_enough and has_enough_money:
    print("\nBouncer: You are old enough and have money. Come on in!")
    wallet_money -= drink_price  # Using Assignment Operator
    print(f"You bought a drink. You have ${wallet_money:.2f} left.")

elif is_old_enough and not has_enough_money:
    print("\nBouncer: You are old enough, but you are broke. Go to the ATM!")

else:
    print(f"\nBouncer: Sorry kid. Come back in {21 - age} years.")

# ==========================================
# 5. LOOPS (while, for, break, continue)
# ==========================================
print("\n--- LOOPING CONTROL FLOW ---")

# A. 'while' loop: keeps going as long as the condition is True.
print("\nCounting down (while loop):")
countdown = 3
while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1
print("Go!")

# B. 'for' loop: iterates over a sequence (like a list or a range of numbers)
print("\nPrinting a range (for loop):")
for i in range(1, 4):  # range(1, 4) gives 1, 2, 3
    print(f"Loop iteration {i}")

# C. 'break' and 'continue'
print("\nTesting break and continue in a loop:")
for num in range(1, 6): # 1, 2, 3, 4, 5
    if num == 3:
        print("Skipping 3! (continue)")
        continue # Skips the rest of THIS iteration and goes to the next number
    
    if num == 5:
        print("Hit 5! Stopping entirely. (break)")
        break # Completely breaks out of the loop and stops it
        
    print(f"Processing number {num}")


# ==========================================
# YOUR CHALLENGE:
# Write a tiny program below that asks the user for a test score (0-100).
# Print "A" if it is >= 90
# Print "B" if it is >= 80
# Print "C" if it is >= 70
# Print "F" if it is < 70
# ==========================================
