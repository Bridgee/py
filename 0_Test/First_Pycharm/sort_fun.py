def sort_fun(a):
    for i in range(len(a)):
        mini = i
        for j in range(i+1, len(a)):
            if a[mini] > a[j]:
               mini = j
        b = a[i]
        a[i] = a[mini]
        a[mini] = b
    return a


if __name__ == "__main__":
    a = [9, 3, 8, 2, 4, 2, 99, 3]
    print(a)
    sort_fun(a)
    print('After sort')
    print(a)