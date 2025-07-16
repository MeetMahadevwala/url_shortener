import random
import string

CHARACTER_SET = string.ascii_letters + string.digits

def generate_short_code(length=6):
    """
    Generates a random short code of a specified length using the defined CHARACTER_SET.

    This function serves as the core generator for the unique identifiers
    that will map to the original long URLs.

    Args:
        length (int): The desired length of the short code. Defaults to 6.

    Returns:
        str: A randomly generated string of the specified length.
    """

    generate_code = "".join(random.choices(CHARACTER_SET, k=length))
    return generate_code

if __name__ == '__main__':
    print("--- Testing generate_test_code ---")
    print("Generate 5 codes with default length (6):")
    # Test 1: Generate a few codes with the default length 6
    for _ in range(5):
        print(generate_short_code())

    print("\n" + "-"*20 + "\n")

    # Test 2: Generate a code with custom length 10
    print("Generating 1 code wtih custom length (10):")
    print(generate_short_code(10))
    print("\n" + "--- Test Complete ---")