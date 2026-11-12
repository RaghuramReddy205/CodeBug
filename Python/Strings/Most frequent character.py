s = input("Enter a String : ")
max = 0
long = ""
for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if count > max:
        max = count
        long = s[i]
print("Most frequent character:", long)
print("Frequency:", max)
