# ==========================================
# Topic: Control Flow (Loops: for, while, break, continue)
# ==========================================

print("--- 1. THE 'FOR' LOOP ---")
for i in range(5):
    print(f"Counting: {i}")

print("\n--- 2. THE 'WHILE' LOOP ---")
countdown = 3
while countdown > 0:
    print(f"Liftoff in {countdown}...")
    countdown -= 1  
print("Blastoff! 🚀")

print("\n--- 3. BREAK & CONTINUE ---")
for number in range(1, 5):
    if number == 2:
        continue # Skip 2
    if number == 4:
        break    # Stop at 4
    print(f"Processing number: {number}")


# ==========================================
# ADVANCED DEEP DIVE SECTION
# ==========================================
print("\n--- ADVANCED DEEP DIVE ---")

# A. Iterating directly over items (Strings/Lists)
# You don't need range() if you want to loop over text directly!
# This is how a tokenizer processes characters in an LLM.
word = "AI"
for letter in word:
    print(f"Character: {letter}")

# B. Nested Loops
# A loop inside a loop. 
# This is exactly how matrices (tensors) are processed in Deep Learning.
print("\nNested Loop Output (Coordinates):")
for x in range(2):        # Outer loop runs 2 times (0, 1)
    for y in range(2):    # Inner loop runs 2 times FOR EVERY outer loop step
        print(f"({x}, {y})")

# C. The 'pass' keyword
# When you are planning code but haven't written it yet, Python throws an error
# if you leave an 'if' or 'for' block empty. 'pass' fixes this.
if True:
    pass # "Do nothing right now, I will write this code later."

# D. The 'for / else' weird Python quirk
# In Python, loops can have an 'else' statement.
# The 'else' block runs ONLY if the loop finishes normally (without hitting a 'break').
print("\nFor/Else Loop Example:")
for n in range(3):
    print(f"Checking {n}")
    if n == 5:
        print("Found 5!")
        break
else:
    # This runs because the loop finished all 3 steps without breaking.
    print("Loop finished, but never found 5.")
