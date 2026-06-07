# Bubble Sort — O(n²) no pior caso
# Implementado por: Hugo

def bubble_sort(arr):
    a = arr.copy()
    trocas = 0
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                trocas += 1
    return a, trocas