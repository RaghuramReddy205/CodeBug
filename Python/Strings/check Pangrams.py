s = input("Enter a sentence: ").lower()
check = "abcdefghijklmnopqrstuvwxyz"

flag = True

for i in range(len(check)):
    if check[i] not in s:
        flag = False
        break

if flag:
    print("Pangram")
else:
    print("Not a Pangram")