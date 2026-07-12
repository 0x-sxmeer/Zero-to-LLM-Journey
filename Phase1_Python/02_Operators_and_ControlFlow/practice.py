# ==========================================
# Topic: Operators and Control Flow (if/elif/else)
# ==========================================
# In Python, we use Operators to do math or compare things.
# We use Control Flow to make decisions based on those comparisons.
# ==========================================

print("--- The Nightclub Bouncer Program ---")

# 1. ASSIGNMENT & ARITHMETIC OPERATORS
# = (Assignment): Puts a value in a box
# +, -, *, /, % (Arithmetic): Math operations. % is modulo (remainder).
age = int(input("How old are you? "))
wallet_money = float(input("How much money do you have? $"))

drink_price = 15.00
# -= (Subtract and assign): Decreases a variable by an amount.
# E.g., wallet_money -= drink_price is the same as wallet_money = wallet_money - drink_price


# 2. COMPARISON OPERATORS
# == (Equal to), != (Not equal to)
# > (Greater than), < (Less than)
# >= (Greater than or equal to), <= (Less than or equal to)

is_old_enough = age >= 21
has_enough_money = wallet_money >= drink_price


# 3. LOGICAL OPERATORS & CONTROL FLOW (if/elif/else)
# and : True only if BOTH sides are true
# or  : True if AT LEAST ONE side is true
# not : Flips True to False, and False to True

if is_old_enough and has_enough_money:
    # If both conditions are met, this block runs.
    print("\nBouncer: You are old enough and have money. Come on in!")
    wallet_money -= drink_price  # Buying a drink
    print(f"You bought a drink. You have ${wallet_money:.2f} left.")

elif is_old_enough and not has_enough_money:
    # If the first 'if' fails, Python checks this 'elif' (Else If)
    print("\nBouncer: You are old enough, but you are broke. Go to the ATM!")

else:
    # If ALL above conditions fail, the 'else' block runs automatically.
    print(f"\nBouncer: Sorry kid, you are only {age}. Come back in {21 - age} years.")


# ==========================================
# YOUR CHALLENGE:
# Write a tiny program below that asks the user for a test score (0-100).
# Print "A" if it is 90 or above.
# Print "B" if it is 80 to 89.
# Print "C" if it is 70 to 79.
# Print "F" if it is below 70.
# ==========================================
