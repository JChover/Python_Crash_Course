first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"  #This is called f-string (format string)
full_name_test = first_name + " " + last_name  #Alternative way to do full name

print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"  #You can assign f-strings to variables
print(message)
