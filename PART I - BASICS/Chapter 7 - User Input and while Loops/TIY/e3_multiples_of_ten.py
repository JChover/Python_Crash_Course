# 7-3 Multiples of Ten
number = int(input("\nEnter a number, and I'll tell you if it's a multiple of ten: "))

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of ten.")
else:
    print(f"\nThe number {number} is not a multiple of ten.")
