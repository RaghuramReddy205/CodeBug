s = input("Enter a string: ")
l = len(s)
rev = ""
for i in range(l-1, -1, -1):
    rev += s[i]
if rev == s:
    print("Palindrome")
else:
    print("Not Palindrome")