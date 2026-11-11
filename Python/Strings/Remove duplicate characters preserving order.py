s = input("Enter a string : ")
check = ""
for i in range(len(s)):
    if s[i] in check:
        continue
    else:
        check += s[i]
print(check)