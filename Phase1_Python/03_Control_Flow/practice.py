# ==========================================
# Topic: Control Flow (if/elif/else, while, for, break/continue)
# ==========================================
# THE FEYNMAN CHECK (Plain English Summary)
# - 'if/elif/else': A fork in the road. Choose a path based on a True/False question.
# - 'for' loop: Use this when you know EXACTLY how many times to repeat something.
# - 'while' loop: Use this when you want to repeat UNTIL a condition stops being true.
# - 'break': Smash the emergency glass. Stop the loop instantly.
# - 'continue': Skip the rest of THIS loop cycle, but keep the loop running.
#
# THE BEGINNER TRAP: Truthy and Falsy values
# You don't have to write 'if age > 0:'. You can just write 'if age:'.
# In Python, the number 0, an empty string "", empty lists [], and None are ALL "Falsy".
# If you put them in an 'if' statement, Python treats them as False.
# EVERYTHING else (like the number 1, or the string "hello") is "Truthy" (True).
# ==========================================

print("--- 1. IF / ELIF / ELSE ---")
print("--- The Nightclub Bouncer Program ---")
age = int(input("How old are you? "))
wallet_money = float(input("How much money do you have? $"))
drink_price = 15.00

is_old_enough = age >= 21
has_enough_money = wallet_money >= drink_price

if is_old_enough and has_enough_money:
    print("\nBouncer: You are old enough and have money. Come on in!")
    wallet_money -= drink_price
    print(f"You bought a drink. You have ${wallet_money:.2f} left.")
elif is_old_enough and not has_enough_money:
    print("\nBouncer: You are old enough, but you are broke. Go to the ATM!")
else:
    print(f"\nBouncer: Sorry kid. Come back in {21 - age} years.")

print("\n--- 2. THE 'FOR' LOOP ---")
for i in range(5):
    print(f"Counting: {i}")

print("\n--- 3. THE 'WHILE' LOOP ---")
countdown = 3
while countdown > 0:
    print(f"Liftoff in {countdown}...")
    countdown -= 1
print("Blastoff! 🚀")

print("\n--- 4. BREAK & CONTINUE ---")
for number in range(1, 6):
    if number == 3:
        print("Skipping 3 (continue)...")
        continue
    if number == 5:
        print("Hit 5! Stopping early (break)...")
        break
    print(f"Processing number: {number}")

# ==========================================
# ADVANCED DEEP DIVE (LLM Engineer Level)
# ==========================================
print("\n--- Advanced: The 'pass' Keyword ---")
if 10 > 5:
    pass # Placeholder

print("\n--- Advanced: The Walrus Operator (:=) ---")
word = "Artificial"
if (n := len(word)) > 5:
    print(f"The word has {n} letters, which is long!")

print("\n--- Advanced: Ternary Operator (One-line If/Else) ---")
status = "Adult" if age >= 18 else "Minor"
print(f"Status is: {status}")

print("\n--- Advanced: Python 3.10 Match/Case ---")
status_code = 404
match status_code:
    case 200:
        print("Success!")
    case 404:
        print("Not Found!")
    case _:
        print("Unknown error!")

print("\n--- Advanced: Iterating over Strings ---")
for char in "LLM":
    print(char)

print("\n--- Advanced: Nested Loops ---")
for i in range(2):
    for j in range(2):
        print(f"Coordinates: x={i}, y={j}")

print("\n--- Advanced: The loop 'else' block ---")
for num in range(3):
    print("Searching...")
else:
    print("Search complete. No 'break' was triggered.")

print("\n--- Advanced: Enumerate and Zip ---")
word_list = ["AI", "ML"]
scores = [95, 82]
for index, (w, s) in enumerate(zip(word_list, scores)):
    print(f"Item {index}: {w} got {s}")

print("\n--- Advanced: Infinite Loops with Break ---")
attempts = 0
while True:
    attempts += 1
    if attempts == 3:
        print("Infinite loop broken internally!")
        break

print("\n--- Advanced: The Iteration Protocol ---")
word_iterator = iter("AI")
print(next(word_iterator))
print(next(word_iterator))

print("\n--- Advanced: itertools & reversed ---")
import itertools
for x, y in itertools.product(range(2), range(2)):
    pass
for num in reversed(range(1, 4)):
    print(f"{num}...")

# ==========================================
# YOUR CHALLENGE:
# Write a tiny program below that asks the user for a test score (0-100).
# Print "A" if it is >= 90
# Print "B" if it is >= 80
# Print "C" if it is >= 70
# Print "F" if it is < 70
# Then write a 'while' loop that asks the user to type the word "quit" to exit.
# ==========================================
