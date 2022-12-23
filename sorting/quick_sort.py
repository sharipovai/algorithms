def quick_sort(a):
    if len(a) <= 1:
        return a
    center = [i for i in a if i == a[0]]
    left = list(filter(lambda x: x<a[0], a))
    right = list(filter(lambda x: x>a[0], a))
    return quick_sort(left) + center + quick_sort(right)

a = [9, 5, 7, -5, 0, 0, 1]
print(quick_sort(a))