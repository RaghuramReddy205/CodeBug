
s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s) - 1):

    if s[i] == s[i + 1]:
        count += 1

    else:
        result += s[i] + str(count)
        count = 1

# Add the last character and its count
if len(s) > 0:
    result += s[len(s) - 1] + str(count)

print("Compressed string:", result)
