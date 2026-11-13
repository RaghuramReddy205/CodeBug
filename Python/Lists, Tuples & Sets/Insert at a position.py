size = int(input("Enter the size of the list : "))
a = []
for i in range(size):
    x = int(input(f'Enter the element {i+1} : '))
    a.append(x)
n = int(input("Enter the element to add : "))
p = int(input("Enter the position to add : "))
a.insert(n, p)
print(a)