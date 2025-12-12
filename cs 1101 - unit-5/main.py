# Unit 5 Assignment: Iterations and Strings
# This program displays a student's name and performs:
# (1) prints first n characters from the left (n is user input)
# (2) counts vowels
# (3) reverses the name

name = "John Smith"

print("Name:", name)

# ===== Part 1(a): Display first n characters from the left =====
n = int(input("Enter n (number of characters from the left): "))

# Slicing safely: if n is larger than length, Python returns the whole string (no error)
left_n = name[:n]
print(f"First {n} characters from left:", left_n)

# ===== Part 1(b): Count the number of vowels =====
vowels = "aeiou"
count = 0

# Loop through each character and check vowels (case-insensitive)
for ch in name.lower():
    if ch in vowels:
        count += 1

print("Number of vowels:", count)

# ===== Part 1(c): Reverse the name =====
reversed_name = name[::-1]  # slicing with step -1 reverses the string
print("Reversed name:", reversed_name)
