def countdown(n):
    """Recursively count down from n to 1, then print 'Blastoff!'."""
    if n <= 0:
        # Base case: when n is 0 or less, stop counting and print Blastoff!
        print("Blastoff!")
    else:
        # Recursive case: print current value, then call countdown with n - 1
        print(n)
        countdown(n - 1)


def countup(n):
    """Recursively count up from a negative number to -1, then print 'Blastoff!'."""
    if n >= 0:
        # Base case: once we reach 0 or higher, we stop counting and print Blastoff!
        print("Blastoff!")
    else:
        # Recursive case: print current value, then call countup with n + 1
        print(n)
        countup(n + 1)


def main():
    # Get user input as a string using input (Python 3) and convert to int
    user_input = input("Enter an integer (positive, negative, or zero): ")
    n = int(user_input)

    # Decide which function to call based on the sign of n
    if n > 0:
        # For a positive number, we count down to Blastoff!
        countdown(n)
    elif n < 0:
        # For a negative number, we count up to Blastoff!
        countup(n)
    else:
        # For zero, treat it as the launch point and print Blastoff! directly
        countdown(n)  # countdown(0) immediately hits the base case and prints Blastoff


if __name__ == "__main__":
    main()


# This version intentionally has no error handling to demonstrate a runtime error.

numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

# This line can cause a ZeroDivisionError at runtime if denominator is 0.
result = numerator / denominator

print("Result of division:", result)


# Safe division with a guard condition against division by zero.

numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

if denominator == 0:
    # This branch handles the error scenario before it happens.
    print("Error: Division by zero is not allowed. Please use a non-zero denominator.")
else:
    # This branch only runs when denominator is safe (non-zero).
    result = numerator / denominator
    print("Result of division:", result)


# Safe division using try/except to catch ZeroDivisionError.

numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

try:
    # This line may raise ZeroDivisionError if denominator is zero.
    result = numerator / denominator
    print("Result of division:", result)
except ZeroDivisionError:
    # This block only runs if a ZeroDivisionError occurs.
    print(
        "Runtime error: You attempted to divide by zero. Please enter a non-zero denominator next time."
    )
