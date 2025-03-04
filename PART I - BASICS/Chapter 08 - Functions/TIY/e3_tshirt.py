# 8-3 T-Shirt
def make_shirt(size, message):
    """Displays the details of a T-Shirt order"""
    print(f"\nHere is the summary of your T-Shirt order.")
    print(f"\nSize: {size}")
    print(f"Message: {message}")


make_shirt('M', 'Ad Astra Per Aspera')
make_shirt(message='Per Aspera Ad Astra', size='S')
