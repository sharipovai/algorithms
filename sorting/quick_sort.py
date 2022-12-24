import random
def quick_sort(a):
    if len(a) <= 1:
        return a
    elem = random.choice(a)
    center = [i for i in a if i == elem]
    left = list(filter(lambda x: x<elem, a))
    right = list(filter(lambda x: x>elem, a))
    return quick_sort(left) + center + quick_sort(right)

a = [9, 5, 7, -5, 0, 0, 1]
print(quick_sort(a))