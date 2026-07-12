# ==========================================
# Topic: Control Flow (Loops: for, while, break, continue)
# ==========================================
# We use loops when we want the computer to repeat an action.
# 1. for loops: When we know exactly how many times to repeat.
# 2. while loops: When we want to repeat UNTIL a condition changes.
# ==========================================

print("--- 1. THE 'FOR' LOOP ---")
# 'range(5)' generates numbers from 0 to 4 (it stops before 5).
for i in range(5):
    print(f"Counting: {i}")

print("\n--- 2. THE 'WHILE' LOOP ---")
# A while loop keeps running as long as the condition is True.
countdown = 3
while countdown > 0:
    print(f"Liftoff in {countdown}...")
    countdown -= 1  # If we forget this, the loop runs forever!
print("Blastoff! 🚀")

print("\n--- 3. BREAK (Emergency Stop) ---")
# 'break' completely shatters the loop and stops it immediately.
for number in range(1, 10):
    if number == 4:
        print("Found the number 4! Stopping the loop early.")
        break  # Kills the loop right here.
    print(f"Checking number: {number}")

print("\n--- 4. CONTINUE (Skip the rest, go to next) ---")
# 'continue' skips the current iteration and jumps to the next one.
for number in range(1, 6):
    if number == 3:
        print("Skipping number 3...")
        continue  # Skips the print statement below for '3'
    print(f"Processing number: {number}")

# ==========================================
# ADVANCED DEEP DIVE (LLM Engineer Level)
# ==========================================
print("\n--- Advanced: Iterating over Strings ---")
# You don't just loop over numbers. You can loop over the letters in text!
for char in "LLM":
    print(char)

print("\n--- Advanced: Nested Loops ---")
# A loop inside a loop. This is how neural network matrix multiplication works!
for i in range(2):
    for j in range(2):
        print(f"Coordinates: x={i}, y={j}")

print("\n--- Advanced: The loop 'else' block ---")
# In Python, loops can have an 'else' block.
# It ONLY runs if the loop finishes normally (without hitting a 'break').
for num in range(3):
    print("Searching...")
else:
    print("Search complete. No 'break' was triggered.")

print("\n--- Advanced: Python 3.10 Match/Case ---")
# The modern, beautiful alternative to massive if/elif chains.
status_code = 404
match status_code:
    case 200:
        print("Success!")
    case 404:
        print("Not Found!")
    case _:
        print("Unknown error!") # The '_' is the default catch-all

print("\n--- Advanced: Enumerate (Looping with an Index) ---")
# When you need both the item AND its position (index) in the list.
word_list = ["AI", "Machine Learning", "LLM"]
for index, w in enumerate(word_list):
    print(f"Item {index}: {w}")

print("\n--- Advanced: Zip (Looping Multiple things at once) ---")
# Combine two sequences like a zipper.
names = ["Alice", "Bob"]
scores = [95, 82]
for name, score in zip(names, scores):
    print(f"{name} got a {score}")

print("\n--- Advanced: Infinite Loops with Break ---")
# Often you don't know how long a loop will run (like a server listening for requests).
# We use 'while True' and rely on an internal 'break' condition.
attempts = 0
while True:
    attempts += 1
    if attempts == 3:
        print("Infinite loop broken internally!")
        break

print("\n--- Advanced: The Iteration Protocol (iter and next) ---")
# This is what a 'for' loop actually does secretly under the hood!
# It creates an iterator, and calls next() until it hits a StopIteration error.
word_iterator = iter("AI")
print(next(word_iterator)) # Prints 'A'
print(next(word_iterator)) # Prints 'I'
# print(next(word_iterator)) # If uncommented, this crashes with StopIteration!

print("\n--- Advanced: itertools (The LLM Engineer's secret weapon) ---")
# When nested loops get too deep, we use itertools.product to flatten them.
import itertools
print("Itertools Product (Flattened Nested Loop):")
for x, y in itertools.product(range(2), range(2)):
    print(f"x={x}, y={y}")

print("\n--- Advanced: Looping Backwards ---")
# Using reversed() is faster and cleaner than doing math with indices.
for num in reversed(range(1, 4)):
    print(f"{num}...")

# Note: List Comprehensions, Generators (yield), and Dictionary iteration
# are all forms of loops, but they have their own dedicated sections later on your roadmap!

# ==========================================
# YOUR CHALLENGE:
# Write a 'while' loop below that asks the user to type the word "quit".
# If they type anything else, it asks again.
# If they type "quit", the loop breaks and prints "Goodbye!"
# ==========================================
