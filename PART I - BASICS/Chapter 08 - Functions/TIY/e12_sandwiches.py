# 8-12 Sandwiches
def make_sandwich(*items):
    """
    Prints a summary of the sandwich that's being ordered.

    Parameters:
    *items: Variable length argument list representing the items on the sandwich.
    """
    print("\nMaking a Sandwich with the following items:")
    for item in items:
        print(f"- {item}")


# Example usage:
make_sandwich('ham', 'cheese')
make_sandwich('turkey', 'lettuce', 'tomato', 'mayo')
make_sandwich('peanut butter', 'jelly')
