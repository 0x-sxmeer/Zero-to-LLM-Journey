# Advanced Python Fundamentals Deep Dive

This document covers the advanced nuances of Python variables, operators, and control flow—the mechanics you need to understand to build AI systems.

## 1. Variables & Types (The Nuances)

### The `NoneType`
In Python, when you want to explicitly say a variable is empty or hasn't been assigned yet, you use `None`. It is not zero, it is not an empty string; it is literally a special type called `NoneType`.
```python
model_weights = None  # We haven't loaded the AI model yet.
```

### Truthiness
Every single piece of data in Python has an inherent `True` or `False` vibe when you force it into a Boolean using `bool()`.
- **Falsy values:** `0`, `0.0`, `""` (empty string), `None`
- **Truthy values:** Literally anything else (`1`, `"hello"`, `-5`)

```python
name = ""
if name:  # Python secretly checks bool(name), which is False!
    print("You have a name!")
else:
    print("You didn't type anything!") # This runs
```

### Multiple Assignment
You can assign multiple variables on a single line. This is heavily used in machine learning when functions return multiple values (like a loss and an accuracy).
```python
x, y = 10, 20
```

## 2. Operators (Under the Hood)

### Identity (`is`) vs. Equality (`==`)
This is a famous Python interview question. 
- `==` asks: "Do these two things have the same value?"
- `is` asks: "Are these two things literally the exact same object in the computer's memory?"

```python
# ALWAYS use 'is' when checking for None:
if my_variable is None:
    print("It is empty.")
```

### Membership Operators (`in`, `not in`)
This checks if something exists inside a collection (like a string, or later, a list).
```python
if "a" in "apple":
    print("Yes!") # This prints
```

## 3. Advanced Control Flow

### Nested Loops
A loop inside a loop. This is exactly how Deep Learning models process grids of pixels or matrices of numbers!
```python
for row in range(3):
    for col in range(3):
        print(f"Row {row}, Column {col}")
```

### Iterating Directly
In languages like C, you use `range()` to count indexes. In Python, you can loop directly over the items themselves!
```python
word = "GPT"
for letter in word:
    print(letter) # Prints G, then P, then T.
```

### The `match` / `case` Statement
Added in Python 3.10, this replaces ugly walls of `elif` statements. It is perfect for handling different commands or status codes.
```python
status_code = 404

match status_code:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case _:
        print("Unknown error") # The underscore means 'else' or 'default'
```

### The `pass` Keyword
Sometimes you need to write an `if` statement or a loop, but you don't know what code to put inside it yet. Python will crash if you leave it empty. You use `pass` to say "Do nothing, I'll write this later."
```python
if score == 100:
    pass # TODO: write celebration code later
```
