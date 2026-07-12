# Topic: Variables, Primitive Types, and Type Conversion

# Goal: Create a simple script that asks the user for their name and birth year.
# Then, calculate their age and print a formatted message.

user_name = input("What is your name? ")
birth_year = input("What year were you born? ")

birth_year_int = int(birth_year)
age = 2026 - birth_year_int

print(f"Hello, {user_name}! You are turning {age} years old this year.")
