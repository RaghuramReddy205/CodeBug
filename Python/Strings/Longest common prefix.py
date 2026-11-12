
n = int(input("Enter number of strings: "))

arr = []

for i in range(n):
    s = input("Enter string: ")
    arr.append(s)

prefix = ""

for i in range(len(arr[0])):
    ch = arr[0][i]
    found = True

    for j in range(1, n):
        if i >= len(arr[j]) or arr[j][i] != ch:
            found = False
            break

    if found:
        prefix += ch
    else:
        break

print("Longest common prefix:", prefix)
