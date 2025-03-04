guest_list = ['socrates', 'seneca', 'zenon', 'platon']  # This is my list of guests

# These are my invitations
print(f"I would like to invite Mr. {guest_list[0].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[1].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[2].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[3].title()} to my dinner.\n")

print(f"Mr. {guest_list[1].title()} is not able to attend the dinner.\n")

guest_list[1] = 'aristoteles'

print(f"I would like to invite Mr. {guest_list[0].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[1].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[2].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[3].title()} to my dinner.\n")

print("Dear attendants, I'm glad to infor you that a bigger table is available.\n")

guest_list.insert(0, 'homero')  # This ADDS a new guest at the BEGINNING of the LIST
guest_list.insert(2, 'ovidio')  # This ADDS a new guest at the MIDDLE of the LIST
guest_list.append('marco aurelio')  # This APPENDS a new guest at the END of the LIST

print(f"I would like to invite Mr. {guest_list[0].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[1].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[2].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[3].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[4].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[5].title()} to my dinner.")
print(f"I would like to invite Mr. {guest_list[6].title()} to my dinner.\n")

print("Dear attendants, seems like at the end, only a table for 2 is available.\n")

print(guest_list)

removed_guest = guest_list.pop(6)
print(f"\nDear Mr. {removed_guest.title()}, I'm sorry to inform you have been uninvited.")
removed_guest = guest_list.pop(4)
print(f"Dear Mr. {removed_guest.title()}, I'm sorry to inform you have been uninvited.")
removed_guest = guest_list.pop(3)
print(f"Dear Mr. {removed_guest.title()}, I'm sorry to inform you have been uninvited.")
removed_guest = guest_list.pop(2)
print(f"Dear Mr. {removed_guest.title()}, I'm sorry to inform you have been uninvited.")
removed_guest = guest_list.pop(0)
print(f"Dear Mr. {removed_guest.title()}, I'm sorry to inform you have been uninvited.\n")

print(guest_list)

print(f"\nMr. {guest_list[0].title()} you are still invited to my dinner.")
print(f"Mr. {guest_list[1].title()} you are still invited to my dinner.\n")

del guest_list[1]
del guest_list[0]

print(guest_list)
