a = [1, 1]
print(a)
for i in range(2, 7):
    b = []
    for j in range(len(a) - 1):
        b.append(a[j])
        b.append(a[j] + a[j + 1])
    b.append(a[len(a) - 1])
    a = b
    print(a)
