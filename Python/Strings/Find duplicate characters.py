s = input("Enter a string : ")
check = ""
for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if count > 1 and s[i] not in check:
        print(s[i])
        check += s[i]
if check == "":
    print("No duplicate characters")