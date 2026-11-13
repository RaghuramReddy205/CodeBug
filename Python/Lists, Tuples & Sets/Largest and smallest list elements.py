n = int(input("Enter the size of the list : "))
a = []
for i in range(n):
    x = int(input(f"Enter the element {i+1} : "))
    a.append(x)

max = a[0]
for j in range(1, n):
    if a[j] > max:
        max = a[j]
print(f'The largest element in the list is {max}')
min = a[0]
for k in range(1, n):
    if a[k] < min :
        min = a[k]
print(f'The smallest element in the list is {min}')
