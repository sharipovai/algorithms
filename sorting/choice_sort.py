def choice_sort(a):
    if len(a) <=1:
        return a
    if len(a) == 2:
        return a if a[0] > a[1] else a[::-1]
    max_d = max(a)
    max_arr = [i for i in a if i == max_d]
    smaller = list(filter(lambda x: x<max_d, a))
    return max_arr + choice_sort(smaller)

a = [0, 1, 0, -1, 10, 5, 11]
print(choice_sort(a))
    