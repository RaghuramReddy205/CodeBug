sen = input("Enter a Sentence : ").lower()
count_w = 0
for i in range(0, len(sen)):
    if sen[i] in 'qwertyuiopasdfghjklzxcvbnm':
        continue
    elif sen[i] == ' ':
        count_w += 1
print(count_w+1)