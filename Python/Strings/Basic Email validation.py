
email = input("Enter email: ")

at_count = 0
at_pos = -1
valid = True

for i in range(len(email)):
    if email[i] == '@':
        at_count += 1
        at_pos = i

    if email[i] == ' ':
        valid = False

if at_count != 1:
    valid = False

elif at_pos == 0 or at_pos == len(email) - 1:
    valid = False

else:
    dot_found = False

    for i in range(at_pos + 1, len(email)):
        if email[i] == '.':
            dot_found = True

    if not dot_found:
        valid = False

    elif email[len(email) - 1] == '.':
        valid = False

if valid:
    print("Valid Email")
else:
    print("Invalid Email")
