s1 = input("Enter string 1 : ")
s2 = input("Enter String 2 : ")
if len(s1) != len(s2):
    print("Not anagrams")
else:
    for i in range(len(s1)):
        if s1[i] in s2:
            print("Anagrams")
            break
        else:
            print("Not anagrams")
            break
