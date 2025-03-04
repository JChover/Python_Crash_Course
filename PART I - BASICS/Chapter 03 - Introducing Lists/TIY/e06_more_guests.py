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
