def quick_sort(a):
    if a == []:
        return []
    if len(a) == 1:
        return a
    center = []
    left = []
    right = []
    center.append(a[0])
    for i in range(1, len(a)):
        if a[i] < center[0]:
            left.append(a[i])
        else:
            right.append(a[i])
    return quick_sort(left) + center + quick_sort(right)

a = [9, 5, 7, -5, 0, 0, 1]
print(quick_sort(a))