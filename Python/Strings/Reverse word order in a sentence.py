sen = input("Enter a Sentence : ")
rev_list = sen.split()
for i in range(len(rev_list)-1, -1, -1):
    print(rev_list[i], end  = " ")