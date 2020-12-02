A1 = [1, 4, 9]
A2 = [9, 9, 9]
A3 = [9, 8, 0]


def plus_one(a):
    a[-1] += 1
    for i in reversed(range(1, len(a))):
        if a[i] != 10:
            break
        a[i] = 0
        a[i-1] += 1
    if a[0] == 10:
        a[0] = 1
        a.append(0)
    return a


print(plus_one(A1))
print(plus_one(A2))
print(plus_one(A3))
