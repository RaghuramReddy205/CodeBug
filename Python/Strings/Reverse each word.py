sen = input("Enter Sentence : ").lower()
rev_list = sen.split()
for i in range(0, len(rev_list)):
    for j in range(len(rev_list[i])-1, -1, -1):
        if rev_list[i][j] in 'qwertyuiopasdfghjklzxcvbnm':
            print(rev_list[i][j], end="")
        elif rev_list[i][j] == " ":
            print(" ")
    print("", end = " ")