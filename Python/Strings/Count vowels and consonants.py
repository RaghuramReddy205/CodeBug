s = input("Enter a string : ").lower()
l = len(s)
count_v = 0
count_c = 0
for i in range(0, l):
    if s[i] in 'aieou':
        count_v += 1
    elif s[i] in 'qwrtypsdfghjklzxcvbnm':
        count_c += 1
print(count_v)
print(count_c)