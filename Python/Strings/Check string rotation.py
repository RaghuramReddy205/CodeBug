s1 = input("Enter string 1 : ")
s2 = input("Enter string 2 : ")
if len(s1) != len(s2):
    print("Rotation not possible")
else:
    new = s1+s1
    if s2 in new:
        print("Rotation Possible")