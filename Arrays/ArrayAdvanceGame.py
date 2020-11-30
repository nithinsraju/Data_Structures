def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i<= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    print(furthest_reached)
    return furthest_reached >= last_idx

A1 = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A1))
A2 = [3, 2, 1, 0, 0, 4, 5]
print(array_advance(A2))