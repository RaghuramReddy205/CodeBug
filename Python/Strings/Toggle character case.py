s = input("Enter a String : ")
toggle = ""
for i in range(0, len(s)):
    if s[i] in 'qwertyuiopasdfghjklzxcvbnm':
        toggle += s[i].upper()
    elif s[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        toggle += s[i].lower()
print(toggle)


