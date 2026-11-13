n = int(input("Enter the size of the list : "))
a = []
for i in range(n):
    x = int(input("Enter the element to add : "))
    a.append(x)
max1 = 0
max2 = 0
if a[0]>a[1]:
    max1 = a[0]
    max2 = a[1]
else:
    max2 = a[0]
    max1 = a[1]
for i in range(2, n):
    if a[i]>max1:
        max2 = max1
        max1 = a[i]
    elif a[i]<max2:
        max2 = a[i]
print(f'The second largest element is {max2}')

