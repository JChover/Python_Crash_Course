guest_list = ['socrates', 'seneca', 'zenon', 'platon', 'aristoteles']  # This is my list of guests
print(guest_list)

# This is an extract of Activity 9 where I got some INDEX ERRORS using the pop() and del to reduce a LIST

removed_guest = guest_list.pop(3)
print(f"Dear Mr. {removed_guest.title()}, I'm sorry to inform you have been uninvited.")
removed_guest = guest_list.pop(2)
print(f"Dear Mr. {removed_guest.title()}, I'm sorry to inform you have been uninvited.")
removed_guest = guest_list.pop(0)
print(f"Dear Mr. {removed_guest.title()}, I'm sorry to inform you have been uninvited.\n")

# I didn't kept in mind that after doing pop or del, the LIST will be REDUCED so for example
# In a LIST of LEN 4 if I pop(3) then my LIST has a LEN 3 so I get an error if I pop(3) again

del guest_list[1]
del guest_list[0]

print(guest_list)
print(f"\nMy guests list is {len(guest_list)} people long.\n")
