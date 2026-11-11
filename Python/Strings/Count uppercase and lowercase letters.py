s = input("Enter a string : ")
count_U = 0
count_l = 0
for i in range(0, len(s)):
    if s[i] in 'qwertyuiopasdfghjklzxcvbnm':
        count_l += 1
    elif s[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        count_U += 1
print("Count of Uppercase letters are : ", count_U)
print("Count of Lowercase letters are : ", count_l)