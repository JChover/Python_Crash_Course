magicians = ['alice', 'david', 'carolina']

for magician in magicians:  # Pull a name from the LIST, and associate it with the variable magician in a loop
    print(magician.title())

print()

for magician in magicians:  #
    print(f"{magician.title()}, that was a great trick!")  # It is possible to print f-strings

print()

for magician in magicians:  #
    print(f"{magician.title()}, that was a great trick!")  # Is it possible to perform more than one action inside
    print(f"I can't wait to see your next trick, {magician.title()}!\n")  # As long as code is INDENTED
print("Thank you, everyone. That was a great magic show!")  # Code not INDENTED will be executed AFTER the LOOP

# for magician in magicians:  # Example of INDENTATION ERROR
# print(magician.title())  # Also if you indent CODE without a LOOP, will output an ERROR



