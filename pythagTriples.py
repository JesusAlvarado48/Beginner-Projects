# This program checks if three sides form a Pythagorean triple.
# A Pythagorean triple consists of three positive integers a, b, and c
# such that a^2 + b^2 = c^2.

def get_int(prompt):
    """Safely get an integer from the user."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ("exit", "quit"):
            print("Exiting the program. Goodbye!")
            exit()

        try:
            return int(user_input)
        except ValueError:
            print("That's not a valid integer. Please try again.\n")

def is_pythagorean_triple(a, b, c):
    """Return True if a, b, c form a Pythagorean triple."""
    sides = sorted([a, b, c])  # ensures sides[2] is the hypotenuse
    return sides[0]**2 + sides[1]**2 == sides[2]**2


def pythagTriples():
    print("Welcome to the Pythagorean Triple Checker!\n")
    print("A Pythagorean triple is a set of three positive integers "
          "a, b, and c such that a^2 + b^2 = c^2.\n")

    while True:
        a = get_int("Enter side a (or type 'exit' to quit): ")
        b = get_int("Enter side b (or type 'exit' to quit): ")
        c = get_int("Enter side c (or type 'exit' to quit): ")

        if is_pythagorean_triple(a, b, c):
            print("\nThis IS a Pythagorean triple.")
        else:
            print("\nThis is NOT a Pythagorean triple.")
        while True:
            again = input("\nWould you like to check another? (y/n): ").strip().lower()
            if again in ("y", "yes"):
                break
            elif again in ("n", "no"):
                print("Thank you for using the Pythagorean Triple Checker!")             
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    pythagTriples()