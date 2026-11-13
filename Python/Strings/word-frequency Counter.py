
s = input("Enter a sentence: ")

words = s.lower().split()

visited = []

for i in range(len(words)):

    if words[i] not in visited:

        count = 0

        for j in range(len(words)):
            if words[i] == words[j]:
                count += 1

        print(words[i], ":", count)

        visited.append(words[i])
