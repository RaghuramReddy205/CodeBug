s = input("Enter a String: ")
rev = ""
l = len(s)
for i in range(l-1, -1, -1):
    rev = rev + s[i]
print(rev)