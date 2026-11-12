s = input("Enter Sentence : ")
new = s.split()
max = 0
long = ""
for i in range(len(new)):
    if len(new[i]) > max:
        max = len(new[i])
        long = new[i]

print("The longest word is " +  long + " with length ", max)